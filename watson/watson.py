import os
import argparse
import time
import json
from doc_generator import generate_doc
from token_generator import generate_token

def get_parent_file_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir) 

def load_config():
    with open(os.path.join(get_parent_file_path(), "watson/config.json")) as config_file:
        return json.load(config_file)

config = load_config()

docs_path = os.path.join(get_parent_file_path(), "generated-docs")
# repo_path = config['GITHUB_REPO']
# git_branch = config['GITHUB_BRANCH']
# github_token = config['GITHUB_TOKEN']
# projects_params = config['PROJECTS_PARAMS']
file_extensions = config['FILE_EXTENSIONS']
model_id = config['MODEL_ID']
model_params = config['MODEL_PARAMS']

def list_files_in_local_repo(repo_path):
    try:
        files = []
        # Use os.walk to walk through the directory structure recursively
        for root, _, filenames in os.walk(repo_path):
            for filename in filenames:
                # Get the full path of each file
                full_path = os.path.join(root, filename)
                files.append(full_path)
        return files
    except Exception as e:
        print(f"Unable to retrieve directory contents: {e}")
        exit()

prompt = "input" """<|system|>
    generate a readme file in markdown format that documents the code below.
    the answer should contain exclusively the content of the markdown readme file, without any additional information.
    here is the code:
    """

def read_file_from_local_path(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Unable to read file {file_path}: {e}")
        exit()

def main():
    parser = argparse.ArgumentParser(description='Read files and list directory contents from a local repository.')
    parser.add_argument('repo_path', type=str, help='Path to the local repository')
    parser.add_argument('api_key', type=str, help='api key to interact with watson x')


    args = parser.parse_args()

    repo_path = args.repo_path
    api_key = args.api_key

    start_time = time.time()

    code_file_list = list_files_in_local_repo(repo_path)
    print("files found in repo:", code_file_list)
    
    


    code_files = prompt
    for file_key in code_file_list:
        if any(file_key.endswith(ext) for ext in file_extensions):
            file_content = read_file_from_local_path(file_key)
            if file_content:
                code_files +="\n" + file_key + "\n" + file_content + "\n <|assistant|>\n"
    print(code_files)


    project_id = "845ef238-5f5c-4155-b84b-9b4ab9759270"
    api_key = api_key
    endpoint_url = "https://eu-de.ml.cloud.ibm.com"
    print(f"Generating documentation using project {project_id}")
    result = generate_doc(project_id, api_key, code_files, model_id, endpoint_url, model_params)

    # Ensure the docs_path directory exists
    os.makedirs(docs_path, exist_ok=True)

    filenames = []
    for i, result in enumerate(results):
        md_file_name = f"{docs_path}/documentation_{i + 1}.md"
        filenames.append(md_file_name)
        with open(md_file_name, 'w') as file:
            # Save the generated text into the markdown file
            file.write(result.get('generated_text', ''))

    end_time = time.time()
    duration = end_time - start_time

    print(f"Execution duration: {duration} seconds")
    print("Generated files:", filenames)

if __name__ == "__main__":
    main()