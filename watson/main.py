import time
import os
import warnings

from ibm_watsonx_ai import APIClient
from ibm_watson_machine_learning.foundation_models import Model
from token_generator import generate_token
from doc_collector import read_file_from_cos ,list_files_in_bucket

warnings.filterwarnings("ignore")

project_id = "fcad2fce-4610-4de3-babd-177600dbad19"

def get_parent_file_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir) 

docs_path = os.path.join(get_parent_file_path(), "generated-docs")

prompt = "input" """<|system|>
    generate a readme file in markdown format that documents the code below.
    the answer should contain exclusively the content of the markdown readme file, without any additional information.
    here is the code:
    """

# Constants for IBM COS values
cos_api_key = os.getenv('COS_API_KEY')
cos_service_instance_id = "crn:v1:bluemix:public:cloud-object-storage:global:a/5c6117ae971c4610a3952401b0bf5a77:a26b5106-54ab-4f56-a43d-dd593a29a7ed::"
cos_endpoint_url = "https://s3.eu-de.cloud-object-storage.appdomain.cloud"
cos_bucket_name = "cloud-object-storage-cos-terraform-code"

cos_file_list = list_files_in_bucket(cos_bucket_name, cos_api_key, cos_service_instance_id, cos_endpoint_url)

code_files = []
for cos_file_key in cos_file_list:
    file_content = read_file_from_cos(cos_bucket_name, cos_file_key, cos_api_key, cos_service_instance_id, cos_endpoint_url)
    if file_content:
        code_files.append(file_content)

def main():
    start_time = time.time()
    
    credentials = {
        "url": "https://eu-gb.ml.cloud.ibm.com",
        "token": generate_token()
    }

    client = APIClient(credentials)
    client.set.default_project(project_id)

    input_texts = set()
    for code_file in code_files:
        input_texts.add(f"{prompt}\n{code_file}\n <|assistant|>\n")

    # Model initialization
    generate_params = {
        "temperature": 0.3,
        "decoding_method": "greedy",
        "max_new_tokens": 900,
        "repetition_penalty": 1.05
    }

    model = Model(
        model_id="ibm/granite-13b-chat-v2",  # Replace with your model ID
        params=generate_params,
        credentials=credentials,
        project_id=project_id,
    )

    results = []
    for input_text in input_texts:
        response = model.generate(input_text)
        results.extend(response.get('results', []))

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