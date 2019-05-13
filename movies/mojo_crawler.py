import requests
from bs4 import BeautifulSoup
import csv
import json
import time
import re
# from models import Movie


def title_preprocessor(title):
    if reg_year.match(title):
        title = reg_year.search(title).group()
    return title


movie_urls = []
movie_list = []
reg_year = re.compile('.+(?=\s\(\d{4}\)$)')
base_url = 'https://www.boxofficemojo.com'
countries = ['us', 'uk', 'france', 'spain', 'germany', 'china', 'japan', 'australia', 'brazil', 'mexico', 'southafrica']

for country in countries:
    print(f'=================={country}==================')
    # 미국
    if country == 'us':
        sub_url = f'/weekend/chart/?yr=2019&wknd=18&p=.htm'
    # 다른나라
    else:
        sub_url = f'/intl/{country}/?yr=2019&wk=18&p=.htm'
    html = requests.get(base_url + sub_url).text
    soup = BeautifulSoup(html, 'html.parser')
    week_list = soup.findAll('table')[4].findAll('tr')[1:11]
    for movie in week_list:
        # title 추출
        title = movie.findAll('td')[2].text
        cleaned_title = title_preprocessor(title)
        
        if cleaned_title not in movie_list:
            movie_list.append(cleaned_title)
            
            temp = {}
            temp['title'] = cleaned_title

            # detail_url 추출
            detail_url = movie.findAll('td')[2].find('a').attrs['href']
            temp['detail_url'] = detail_url

            html = requests.get(base_url + detail_url).text
            soup = BeautifulSoup(html, 'html.parser')

            # 개봉연도 추출
            year = soup.findAll('table')[4].table.findAll('td')[2].b.text.split()[-1]
            temp['year'] = year
            
            movie_urls.append(temp)

with open('.fixtures/raw/mojo.csv', 'w+') as f:
    fieldnames = ['title', 'year', 'detail_url']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    for row in movie_urls:
        writer.writerow(row)