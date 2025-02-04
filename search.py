import requests
from bs4 import BeautifulSoup


#Using serxng to search the web
# https://github.com/ishan3350/SearXNG

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

#asking user the question and then searching it
def ask_user():
    query = input("How can I help you?")
    search_results = searxng_search(query)

    results = search_results.get('results', [])

    page_text = ""

#get the text from top 5 results
    for i in results[:5]:
        url = i.get('url')
        print(url)
        response  = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')

        page_text += soup.get_text()


#preparing the prompt for Deepseek model running on ollama server
    prompt = f"Based on the following information only: {page_text} \n\nfrom above text help explain {query} in detail"

    return prompt






