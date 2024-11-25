import warnings

from ibm_watsonx_ai import APIClient
from ibm_watson_machine_learning.foundation_models import Model
from token_generator import generate_token

warnings.filterwarnings("ignore")

def generate_doc(project_id, api_key, input_text, model_id, model_endpoint_url, model_params):
    try:
        credentials = {
            "url": model_endpoint_url,
            "token": generate_token(api_key)
        }

        client = APIClient(credentials)
        client.set.default_project(project_id)

        model = Model(
            model_id=model_id,
            params=model_params,
            credentials=credentials,
            project_id=project_id,
        )

        response = model.generate(input_text)
        return response.get('results', [])

    except Exception as e:
        print(f"An error occurred during document generation: {e}")
        exit()
