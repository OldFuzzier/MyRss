#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
"电影天堂最新电影"
URL = 'http://www.dy2018.com/'

def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                            '(KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}
    html = requests.get(url, headers=headers).content
    return html

def parser_html(text):
    soup = BeautifulSoup(text, 'html.parser')
    li_lst = soup.find('div', class_='co_content222').find_all('li')
    titles = map(lambda li: li.find('a').string, li_lst)
    urls = map(lambda li: URL+li.find('a')['href'], li_lst)
    return titles, urls

def main_dy2018():
    text = get_html(URL)
    titles, urls = parser_html(text)
    info_lst = zip(titles, urls)
    return info_lst





