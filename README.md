# watsonX-ai
This repo contains a basic script to programmatically interact with watsonx platform

# Repository Documentation Generator

This README provides instructions for uploading files from a local repository to IBM Watsonx AI and generating documentation using the uploaded files.

## Prerequisites

- IBM Watsonx AI Python SDK
- Python 3.6+
- IBM Watsonx AI credentials

## Installation

1. Install the IBM Watsonx AI Python SDK:
   ```bash
   pip install ibm-watsonx-ai

2. Install Python requirements
   ```bash
   pip install -r requirements.txt

## Authentication

1. To generate a valid token use this command (request tha api key from the boss :p)
   ```bash
   curl -X POST 'https://iam.cloud.ibm.com/identity/token' -H 'Content-Type: application/x-www-form-urlencoded' -d 'grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey=API_KEY'

