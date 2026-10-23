from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError

from legalization_consulting.core.config import Settings
from legalization_consulting.main import create_app
from legalization_consulting.services.leads import LeadRecord, LeadStorageError


class RecordingLeadStore:
    def __init__(self) -> None:
        self.leads: list[LeadRecord] = []

    async def append(self, lead: LeadRecord) -> None:
        self.leads.append(lead)


class FailingLeadStore:
    async def append(self, lead: LeadRecord) -> None:
        del lead
        raise LeadStorageError("test storage failure")


@pytest.fixture
def lead_store() -> RecordingLeadStore:
    return RecordingLeadStore()


@pytest.fixture
def lead_client(lead_store: RecordingLeadStore) -> Iterator[TestClient]:
    settings = Settings(_env_file=None)
    app = create_app(settings=settings, lead_store=lead_store)
    with TestClient(app) as client:
        yield client


def test_create_lead(lead_client: TestClient, lead_store: RecordingLeadStore) -> None:
    response = lead_client.post(
        "/api/leads",
        json={
            "full_name": "  Jan   Kowalski  ",
            "phone": "+48 123-456-789",
            "comment": "  Karta pobytu  ",
            "language": "pl",
            "company_website": "",
        },
    )

    assert response.status_code == 201
    assert response.json() == {"status": "accepted"}
    assert len(lead_store.leads) == 1

    lead = lead_store.leads[0]
    assert lead.full_name == "Jan Kowalski"
    assert lead.phone == "+48123456789"
    assert lead.comment == "Karta pobytu"
    assert lead.created_at.tzinfo is not None
    assert lead.as_sheet_row()[5:] == ["pl", "website"]


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("full_name", "J"),
        ("phone", "call-me"),
        ("phone", "+48 12"),
        ("comment", "x" * 1001),
        ("language", "de"),
    ],
)
def test_rejects_invalid_lead_data(
    lead_client: TestClient,
    lead_store: RecordingLeadStore,
    field: str,
    value: str,
) -> None:
    payload = {"full_name": "Jan Kowalski", "phone": "+48123456789"}
    payload[field] = value

    response = lead_client.post("/api/leads", json=payload)

    assert response.status_code == 422
    assert lead_store.leads == []


def test_honeypot_accepts_without_storing(
    lead_client: TestClient,
    lead_store: RecordingLeadStore,
) -> None:
    response = lead_client.post(
        "/api/leads",
        json={
            "full_name": "Spam Bot",
            "phone": "+48123456789",
            "company_website": "https://spam.invalid",
        },
    )

    assert response.status_code == 201
    assert response.json() == {"status": "accepted"}
    assert lead_store.leads == []


def test_returns_service_unavailable_when_storage_fails() -> None:
    app = create_app(settings=Settings(_env_file=None), lead_store=FailingLeadStore())

    with TestClient(app) as client:
        response = client.post(
            "/api/leads",
            json={"full_name": "Jan Kowalski", "phone": "+48123456789"},
        )

    assert response.status_code == 503
    assert response.json() == {
        "detail": "Consultation requests are temporarily unavailable"
    }


def test_rate_limits_repeated_submissions(
    lead_client: TestClient,
    lead_store: RecordingLeadStore,
) -> None:
    payload = {"full_name": "Jan Kowalski", "phone": "+48123456789"}

    responses = [lead_client.post("/api/leads", json=payload) for _ in range(6)]

    assert [response.status_code for response in responses] == [201, 201, 201, 201, 201, 429]
    assert responses[-1].headers["retry-after"] == "600"
    assert len(lead_store.leads) == 5


def test_lead_collection_requires_spreadsheet_id() -> None:
    with pytest.raises(ValidationError):
        Settings(
            _env_file=None,
            leads_enabled=True,
            google_sheets_spreadsheet_id=None,
        )
