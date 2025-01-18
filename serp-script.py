from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()

# Import the API key and search engine ID from.env
api_key = os.getenv("API_KEY")
search_engine_id = os.getenv("SEARCH_ENGINE_ID")

# Create the service object for the custom search API
service = build("customsearch", "v1", developerKey=api_key)

def google_search(query, num_results):
    results = []
    start_index = 1  # Start from the first result
    max_results = min(num_results, 100)  # Ensure we don't request more than 100 results
    while len(results) < max_results:
        try:
            res = service.cse().list(
                q=query,
                cx=search_engine_id,
                num=min(max_results - len(results), 10),  # Fetch up to 10 results per request
                start=start_index
            ).execute()

            # Add the results to the list
            items = res.get('items', [])
            results.extend(items)

            # Increment the start index to get the next batch of results
            start_index += 10

            # Check if we've reached the end of available results
            if len(items) == 0:
                break

        except Exception as e:
            print(f"An error occurred: {e}")
            break

    return results

# Get user input for the search query
user_query = input("Enter your search query: ")

# Perform the search
search_results = google_search(user_query, 100)

# Print the links of the top 100 results
for item in search_results:
    print(item['link'])
