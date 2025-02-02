import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.inchcalculator.com/what-is-todays-date/")

soup = BeautifulSoup(response.text, 'html.parser')

page_text = soup.get_text()

print(page_text)