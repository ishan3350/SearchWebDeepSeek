import requests
from bs4 import BeautifulSoup
import re

def searxng_search(query, searxng_url="http://search.local:8080/search"):
    params = {
        'q': query,        # The search query
        'format': 'json'   # Request JSON formatted results
    }
    try:
        response = requests.get(searxng_url, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()  # Return the response as a Python dictionary
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None

def ask_user():
    query = input("How can I help you?")
    search_results = searxng_search(query)

    print(search_results['results'][0]['url'])

    response  = requests.get(search_results['results'][0]['url'])

    soup = BeautifulSoup(response.text, 'html.parser')

    page_text = soup.get_text()


    prompt = f"Based on the following information only: {page_text} \n\nfrom above text help summarize {query}?"

    return prompt






