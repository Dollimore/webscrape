import requests
from bs4 import BeautifulSoup
import pandas as pd


# First, check status code is 200, if returns 404, API is working but access is denied. Common for Job listing websites.

def extract(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    url = f'https://www.seek.com.au/cyber-security-jobs?page={page}'
    r = requests.get(url, headers)
    return r.status_code
print(extract(0))


def transform(soup):
    divs = soup.find_all("div", class_="_1wkzzau0 szurmz0 szurmz5")
    for target in divs:
        title = target.find('a').text.strip()
    return len(divs)


print(extract(0))
