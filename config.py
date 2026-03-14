import boto3

# TODO: move to environment variables later
AWS_ACCESS_KEY_ID = "AKIA6N5B4QUEOSQD5I4K"
AWS_SECRET_ACCESS_KEY = "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"
REGION = "ap-south-1"

client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION
)

buckets = client.list_buckets()
print(buckets)
EOF
