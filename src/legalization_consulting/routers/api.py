from typing import Literal, TypedDict

from fastapi import APIRouter


class HealthResponse(TypedDict):
    status: Literal["ok"]


router = APIRouter(tags=["system"])


@router.get("/health")
async def health() -> HealthResponse:
    return {"status": "ok"}
