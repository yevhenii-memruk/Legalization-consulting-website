from fastapi.testclient import TestClient


def test_home_page(client: TestClient) -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Non-stop Documents" in response.text
