import time
from ibm_watsonx_ai import APIClient
from ibm_watson_machine_learning.foundation_models import Model

from ibm_watsonx_ai.helpers import DataConnection
from token_generator import generate_token
import warnings

warnings.filterwarnings("ignore")

project_id = "fcad2fce-4610-4de3-babd-177600dbad19"

def main():
    start_time = time.time()
    
    credentials = {
        "url": "https://eu-gb.ml.cloud.ibm.com",
        "token": generate_token()
    }

    client = APIClient(credentials)
    client.set.default_project(project_id)

    input_text = "input" """<|system|>
    generate a readme file in markdown format that documents the code below.
    the answer should contain exclusively the content of the markdown readme file, without any additional information.
    here is the code:

    "provider "aws" {
      region = "us-east-1"
    }

    resource "aws_s3_bucket" "test_bucket" {
      bucket = "my-unique-bucket-name-123456"

      tags = {
        Name        = "TestBucket"
        Environment = "Dev"
      }
    }
    "
    <|assistant|>
    """

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

    response = model.generate(input_text)
    results = response.get('results', [])

    filenames = []
    for i, result in enumerate(results):
        md_file_name = f"documentation_{i + 1}.md"
        filenames.append(md_file_name)
        with open(md_file_name, 'w') as file:
            # Save the generated_text field of the result into the markdown file
            file.write(result.get('generated_text', ''))

    end_time = time.time()
    duration = end_time - start_time

    print(f"Execution duration: {duration} seconds")
    print("Generated files:", filenames)

if __name__ == '__main__':
    main()