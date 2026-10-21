from typing import Annotated

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse

from legalization_consulting.core.config import Settings, get_settings
from legalization_consulting.core.templating import templates

router = APIRouter(include_in_schema=False)


@router.get("/", response_class=HTMLResponse)
async def home(
    request: Request,
    settings: Annotated[Settings, Depends(get_settings)],
) -> HTMLResponse:
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"company_name": settings.name},
    )
