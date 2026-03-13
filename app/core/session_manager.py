"""Simple in-memory session generation helpers for simulator flows."""

from __future__ import annotations

from datetime import UTC, datetime
from uuid import uuid4


class SessionManager:
    """Generates lightweight session descriptors for demo flows."""

    def create_session(self, session_type: str) -> dict:
        created_at = datetime.now(UTC).isoformat()
        return {
            "session_id": f"{session_type}-{uuid4()}",
            "session_type": session_type,
            "created_at": created_at,
            "state": "created",
        }
