# WatsonX AI Documentation Generator

This project generates documentation for code files in a local repository using IBM WatsonX AI.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Project Structure](#project-structure)
- [Configuration](#configuration)

## Introduction

WatsonX AI is a project aimed at utilizing IBM Watson's capabilities to develop innovative AI applications. This project includes various tools and libraries to help developers build, train, and deploy AI models efficiently.

## Features

- Natural Language Processing (NLP)
- Machine Learning (ML)
- Integration with IBM Cloud

## Installation

To install the WatsonX AI project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/watsonX-ai.git
    ```
2. Navigate to the project directory:
    ```bash
    cd watsonX-ai
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Project Structure

- `token_generator.py`: Generates an access token using an API key.
- `main.py`: Main script to orchestrate the documentation generation process.
- `doc_generator.py`: Generates documentation using IBM WatsonX AI.
- `doc_collector.py`: Collects code files from a GitHub repository or IBM Cloud Object Storage.

## Configuration

The project requires a configuration file `config.json` located in the `watson` directory. The configuration file should contain the following parameters:

```json
{
    "GITHUB_REPO": "your_github_repo",
    "GITHUB_BRANCH": "your_github_branch",
    "GITHUB_TOKEN": "your_github_token",
    "PROJECTS_PARAMS": [
        {
            "PROJECT_ID": "your_project_id",
            "API_Key": "your_api_key",
            "MODEL_ENDPOINT_URL": "your_model_endpoint_url"
        }
    ],
    "FILE_EXTENSIONS": [".py", ".java", ".js"],
    "MODEL_ID": "your_model_id",
    "MODEL_PARAMS": {
        "param1": "value1",
        "param2": "value2"
    }
}
```