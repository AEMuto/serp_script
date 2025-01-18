# Google Search Results Script

A Python script that uses Google Custom Search API to fetch search results.

## Prerequisites

- Python 3.x
- Google Cloud Platform account
- Custom Search Engine ID
- API Key from Google Cloud Platform

## Setup

1. Clone the repository:
```sh
git clone https://github.com/AEMuto/serp_script
cd serp_script
```

2. Create a virtual environment:
```sh
python -m venv venv
source venv/bin/activate
```

3. Install required packages:
```sh
pip install google-api-python-client python-dotenv
```

4. Create a `.env` file in the root directory with your credentials:
```
API_KEY=your_google_api_key_here
SEARCH_ENGINE_ID=your_search_engine_id_here
```

## Usage

1. Activate the virtual environment:
```sh
source venv/bin/activate
```

2. Run the script:
```sh
python serp-script.py
```

3. Enter your search query when prompted.

The script will return up to 100 URLs from Google search results.

## Features

- Fetches up to 100 search results
- Handles pagination automatically
- Error handling for API requests
- Environment variable support for secure credential management

## Note

Make sure to keep your `.env` file secure and never commit it to version control.