from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from legalization_consulting.core.config import Settings, get_settings
from legalization_consulting.core.paths import STATIC_DIR
from legalization_consulting.core.security import SecurityHeadersMiddleware
from legalization_consulting.integrations.google_sheets import GoogleSheetsLeadStore
from legalization_consulting.routers import api, leads, pages
from legalization_consulting.services.leads import DisabledLeadStore, LeadStore
from legalization_consulting.services.rate_limit import LeadRateLimiter


def create_app(
    *,
    settings: Settings | None = None,
    lead_store: LeadStore | None = None,
) -> FastAPI:
    """Create and configure the FastAPI application."""
    settings = settings or get_settings()
    application = FastAPI(
        title=settings.name,
        description=settings.description,
        version=settings.version,
        debug=settings.debug,
    )
    if lead_store is not None:
        application.state.lead_store = lead_store
    elif settings.leads_enabled:
        application.state.lead_store = GoogleSheetsLeadStore(
            spreadsheet_id=settings.google_sheets_spreadsheet_id or "",
            sheet_range=settings.google_sheets_range,
        )
    else:
        application.state.lead_store = DisabledLeadStore()

    application.state.lead_rate_limiter = LeadRateLimiter(
        limit=settings.lead_rate_limit,
        window_seconds=settings.lead_rate_window_seconds,
    )
    application.add_middleware(SecurityHeadersMiddleware)
    application.mount(
        "/static",
        StaticFiles(directory=STATIC_DIR),
        name="static",
    )
    application.include_router(pages.router)
    application.include_router(api.router)
    application.include_router(leads.router)

    return application


app = create_app()
