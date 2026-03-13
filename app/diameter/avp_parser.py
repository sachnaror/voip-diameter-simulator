"""Minimal AVP parsing utilities for demo Diameter payloads."""

from __future__ import annotations


def parse_avps(avps: dict[str, str]) -> list[dict]:
    """Convert a raw AVP mapping into a normalized list."""
    return [{"name": name, "value": value} for name, value in avps.items()]
