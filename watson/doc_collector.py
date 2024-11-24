import ibm_boto3
import os
from ibm_botocore.client import Config, ClientError

def read_file_from_cos(bucket_name, file_key, api_key, service_instance_id, endpoint_url):
    cos_client = ibm_boto3.client("s3",
        ibm_api_key_id=api_key,
        ibm_service_instance_id=service_instance_id,
        config=Config(signature_version="oauth"),
        endpoint_url=endpoint_url
    )

    try:
        file = cos_client.get_object(Bucket=bucket_name, Key=file_key)
        return format(file["Body"].read())
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
        exit()
    except Exception as e:
        print("Unable to retrieve file contents: {0}".format(e))
        exit()

def list_files_in_bucket(bucket_name, api_key, service_instance_id, endpoint_url):
    cos_client = ibm_boto3.client("s3",
        ibm_api_key_id=api_key,
        ibm_service_instance_id=service_instance_id,
        config=Config(signature_version="oauth"),
        endpoint_url=endpoint_url
    )
    print("Retrieving bucket contents from: {0}".format(bucket_name))
    try:
        files = cos_client.list_objects(Bucket=bucket_name)
        file_list = []
        for file in files.get("Contents", []):
            file_list.append(file["Key"])
        return file_list
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
        exit()
    except Exception as e:
        print("Unable to retrieve bucket contents: {0}".format(e))
        exit()

#defined two functions
def read_file_from_local_repo(repo_path, file_path):
    full_path = os.path.join(repo_path, file_path)
    try:
        with open(full_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {full_path}")
        exit()
    except Exception as e:
        print(f"Unable to retrieve file contents: {e}")
        exit()

def list_files_in_local_repo(repo_path):
    try:
        files = []
        for root, dirs, filenames in os.walk(repo_path):
            for filename in filenames:
                files.append(os.path.relpath(os.path.join(root, filename), repo_path))
        return files
    except Exception as e:
        print(f"Unable to retrieve directory contents: {e}")
        exit()
