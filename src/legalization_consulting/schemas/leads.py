"""Validation models for consultation requests."""

import re
from enum import StrEnum
from typing import Annotated, Literal

import phonenumbers
from phonenumbers import NumberParseException, PhoneNumberFormat
from pydantic import BaseModel, ConfigDict, Field, field_validator

PHONE_CHARACTERS = re.compile(r"^\+?[0-9\s().-]+$")


class LeadLanguage(StrEnum):
    """Languages supported by the lead-processing API."""

    PL = "pl"
    UK = "uk"
    RU = "ru"
    EN = "en"


class LeadCreate(BaseModel):
    """User-provided consultation request."""

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    full_name: Annotated[str, Field(min_length=2, max_length=120)]
    phone: Annotated[str, Field(min_length=7, max_length=32)]
    comment: Annotated[str | None, Field(max_length=1000)] = None
    language: LeadLanguage = LeadLanguage.PL
    company_website: Annotated[str, Field(max_length=200)] = ""

    @field_validator("full_name")
    @classmethod
    def normalize_full_name(cls, value: str) -> str:
        """Collapse repeated whitespace before storing a name."""
        return " ".join(value.split())

    @field_validator("phone")
    @classmethod
    def normalize_phone(cls, value: str) -> str:
        """Validate a phone number and store it in international E.164 format."""
        if not PHONE_CHARACTERS.fullmatch(value):
            raise ValueError("phone contains unsupported characters")

        digits = re.sub(r"\D", "", value)
        if value.startswith("+"):
            parseable = f"+{digits}"
        elif digits.startswith("00"):
            parseable = f"+{digits[2:]}"
        elif len(digits) == 11 and digits.startswith("48"):
            parseable = f"+{digits}"
        else:
            parseable = digits

        try:
            number = phonenumbers.parse(parseable, "PL")
        except NumberParseException as exc:
            raise ValueError("phone is not a valid telephone number") from exc

        if not phonenumbers.is_valid_number(number):
            raise ValueError("phone is not a valid telephone number")

        return phonenumbers.format_number(number, PhoneNumberFormat.E164)

    @field_validator("comment", mode="before")
    @classmethod
    def empty_comment_to_none(cls, value: object) -> object:
        """Treat an empty optional comment as missing."""
        if isinstance(value, str) and not value.strip():
            return None
        return value


class LeadAccepted(BaseModel):
    """Public response returned after accepting a consultation request."""

    status: Literal["accepted"] = "accepted"
