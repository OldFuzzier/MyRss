#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

from request_web import get_html

"新书速递"
URL = 'https://book.douban.com/'


def parser_html(text):
    soup = BeautifulSoup(text, 'html.parser')
    li_info_lst = soup.find('div', class_='slide-list').find_all('li')
    titles = [info.find('div', class_='title').find('a').string for info in li_info_lst if info]
    urls = [info.find('div', class_='title').find('a')['href'] for info in li_info_lst if info]
    authors = [info.find('div', class_='author').string.strip() for info in li_info_lst if info]
    abstracts = [info.find('div', class_='more-meta').find('p', class_='abstract').string.strip() for info in li_info_lst if info]
    return titles, urls, authors, abstracts


def main_douban():
    text = get_html(URL)
    titles, urls, authors, abstracts = parser_html(text)
    info_lst = zip(titles, urls, authors, abstracts)
    return info_lst


main_douban()
