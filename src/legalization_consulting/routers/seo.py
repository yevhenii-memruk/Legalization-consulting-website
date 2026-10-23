"""Search-engine discovery endpoints."""

from xml.etree.ElementTree import Element, SubElement, tostring

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import PlainTextResponse, Response

from legalization_consulting.core.config import Settings
from legalization_consulting.core.i18n import LANGUAGES
from legalization_consulting.core.seo import localized_path, public_origin

router = APIRouter(include_in_schema=False)


@router.get("/robots.txt", response_class=PlainTextResponse)
async def robots(request: Request) -> PlainTextResponse:
    """Allow indexing only after a trusted production origin is configured."""
    settings: Settings = request.app.state.settings
    origin = public_origin(settings.public_base_url)
    if origin is None:
        return PlainTextResponse("User-agent: *\nDisallow: /\n")

    return PlainTextResponse(f"User-agent: *\nAllow: /\nSitemap: {origin}/sitemap.xml\n")


@router.get("/sitemap.xml")
async def sitemap(request: Request) -> Response:
    """Return canonical URLs for every public language version."""
    settings: Settings = request.app.state.settings
    origin = public_origin(settings.public_base_url)
    if origin is None:
        raise HTTPException(status_code=404, detail="Sitemap is not configured")

    urlset = Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for path in ("/", "/privacy"):
        for language in LANGUAGES:
            url = SubElement(urlset, "url")
            location = SubElement(url, "loc")
            location.text = f"{origin}{localized_path(path, language['code'])}"

    body = tostring(urlset, encoding="utf-8", xml_declaration=True)
    return Response(content=body, media_type="application/xml")
