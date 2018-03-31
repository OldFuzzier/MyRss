#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

from request_web import get_html

"即将上映"
URL = 'https://www.damai.cn/bj/'


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
