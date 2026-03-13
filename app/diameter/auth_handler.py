"""Authentication logic for Diameter simulation."""

from __future__ import annotations

from app.core.config import get_settings


class AuthHandler:
    """Provides a deterministic auth result for demo subscribers."""

    def authenticate(self, subscriber_id: str) -> dict:
        settings = get_settings()
        accepted = bool(subscriber_id and subscriber_id.strip())
        return {
            "subscriber_id": subscriber_id,
            "realm": settings.default_realm,
            "status": "authorized" if accepted else "rejected",
            "result_code": 2001 if accepted else 4001,
        }
