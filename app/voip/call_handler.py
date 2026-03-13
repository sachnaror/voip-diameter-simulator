"""High-level VoIP call orchestration."""

from __future__ import annotations

from app.core.session_manager import SessionManager
from app.voip.sip_client import SIPClient


class CallHandler:
    """Creates a simulated call session and SIP event timeline."""

    def __init__(self) -> None:
        self.session_manager = SessionManager()
        self.sip_client = SIPClient()

    def start_call(self, caller: str, callee: str) -> dict:
        session = self.session_manager.create_session("voip")
        timeline = self.sip_client.initiate_call(caller, callee)
        return {
            "status": "established",
            "session": session,
            "timeline": timeline,
        }
