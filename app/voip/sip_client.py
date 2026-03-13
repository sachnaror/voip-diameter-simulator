"""SIP client primitives for the simulator."""

from __future__ import annotations


class SIPClient:
    """Builds a simple call-flow timeline for a simulated SIP session."""

    def initiate_call(self, caller: str, callee: str) -> list[dict]:
        return [
            {"step": "INVITE", "source": caller, "destination": callee, "status": "sent"},
            {"step": "100 Trying", "source": "network", "destination": caller, "status": "received"},
            {"step": "180 Ringing", "source": callee, "destination": caller, "status": "received"},
            {"step": "200 OK", "source": callee, "destination": caller, "status": "received"},
            {"step": "ACK", "source": caller, "destination": callee, "status": "sent"},
        ]
