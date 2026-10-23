import pytest
from fastapi.testclient import TestClient


def test_home_page(client: TestClient) -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Non-stop Documents" in response.text
    assert 'id="services"' in response.text
    assert 'id="process"' in response.text
    assert 'id="faq"' in response.text
    assert "Karta pobytu" in response.text
    assert 'action="/api/leads"' in response.text
    assert 'method="post"' in response.text
    assert 'type="submit" data-lead-submit' in response.text


@pytest.mark.parametrize(
    ("language", "expected_text"),
    [
        ("pl", "Twoje dokumenty."),
        ("uk", "Ваші документи."),
        ("ru", "Ваши документы."),
        ("en", "Your documents."),
    ],
)
def test_home_page_language(
    client: TestClient,
    language: str,
    expected_text: str,
) -> None:
    response = client.get("/", params={"lang": language})

    assert response.status_code == 200
    assert f'<html lang="{language}">' in response.text
    assert expected_text in response.text
    assert response.text.count('aria-current="page"') == 1


def test_unknown_language_falls_back_to_polish(client: TestClient) -> None:
    response = client.get("/", params={"lang": "de"})

    assert response.status_code == 200
    assert '<html lang="pl">' in response.text
    assert "Twoje dokumenty." in response.text


def test_security_headers(client: TestClient) -> None:
    response = client.get("/")

    assert response.headers["content-security-policy"].startswith("default-src 'self'")
    assert "frame-ancestors 'none'" in response.headers["content-security-policy"]
    assert response.headers["permissions-policy"] == "camera=(), geolocation=(), microphone=()"
    assert response.headers["referrer-policy"] == "strict-origin-when-cross-origin"
    assert response.headers["x-content-type-options"] == "nosniff"
    assert response.headers["x-frame-options"] == "DENY"


def test_landing_page_assets(client: TestClient) -> None:
    stylesheet = client.get("/static/css/styles.css")
    script = client.get("/static/js/main.js")
    image = client.get("/static/images/warsaw-skyline.jpg")
    favicon = client.get("/static/images/favicon.svg")

    assert stylesheet.status_code == 200
    assert stylesheet.headers["content-type"].startswith("text/css")
    assert script.status_code == 200
    assert "javascript" in script.headers["content-type"]
    assert image.status_code == 200
    assert image.headers["content-type"] == "image/jpeg"
    assert favicon.status_code == 200
    assert favicon.headers["content-type"] == "image/svg+xml"
