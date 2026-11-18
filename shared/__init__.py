"""Shared utilities used by every AWS practical folder."""

from .aws import AwsClientFactory
from .config import Settings, get_settings

__all__ = ["AwsClientFactory", "Settings", "get_settings"]
