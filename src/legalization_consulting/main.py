from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from legalization_consulting.core.config import get_settings
from legalization_consulting.core.paths import STATIC_DIR
from legalization_consulting.routers import api, pages


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    settings = get_settings()
    application = FastAPI(
        title=settings.name,
        description=settings.description,
        version=settings.version,
        debug=settings.debug,
    )
    application.mount(
        "/static",
        StaticFiles(directory=STATIC_DIR),
        name="static",
    )
    application.include_router(pages.router)
    application.include_router(api.router)

    return application


app = create_app()
