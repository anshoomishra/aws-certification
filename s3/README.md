# S3 Python Lab

This folder contains the first AWS certification practical lab using Python and `boto3`. Shared configuration and utilities live in the repository-level [`shared/`](../shared/) package so every future practical can reuse them.

## Configure credentials safely

The preferred approach is an AWS CLI profile or IAM Identity Center profile:

```powershell
aws configure sso
aws sso login --profile default
```

From the repository root, copy the global configuration template and adjust the non-secret values:

```powershell
Copy-Item .env.example .env
```

`.env` is ignored by Git. Never add access keys or session tokens to Python files, notebooks, or committed configuration. boto3 uses the standard AWS credential provider chain, so you can also use role-based credentials in EC2, ECS or Lambda.

## Run the read-only starter

From the repository root:

```powershell
.\.venv\Scripts\Activate.ps1
python -m s3.list_buckets
```

The script only calls `ListBuckets`; it does not create, upload, modify or delete anything.

## Shared project structure

```text
aws-certification/
├── .env.example              # Global configuration template
├── requirements.txt          # Global Python dependencies
├── shared/
│   ├── config.py             # Settings loaded from the root .env
│   ├── aws.py                # AwsClientFactory and retry configuration
│   └── tags.py               # Standard ownership and cost tags
└── s3/                       # S3-specific practicals
```

Use `AwsClientFactory` in future labs:

```python
from shared import AwsClientFactory

s3 = AwsClientFactory().client("s3")
```

## Next S3 exercises

1. Create a uniquely named lab bucket with `us-east-1` handling where required.
2. Apply ownership tags and default encryption.
3. Upload and download an object with metadata and a checksum.
4. Generate a short-lived presigned URL.
5. Add versioning and a lifecycle policy.
6. Test access using a least-privilege IAM policy.
7. Write unit tests with `pytest` and `moto`.
8. Add a dry-run cleanup command that only removes resources with your lab ownership tag.

Always set a budget alert, use a dedicated lab account where possible, and delete billable resources after testing.
