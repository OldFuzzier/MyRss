#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                            '(KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}
    html = requests.get(url, headers=headers, verify=False).text
    return html