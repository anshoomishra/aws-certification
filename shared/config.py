"""Global, environment-driven configuration for AWS practicals."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(REPOSITORY_ROOT / ".env")


@dataclass(frozen=True)
class Settings:
    """Immutable application settings shared by all practical folders."""

    aws_region: str
    aws_profile: str | None
    lab_project: str
    lab_owner: str
    lab_environment: str
    s3_bucket_prefix: str

    @classmethod
    def from_environment(cls) -> "Settings":
        """Build settings from environment variables and the root .env file."""

        return cls(
            aws_region=os.getenv("AWS_REGION", "ap-south-1"),
            aws_profile=os.getenv("AWS_PROFILE") or None,
            lab_project=os.getenv("AWS_LAB_PROJECT", "aws-certification"),
            lab_owner=os.getenv("AWS_LAB_OWNER", "learning"),
            lab_environment=os.getenv("AWS_LAB_ENVIRONMENT", "learning"),
            s3_bucket_prefix=os.getenv(
                "S3_BUCKET_PREFIX", "aws-certification-s3-lab"
            ),
        )


def get_settings() -> Settings:
    """Return the current global configuration."""

    return Settings.from_environment()
