import ibm_boto3
import os
import requests
from ibm_botocore.client import Config, ClientError
import base64

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

def read_file_from_git_repo(repo_url, file_path, branch='develop', token=None):
    api_url = f"https://api.github.com/repos/{repo_url}/contents/{file_path}?ref={branch}"
    headers = {'Authorization': f'token {token}'} if token else {}
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        file_content = response.json().get('content', '')
        return base64.b64decode(file_content).decode('utf-8')
    except requests.exceptions.RequestException as e:
        print(f"Unable to retrieve file contents: {e}")
        exit()

def list_files_in_git_repo(repo_url, branch='develop', token=None):
    api_url = f"https://api.github.com/repos/{repo_url}/git/trees/{branch}?recursive=1"
    headers = {'Authorization': f'token {token}'} if token else {}
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        tree = response.json().get('tree', [])
        files = [item['path'] for item in tree if item['type'] == 'blob']
        return files
    except requests.exceptions.RequestException as e:
        print(f"Unable to retrieve repository contents: {e}")
        exit()
