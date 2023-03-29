import requests
from bs4 import BeautifulSoup
import pandas as pd

'''
Scrape web for job (Cyber security) data, (Title, salary).
Extract - Extract data from url using requests and Soup. Include headers. Use 'f string' if scraping multiple pages
Transform - Find classes in element. Transform into usable and clean data.
Store - Store in dictionary then append to empty list. Save to CSV. 
'''


def extract(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    url = f'https://www.seek.com.au/cyber-security-jobs?page={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def transform(soup):
    divs = soup.find_all("div", class_="_1wkzzau0 szurmz0 szurmz5")
    for target in divs:
        title = target.find('a').text.strip()
        if 'cyber' in title:
            return title
        else:
            pass
        try:
            salary = target.find('div', class_='_1wkzzau0 v28kuf0 v28kuf4 v28kuf2').text.strip()
        except:
            salary = ''.strip()

        job = {
            'Title': title,
            'Salary': salary
        }
        joblist.append(job)
    return


joblist = []

for i in range(1, 7, 1):
    c = extract(1)
    transform(c)

df = pd.DataFrame(joblist)
#df.to_csv('jobs.csv')