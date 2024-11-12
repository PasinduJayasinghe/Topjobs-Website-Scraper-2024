import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(page):
    # Using header
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    # Parameter for different categories
    url = f'https://www.topjobs.lk/applicant/vacancybyfunctionalarea.jsp?FA={page}&jst=OPEN'
    r = requests.get(url, headers=headers)
    
    if r.status_code != 200:
        print(f"Error fetching data: {r.status_code}")
        return None

    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    
    table_rows = soup.find_all('tr')
    
    for row in table_rows:
        td_tags = row.find_all('td')
        for td_tag in td_tags:
            print(td_tag.text.strip())
    return

jobs = extract("SDQ")
transform(jobs)
   
