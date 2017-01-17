#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
"即将上映"
URL = 'https://www.damai.cn/bj/'


def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                            '(KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}
    html = requests.get(url, headers=headers, verify=False).text
    return html


def parser_html(text):
    soup = BeautifulSoup(text, 'html.parser')
    li_lst = soup.find('div', class_='index-con').next_sibling.next_sibling.find_all('li')
    titles = [li.find('dt').find('a')['title'] for li in li_lst]
    prices = map(lambda x: x.find('p', class_='price').find('strong').text if x.find('p', class_='price').find(
        'strong') is not None else 'none', li_lst)
    time = [i.find('p', class_='time').string for i in li_lst]
    places = [i.find('p', class_='place').string for i in li_lst]
    urls = [i.find('a')['href'] for i in li_lst]
    return titles, prices, time, places, urls


def main_damai():
    text = get_html(URL)
    title, prices, time, place, urls = parser_html(text)
    info_lst = zip(title, prices, time, place, urls)
    return info_lst
