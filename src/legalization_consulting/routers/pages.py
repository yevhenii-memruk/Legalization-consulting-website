from typing import Annotated

from fastapi import APIRouter, Depends, Query, Request
from fastapi.responses import HTMLResponse

from legalization_consulting.core.config import Settings, get_settings
from legalization_consulting.core.i18n import LANGUAGES, get_page_content
from legalization_consulting.core.privacy_content import get_privacy_content
from legalization_consulting.core.templating import templates

router = APIRouter(include_in_schema=False)


@router.get("/", response_class=HTMLResponse)
async def home(
    request: Request,
    settings: Annotated[Settings, Depends(get_settings)],
    lang: Annotated[str | None, Query(max_length=8)] = None,
) -> HTMLResponse:
    language, content = get_page_content(lang)
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "company_name": settings.name,
            "content": content,
            "contact_email": settings.contact_email,
            "current_language": language,
            "languages": LANGUAGES,
        },
    )


@router.get("/privacy", response_class=HTMLResponse)
async def privacy(
    request: Request,
    settings: Annotated[Settings, Depends(get_settings)],
    lang: Annotated[str | None, Query(max_length=8)] = None,
) -> HTMLResponse:
    language, content = get_privacy_content(lang)
    _, shared_content = get_page_content(language)
    return templates.TemplateResponse(
        request=request,
        name="privacy.html",
        context={
            "company_name": settings.name,
            "contact_email": settings.contact_email,
            "content": content,
            "shared_content": shared_content,
            "current_language": language,
            "languages": LANGUAGES,
        },
    )
