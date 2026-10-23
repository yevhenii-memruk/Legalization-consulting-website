"""Public consultation request endpoint."""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request, status

from legalization_consulting.schemas.leads import LeadAccepted, LeadCreate
from legalization_consulting.services.leads import LeadService, LeadStorageError
from legalization_consulting.services.rate_limit import LeadRateLimiter

router = APIRouter(prefix="/api/leads", tags=["leads"])


def get_lead_service(request: Request) -> LeadService:
    """Build the use case from the application-configured storage adapter."""
    return LeadService(request.app.state.lead_store)


def get_rate_limiter(request: Request) -> LeadRateLimiter:
    """Return the limiter owned by this application instance."""
    return request.app.state.lead_rate_limiter


@router.post("", response_model=LeadAccepted, status_code=status.HTTP_201_CREATED)
async def create_lead(
    submission: LeadCreate,
    request: Request,
    service: Annotated[LeadService, Depends(get_lead_service)],
    rate_limiter: Annotated[LeadRateLimiter, Depends(get_rate_limiter)],
) -> LeadAccepted:
    """Validate and persist one consultation request."""
    client_address = request.client.host if request.client else "unknown"
    if not await rate_limiter.allow(client_address):
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many consultation requests",
            headers={"Retry-After": str(rate_limiter.window_seconds)},
        )

    try:
        await service.submit(submission)
    except LeadStorageError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Consultation requests are temporarily unavailable",
        ) from exc

    return LeadAccepted()
