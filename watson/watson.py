import os
import argparse
import time
import json
from doc_generator import generate_doc

def get_parent_file_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir) 

def load_config():
    with open(os.path.join(get_parent_file_path(), "watson/config.json")) as config_file:
        return json.load(config_file)

config = load_config()

docs_path = os.path.join(get_parent_file_path(), "docs")
file_extensions = config['FILE_EXTENSIONS']
model_id = config['MODEL_ID']
model_params = config['MODEL_PARAMS']
# Adjust projects_params to handle the given config structure
projects_params = {
    config['PROJECTS_PARAMS']['PROJECT_ID']: config['PROJECTS_PARAMS']['MODEL_ENDPOINT_URL']
}

prompt = "input" """<|system|>
    generate a readme file in markdown format that documents the code below.
    your response should contain exclusively the content of the markdown readme file. so it should start with the title, followed by the description, and then the code documentation.
    here is the code:
    """

def list_files_in_local_repo(repo_path):
    try:
        files = []
        for root, _, filenames in os.walk(repo_path):
            for filename in filenames:
                full_path = os.path.join(root, filename)
                files.append(full_path)
        return files
    except Exception as e:
        print(f"Unable to retrieve directory contents: {e}")
        exit()



def read_file_from_local_path(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Unable to read file {file_path}: {e}")
        exit()

def main():
    start_time = time.time()

    parser = argparse.ArgumentParser(description='Read files and list directory contents from a local repository.')
    parser.add_argument('repo_path', type=str, help='Path to the local repository')
    parser.add_argument('api_key', type=str, help='api key to interact with watson x')

    args = parser.parse_args()
    repo_path = args.repo_path
    api_key = args.api_key
    
    code_file_list = list_files_in_local_repo(repo_path)
    print("files found in repo:", code_file_list)
    
    code_files = prompt
    for file_key in code_file_list:
        if any(file_key.endswith(ext) for ext in file_extensions):
            file_content = read_file_from_local_path(file_key)
            if file_content:
                code_files +="\n" + file_key + "\n" + file_content 
    code_files += "\n <|assistant|>\n"
    
    print(code_files)

    project_id, endpoint_url = next(iter(projects_params.items()))
    print(f"Generating documentation using project {project_id}")
    result = generate_doc(project_id, api_key, code_files, model_id, endpoint_url, model_params)
    # Extract generated_text from result and remove the last line
    md_text = [res.get('generated_text', '').replace('---<|endoftext|>', '').rstrip('\n') for res in result]

    # Ensure the docs_path directory exists
    os.makedirs(docs_path, exist_ok=True)

    md_file_name = f"{docs_path}/documentation.md"
    with open(md_file_name, 'w') as file:
        # Save the generated text as a markdown file
        file.write('\n'.join(md_text))

    end_time = time.time()
    duration = end_time - start_time

    print(f"Execution duration: {duration} seconds")
    print("Generated file:", md_file_name)

if __name__ == "__main__":
    main()
