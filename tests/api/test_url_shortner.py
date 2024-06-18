from http import HTTPStatus
from httpx import AsyncClient
from main import app
from src.repository import find_url_by_hash


async def test_shorten_url(api: AsyncClient, db):
    response = await api.post(
        app.url_path_for("shorten_url"), params={"url": "google.com"}
    )

    assert response.status_code == HTTPStatus.OK
    url = await find_url_by_hash(db, response.json()["hashed_url"])
    assert url.original_url == "google.com"


async def test_find_url(api: AsyncClient):
    hashed_url = (
        await api.post(app.url_path_for("shorten_url"), params={"url": "https://www.google.com"})
    ).json()["hashed_url"]

    response = await api.get(app.url_path_for("get_url_by_hash", hashed_url=hashed_url))

    assert response.status_code == HTTPStatus.TEMPORARY_REDIRECT
    assert response.next_request.url == "https://www.google.com"
