# Documentation for the `aws_s3_bucket` resource in Terraform

## Overview

The `aws_s3_bucket` resource in Terraform is used to create an S3 bucket in AWS with specified configuration options. This resource allows you to manage various aspects of your S3 bucket, such as bucket name, region, tags, and encryption settings.

## Configuration

The primary configuration for the `aws_s3_bucket` resource includes:

1. **bucket:** The name of the S3 bucket to be created.
2. **region:** The region where the S3 bucket will be created.
3. **tags:** A map of key-value pairs to apply to the S3 bucket.

Additional configuration options include:

- **acl:** The access control list (ACL) for the S3 bucket. Defaults to `public-read`.
- **encryption\_type:** The encryption type for the S3 bucket. Defaults to `none`.
- **server\_side\_encryption\_configuration:** Specify server-side encryption configuration for the S3 bucket.
- **lifecycle\_rule:** Define lifecycle rules for the S3 bucket.

## Example Usage

Here's an example of how to use the `aws_s3_bucket` resource to create an S3 bucket named `my-unique-bucket-name-123456` in the `us-east-1` region with the tag `Name` set to `TestBucket` and `Environment` set to `Dev`:

```hcl
resource "aws_s3_bucket" "test_bucket" {
  bucket = "my-unique-bucket-name-123456"

  tags = {
    Name        = "TestBucket"
    Environment = "Dev"
  }
}
```

## Benefits

Using the `aws_s3_bucket` resource in Terraform offers several benefits, including:

- **Consistency:** Ensure consistent S3 bucket configurations across your infrastructure.
- **Versioning:** Enable versioning for your S3 buckets to preserve, retrieve, and restore deleted or older versions of objects.
- **Lifecycle Policies:** Automate the management of object deletion and archival with lifecycle policies.
- **Encryption:** Secure your data at rest and in transit with encryption options.

## Related Resources

For more information on the `aws_s3_bucket` resource, refer to the [official Terraform documentation](https://registry.terraform.io/modules/aws/s3_bucket/aws/latest).

---<|endoftext|>