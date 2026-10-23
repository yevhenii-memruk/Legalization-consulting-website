from typing import Annotated

from fastapi import APIRouter, Depends, Query, Request
from fastapi.responses import HTMLResponse

from legalization_consulting.core.config import Settings, get_settings
from legalization_consulting.core.i18n import LANGUAGES, get_page_content
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
            "current_language": language,
            "languages": LANGUAGES,
        },
    )
