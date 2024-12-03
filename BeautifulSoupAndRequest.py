from bs4 import BeautifulSoup
import requests

url = 'https://www.scrapethissite.com/pages/forms/'

page = requests.get(url)
soup = BeautifulSoup(page.text, features="html.parser")  # Explicitly specify the parser

print(soup.prettify())  # Optional: To see the parsed HTML

