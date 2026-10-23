"""Small in-process rate limiter for the public lead endpoint."""

import hashlib
import secrets
import time
from asyncio import Lock
from collections import deque


class LeadRateLimiter:
    """Limit requests per client without retaining raw client addresses."""

    def __init__(self, limit: int, window_seconds: int) -> None:
        self._limit = limit
        self._window_seconds = window_seconds
        self._requests: dict[str, deque[float]] = {}
        self._salt = secrets.token_bytes(16)
        self._lock = Lock()
        self._last_cleanup = time.monotonic()

    @property
    def window_seconds(self) -> int:
        """Expose the configured window for the HTTP Retry-After header."""
        return self._window_seconds

    async def allow(self, client_address: str) -> bool:
        """Return whether another request is allowed in the current window."""
        now = time.monotonic()
        cutoff = now - self._window_seconds
        client_key = self._client_key(client_address)

        async with self._lock:
            if now - self._last_cleanup >= self._window_seconds:
                self._cleanup(cutoff)
                self._last_cleanup = now

            requests = self._requests.setdefault(client_key, deque())
            while requests and requests[0] <= cutoff:
                requests.popleft()

            if len(requests) >= self._limit:
                return False

            requests.append(now)
            return True

    def _client_key(self, client_address: str) -> str:
        return hashlib.blake2s(
            client_address.encode("utf-8"),
            key=self._salt,
        ).hexdigest()

    def _cleanup(self, cutoff: float) -> None:
        expired_keys: list[str] = []
        for client_key, requests in self._requests.items():
            while requests and requests[0] <= cutoff:
                requests.popleft()
            if not requests:
                expired_keys.append(client_key)

        for client_key in expired_keys:
            del self._requests[client_key]
