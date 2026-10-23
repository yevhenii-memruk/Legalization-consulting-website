"""Google Sheets adapter for consultation requests."""

from asyncio import Lock

import google.auth
from anyio import to_thread
from googleapiclient.discovery import build

from legalization_consulting.services.leads import LeadRecord, LeadStorageError

SHEETS_SCOPE = "https://www.googleapis.com/auth/spreadsheets"


class GoogleSheetsLeadStore:
    """Append leads to a private Google Sheet using ADC credentials."""

    def __init__(self, spreadsheet_id: str, sheet_range: str) -> None:
        self._spreadsheet_id = spreadsheet_id
        self._sheet_range = sheet_range
        self._credentials, _ = google.auth.default(scopes=[SHEETS_SCOPE])
        self._lock = Lock()

    async def append(self, lead: LeadRecord) -> None:
        """Append one row without parsing user values as spreadsheet formulas."""
        async with self._lock:
            try:
                await to_thread.run_sync(self._append_sync, lead)
            except Exception as exc:
                raise LeadStorageError("Google Sheets append failed") from exc

    def _append_sync(self, lead: LeadRecord) -> None:
        sheets = build(
            "sheets",
            "v4",
            credentials=self._credentials,
            cache_discovery=False,
        )
        (
            sheets.spreadsheets()
            .values()
            .append(
                spreadsheetId=self._spreadsheet_id,
                range=self._sheet_range,
                valueInputOption="RAW",
                insertDataOption="INSERT_ROWS",
                body={"majorDimension": "ROWS", "values": [lead.as_sheet_row()]},
            )
            .execute(num_retries=0)
        )
