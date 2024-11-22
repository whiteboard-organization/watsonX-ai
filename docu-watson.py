from ibm_watsonx_ai import APIClient
from ibm_watson_machine_learning.foundation_models import Model

from ibm_watsonx_ai.helpers import DataConnection
import json
import os


credentials = {
     "url": "https://eu-gb.ml.cloud.ibm.com",
    "token": "eyJraWQiOiIyMDI0MTEwMTA4NDIiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJJQk1pZC02OTcwMDBMSlFEIiwiaWQiOiJJQk1pZC02OTcwMDBMSlFEIiwicmVhbG1pZCI6IklCTWlkIiwianRpIjoiOGEwYmY3ZTQtNTRkMS00Mjg0LTg0N2YtYTU3Mzc3ZTE0MzFkIiwiaWRlbnRpZmllciI6IjY5NzAwMExKUUQiLCJnaXZlbl9uYW1lIjoiQWhtZWQiLCJmYW1pbHlfbmFtZSI6Ik16b3VnaGkiLCJuYW1lIjoiQWhtZWQgTXpvdWdoaSIsImVtYWlsIjoiQWhtZWQuTXpvdWdoaUBpYm0uY29tIiwic3ViIjoiQWhtZWQuTXpvdWdoaUBpYm0uY29tIiwiYXV0aG4iOnsic3ViIjoiQWhtZWQuTXpvdWdoaUBpYm0uY29tIiwiaWFtX2lkIjoiSUJNaWQtNjk3MDAwTEpRRCIsIm5hbWUiOiJBaG1lZCBNem91Z2hpIiwiZ2l2ZW5fbmFtZSI6IkFobWVkIiwiZmFtaWx5X25hbWUiOiJNem91Z2hpIiwiZW1haWwiOiJBaG1lZC5Nem91Z2hpQGlibS5jb20ifSwiYWNjb3VudCI6eyJ2YWxpZCI6dHJ1ZSwiYnNzIjoiNWJlYzNhZGMxZTJjNGFiMjk1OWUzZmUyMmQwZGEzNjUiLCJmcm96ZW4iOnRydWV9LCJpYXQiOjE3MzIyNzIxNzYsImV4cCI6MTczMjI3NTc3NiwiaXNzIjoiaHR0cHM6Ly9pYW0uY2xvdWQuaWJtLmNvbS9pZGVudGl0eSIsImdyYW50X3R5cGUiOiJ1cm46aWJtOnBhcmFtczpvYXV0aDpncmFudC10eXBlOmFwaWtleSIsInNjb3BlIjoiaWJtIG9wZW5pZCIsImNsaWVudF9pZCI6ImRlZmF1bHQiLCJhY3IiOjEsImFtciI6WyJwd2QiXX0.LmnwjFZrxufjLd4DDSKUdT1rZI-eyqPugvhIZV_EzpD-RMiUftrBPHBgxuy9R641SUsdH7EpwfYCSR_qWQ7tZBHuddfcbAqysDN2tZFQvXHQV8kxqRfUGCAr5wG3XGbXEpFAkF6S2-9hr6rZg_Tpz3M6Pv-I4PEY4XrGN5qHVgcOP_bTDi_mkQ7JuNOWqm483btlDLVg72-RX9p-wtLINJjwyLgW5-tj_kb2P7UIHgyWS-CpxZM63YU4bP66sVE-Lqsf8cXvqEDAN3wLX4xpOWwBCMLRPHoXlqEtb1R6G7t-jCwzoDktfXtI347Xtps8AtLpWmlmOGWYTFuZ90FyrA"
    }

client = APIClient(credentials)
project_id = "fcad2fce-4610-4de3-babd-177600dbad19"
space_id = "50e01d73-e886-46af-a1b8-0c668e39187b"
client.set.default_project(project_id)

#we need to create a function that extract text from multiple files and get in one string so we can pass it as an input to the model.

input_text = "input" """<|system|>
can you generate a readme file based on this
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
    project_id="fcad2fce-4610-4de3-babd-177600dbad19",  # Replace with your project ID

)

response = model.generate(input_text)

print(response)

