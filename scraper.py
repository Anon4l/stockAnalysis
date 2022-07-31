import requests
import re
import json
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0'}
def get_news(subject):
    url = 'https://www.google.com/search?q=' + subject + '&tbm=nws'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    news = soup.find_all("div",class_ = 'BNeawe s3v9rd AP7Wnd') #, class_='mCBkyc y355M ynAwRc MBeuO jBgGLd OSrXXb'  soup.text.split('...')
    news_list = []
    for n in news:
        news_list.append(re.sub("(\d|\d\d) (horas|dias|semanas|meses|mes|semana|dia|hora|anos) atrás","",n.text))
    news_list = list(set(news_list))
    return news_list