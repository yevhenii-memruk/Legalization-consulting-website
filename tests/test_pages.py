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
    assert 'type="button" data-demo-submit' in response.text


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
