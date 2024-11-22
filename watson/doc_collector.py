import ibm_boto3
from ibm_botocore.client import Config

def read_file_from_cos(bucket_name, file_key, api_key, service_instance_id, endpoint_url):
    cos = ibm_boto3.client('s3',
                           ibm_api_key_id=api_key,
                           ibm_service_instance_id=service_instance_id,
                           config=Config(signature_version='oauth'),
                           endpoint_url=endpoint_url)
    try:
        file = cos.get_object(Bucket=bucket_name, Key=file_key)
        return file['Body'].read().decode('utf-8')
    except Exception as e:
        print(f"Unable to read file from COS: {e}")
        return None
