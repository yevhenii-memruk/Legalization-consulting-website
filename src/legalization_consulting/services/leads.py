"""Lead-processing use case and storage boundary."""

from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Protocol
from uuid import UUID, uuid4
from zoneinfo import ZoneInfo

from legalization_consulting.schemas.leads import LeadCreate, LeadLanguage

WARSAW_TIME_ZONE = ZoneInfo("Europe/Warsaw")
SHEET_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


@dataclass(frozen=True, slots=True)
class LeadRecord:
    """Validated lead enriched with server-owned metadata."""

    lead_id: UUID
    created_at: datetime
    full_name: str
    phone: str
    comment: str | None
    language: LeadLanguage
    source: str = "website"

    def as_sheet_row(self) -> list[str]:
        """Return values in the documented Google Sheet column order."""
        return [
            str(self.lead_id),
            self.created_at.astimezone(WARSAW_TIME_ZONE).strftime(SHEET_DATETIME_FORMAT),
            self.full_name,
            self.phone,
            self.comment or "",
            self.language.value,
            self.source,
        ]


class LeadStorageError(RuntimeError):
    """Raised when a validated lead cannot be stored."""


class LeadStore(Protocol):
    """Storage contract used by the lead service."""

    async def append(self, lead: LeadRecord) -> None:
        """Persist one lead or raise LeadStorageError."""
        ...


class DisabledLeadStore:
    """Safe default used until external lead storage is configured."""

    async def append(self, lead: LeadRecord) -> None:
        del lead
        raise LeadStorageError("lead storage is disabled")


class LeadService:
    """Create server metadata and send valid leads to configured storage."""

    def __init__(self, store: LeadStore) -> None:
        self._store = store

    async def submit(self, submission: LeadCreate) -> None:
        if submission.company_website:
            return

        lead = LeadRecord(
            lead_id=uuid4(),
            created_at=datetime.now(UTC),
            full_name=submission.full_name,
            phone=submission.phone,
            comment=submission.comment,
            language=submission.language,
        )
        await self._store.append(lead)
