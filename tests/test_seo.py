from xml.etree import ElementTree

from fastapi.testclient import TestClient

from legalization_consulting.core.config import Settings
from legalization_consulting.main import create_app


def test_unconfigured_site_is_not_indexable(client: TestClient) -> None:
    page = client.get("/")
    robots = client.get("/robots.txt")
    sitemap = client.get("/sitemap.xml")

    assert '<meta name="robots" content="noindex,nofollow">' in page.text
    assert 'rel="canonical"' not in page.text
    assert robots.status_code == 200
    assert robots.text == "User-agent: *\nDisallow: /\n"
    assert sitemap.status_code == 404


def test_configured_site_has_localized_search_metadata() -> None:
    settings = Settings(
        _env_file=None,
        public_base_url="https://nonstopdocuments.example",
    )
    with TestClient(create_app(settings=settings)) as client:
        response = client.get("/", params={"lang": "uk"})

    assert response.status_code == 200
    assert '<meta name="robots" content="index,follow">' in response.text
    assert (
        '<link rel="canonical" href="https://nonstopdocuments.example/?lang=uk">' in response.text
    )
    assert response.text.count('rel="alternate" hreflang=') == 5
    assert 'hreflang="x-default" href="https://nonstopdocuments.example/"' in response.text
    assert (
        '<meta property="og:url" content="https://nonstopdocuments.example/?lang=uk">'
        in response.text
    )
    assert (
        '<meta property="og:image" '
        'content="https://nonstopdocuments.example/static/images/og-cover.png">' in response.text
    )


def test_configured_site_exposes_robots_and_sitemap() -> None:
    settings = Settings(
        _env_file=None,
        public_base_url="https://nonstopdocuments.example/",
    )
    with TestClient(create_app(settings=settings)) as client:
        robots = client.get("/robots.txt")
        sitemap = client.get("/sitemap.xml")

    assert robots.text == (
        "User-agent: *\nAllow: /\nSitemap: https://nonstopdocuments.example/sitemap.xml\n"
    )
    assert sitemap.status_code == 200
    assert sitemap.headers["content-type"].startswith("application/xml")

    document = ElementTree.fromstring(sitemap.content)
    namespace = {"sitemap": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locations = [element.text for element in document.findall("sitemap:url/sitemap:loc", namespace)]
    assert len(locations) == 8
    assert "https://nonstopdocuments.example/" in locations
    assert "https://nonstopdocuments.example/?lang=en" in locations
    assert "https://nonstopdocuments.example/privacy?lang=ru" in locations
