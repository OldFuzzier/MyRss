#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
"电影天堂最新电影"
URL = 'http://www.dytt8.net/index.html'


def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                            '(KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}
    html = requests.get(url, headers=headers).text
    return html


def parser_html(text):
    soup = BeautifulSoup(text, 'html.parser')
    tr_lst = soup.find('div', class_='co_content8').find_all('tr')
    titles = map(lambda li: li.find('a').next_sibling.next_sibling.string, tr_lst)
    urls = map(lambda li: URL[:-10]+li.find('a').next_sibling.next_sibling['href'], tr_lst)
    return titles, urls


def main_dy2018():
    text = get_html(URL)
    titles, urls = parser_html(text)
    info_lst = zip(titles, urls)
    return info_lst

