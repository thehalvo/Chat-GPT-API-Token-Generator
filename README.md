# Chat GPT API Token Generator
A Python script to automatically generate short stories based on a preset prompt using OpenAI's GPT-3.5 API. It's primary purpose is to use up tokens
over an hour, so that your OpenAI account is billed at least $1, thereby giving
you access to GPT-4 the following month.

## Table of Contents
1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Contribution](#contribution)
5. [Disclaimer](#disclaimer)

## Requirements

- Python 3.x
- OpenAI Python package
- An OpenAI API key

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/thehalvo/Chat-GPT-API-Token-Generator.git
    ```

2. Navigate into the project directory and install required packages:

    ```bash
    cd Chat-GPT-API-Token-Generator
    ```

## Usage

1. Set your OpenAI API key as an environment variable:

    ```bash
    export OPENAI_API_KEY="your-api-key-here"
    ```

2. Run the script:

    ```bash
    python generator.py
    ```

This will generate random stories every 5 seconds. Please be aware that this might quickly use up your API quota, so use it judiciously. I recommend setting
your API limit to $2 in your OpenAI settings before using this script.

## Contribution

Feel free to fork the project, open a pull request, or submit suggestions and bugs as issues.

## Disclaimer

This project is not affiliated, associated, authorized, endorsed by, or in any way officially connected with OpenAI. Be aware of the OpenAI API rate limits and the API usage cost when running the script.
