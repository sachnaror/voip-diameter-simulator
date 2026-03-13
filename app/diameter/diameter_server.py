"""Diameter request orchestration for the simulator."""

from __future__ import annotations

from app.core.config import get_settings
from app.core.session_manager import SessionManager
from app.diameter.auth_handler import AuthHandler
from app.diameter.avp_parser import parse_avps


class DiameterServer:
    """Builds a simulated Diameter response payload."""

    def __init__(self) -> None:
        self.auth_handler = AuthHandler()
        self.session_manager = SessionManager()

    def handle_request(self, subscriber_id: str, command_code: int, avps: dict[str, str]) -> dict:
        settings = get_settings()
        session = self.session_manager.create_session("diameter")
        auth_result = self.auth_handler.authenticate(subscriber_id)
        return {
            "status": "processed",
            "command_code": command_code,
            "origin_host": settings.default_origin_host,
            "origin_realm": settings.default_origin_realm,
            "session": session,
            "auth": auth_result,
            "avps": parse_avps(avps),
        }
