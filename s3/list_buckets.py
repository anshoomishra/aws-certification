"""Read-only S3 example: list buckets for the configured AWS identity."""

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
