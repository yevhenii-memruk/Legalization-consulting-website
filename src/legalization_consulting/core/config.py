from functools import lru_cache

from pydantic import AnyHttpUrl, Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    name: str = "Non-Stop Documents"
    description: str = "Legalization consulting website"
    version: str = "0.1.0"
    debug: bool = False
    contact_email: str = "documentnonstop@gmail.com"
    public_base_url: AnyHttpUrl | None = None
    leads_enabled: bool = False
    google_sheets_spreadsheet_id: str | None = None
    google_sheets_range: str = "Leads!A:G"
    lead_rate_limit: int = Field(default=5, gt=0)
    lead_rate_window_seconds: int = Field(default=600, gt=0)

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="APP_",
        extra="ignore",
    )

    @model_validator(mode="after")
    def validate_lead_storage(self) -> Settings:
        """Require a destination before real lead collection is enabled."""
        if self.leads_enabled and not self.google_sheets_spreadsheet_id:
            raise ValueError("APP_GOOGLE_SHEETS_SPREADSHEET_ID is required when leads are enabled")
        return self


@lru_cache
def get_settings() -> Settings:
    """Return one validated settings instance per process."""
    return Settings()
