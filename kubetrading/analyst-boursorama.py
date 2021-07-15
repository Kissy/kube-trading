import logging
import re
import requests
from bs4 import BeautifulSoup

url = "https://www.boursorama.com/bourse/actions/consensus/recommandations-paris/"
page = requests.get(url)

if not page.status_code == 200:
    logging.error("Failed to retrieve url {} with error {}", url, page.status_code)
else:
    soup = BeautifulSoup(page.text, 'html.parser')
    rows = soup.select('.c-analysts table.c-table tbody.c-table__body tr.c-table__row')
    for row in rows:
        url = row.select_one('td:nth-child(1) a')['href']
        match = re.match('^/cours/consensus/1rP([^/]+)/$', url)
        if match:
            ticker = match.group(1)
            recommendation = row.select_one('td:nth-child(2) span.u-only-clipboard').text.strip()
            objective = float(row.select_one('td:nth-child(4)').text.strip())
            analyst_count = row.select_one('td:nth-child(6)').text.strip() # TODO parse
            per = float(row.select_one('td:nth-child(10)').text.strip())
            print(ticker + " " + recommendation + " " + str(objective) + " " + analyst_count + " " + str(per))
