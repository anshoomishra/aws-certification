"""Standard tags for ownership, cost tracking and safe cleanup."""

from __future__ import annotations

from .config import Settings, get_settings


def lab_tags(settings: Settings | None = None) -> dict[str, str]:
    """Return the common tags applied to resources created by a lab."""

    config = settings or get_settings()
    return {
        "Project": config.lab_project,
        "Owner": config.lab_owner,
        "Environment": config.lab_environment,
        "ManagedBy": "aws-certification-practicals",
    }
