import requests
from bs4 import BeautifulSoup
import pandas as pd


def extract(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    url = f'https://www.seek.com.au/cyber-security-jobs?page={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


# Check transform returns chosen div class by using len function
def transform(soup):
    divs = soup.find_all("div", class_="_1wkzzau0 szurmz0 szurmz5")
    return len(divs)


c = extract(0)
print(transform(c))
