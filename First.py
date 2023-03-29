import requests
from bs4 import BeautifulSoup
import pandas as pd


# First, check status code is 200, if returns 404, API is working but access is denied. Common for Job listing websites (Glassdoor, Indeed).

def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    url = f'https://www.seek.com.au/cyber-security-jobs?page={page}'
    r = requests.get(url, headers)
    return r.status_code
print(extract(0))
