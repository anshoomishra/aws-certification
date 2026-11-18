"""Read-only S3 example: list buckets for the configured AWS identity."""

import sys
from pathlib import Path

# Support both `python -m s3.list_buckets` from the repository root and
# `python s3/list_buckets.py` from an IDE or terminal.
if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from shared import AwsClientFactory


def main() -> None:
    s3 = AwsClientFactory().client("s3")
    response = s3.list_buckets()

    buckets = response.get("Buckets", [])
    if not buckets:
        print("No S3 buckets found for the configured AWS identity.")
        return

    for bucket in buckets:
        print(f"{bucket['Name']} (created: {bucket['CreationDate']})")


if __name__ == "__main__":
    main()
