"""HTTP routes for the VoIP Diameter simulator."""

from __future__ import annotations

from datetime import UTC, datetime

from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.core.config import get_settings
from app.diameter.diameter_server import DiameterServer
from app.voip.call_handler import CallHandler


router = APIRouter()


class CallSimulationRequest(BaseModel):
    caller: str = Field(..., description="Originating phone number or subscriber ID")
    callee: str = Field(..., description="Destination phone number or subscriber ID")


class DiameterSimulationRequest(BaseModel):
    subscriber_id: str = Field(..., description="Subscriber identity used for auth")
    command_code: int = Field(default=265, description="Diameter command code")
    avps: dict[str, str] = Field(default_factory=dict, description="Diameter AVP name/value pairs")


@router.get("/", tags=["meta"])
def get_index() -> dict:
    settings = get_settings()
    return {
        "name": settings.app_name,
        "version": settings.app_version,
        "environment": settings.app_env,
        "description": (
            "A lightweight telecom simulator for SIP call flow and Diameter-based "
            "authentication."
        ),
        "docs": "/docs",
        "timestamp": datetime.now(UTC).isoformat(),
    }


@router.get("/health", tags=["meta"])
def healthcheck() -> dict:
    settings = get_settings()
    return {
        "status": "ok",
        "service": settings.app_name,
        "environment": settings.app_env,
    }


@router.get("/config", tags=["meta"])
def get_config() -> dict:
    settings = get_settings()
    return {
        "api_prefix": settings.api_prefix,
        "default_realm": settings.default_realm,
        "origin_host": settings.default_origin_host,
        "origin_realm": settings.default_origin_realm,
    }


@router.post("/simulate/call", tags=["simulation"])
def simulate_call(payload: CallSimulationRequest) -> dict:
    handler = CallHandler()
    result = handler.start_call(payload.caller, payload.callee)
    return {
        "message": "Simulated SIP call flow generated successfully.",
        **result,
    }


@router.post("/simulate/diameter", tags=["simulation"])
def simulate_diameter(payload: DiameterSimulationRequest) -> dict:
    server = DiameterServer()
    result = server.handle_request(
        subscriber_id=payload.subscriber_id,
        command_code=payload.command_code,
        avps=payload.avps,
    )
    return {
        "message": "Simulated Diameter transaction processed successfully.",
        **result,
    }
