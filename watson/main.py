import time
import os
import json
from itertools import cycle

from doc_collector import list_files_in_git_repo, read_file_from_git_repo
from doc_generator import generate_doc

def get_parent_file_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir) 

def load_config():
    with open(os.path.join(get_parent_file_path(), "watson/config.json")) as config_file:
        return json.load(config_file)

config = load_config()

docs_path = os.path.join(get_parent_file_path(), "generated-docs")
repo_path = config['GITHUB_REPO']
git_branch = config['GITHUB_BRANCH']
github_token = config['GITHUB_TOKEN']
projects_params = config['PROJECTS_PARAMS']
file_extensions = config['FILE_EXTENSIONS']
model_id = config['MODEL_ID']
model_params = config['MODEL_PARAMS']

print(github_token)
projects_dict = {project['PROJECT_ID']: {'API_Key': project['API_Key'], 'Endpoint_URL': project['MODEL_ENDPOINT_URL']} for project in projects_params}

prompt = "input" """<|system|>
    generate a readme file in markdown format that documents the code below.
    the answer should contain exclusively the content of the markdown readme file, without any additional information.
    here is the code:
    """

def main():
    start_time = time.time()

    code_file_list = list_files_in_git_repo(repo_path, git_branch, github_token)
    print("files found in repo:", code_file_list)

    code_files = []
    for file_key in code_file_list:
        if any(file_key.endswith(ext) for ext in file_extensions):
            file_content = read_file_from_git_repo(repo_path, file_key, git_branch, github_token)
            if file_content:
                code_files.append(f"{prompt}\n{file_content}\n <|assistant|>\n")

    project_cycle = cycle(projects_dict.items())
    
    results = []
    for input_text in code_files:
        project_id, project_info = next(project_cycle)
        api_key = project_info['API_Key']
        endpoint_url = project_info['Endpoint_URL']
        print(f"Generating documentation using project {project_id}")
        result = generate_doc(project_id, api_key, input_text, model_id, endpoint_url, model_params)
        results.extend(result)

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

if __name__ == '__main__':
    main()