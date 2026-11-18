"""Reusable object-oriented boto3 session and client factory."""

from __future__ import annotations

from typing import Any

import boto3
from botocore.config import Config

from .config import Settings, get_settings


class AwsClientFactory:
    """Create consistently configured boto3 clients and resources."""

    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or get_settings()
        self.session = boto3.Session(
            profile_name=self.settings.aws_profile,
            region_name=self.settings.aws_region,
        )
        self.client_config = Config(
            retries={"mode": "standard", "max_attempts": 5},
            user_agent_extra="aws-certification-practicals/1.0",
        )

    def client(self, service_name: str) -> Any:
        """Return a retry-configured low-level boto3 client."""

        return self.session.client(
            service_name,
            region_name=self.settings.aws_region,
            config=self.client_config,
        )

    def resource(self, service_name: str) -> Any:
        """Return a boto3 resource using the global Region and credentials."""

        return self.session.resource(
            service_name,
            region_name=self.settings.aws_region,
            config=self.client_config,
        )
