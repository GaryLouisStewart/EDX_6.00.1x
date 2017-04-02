#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 23:30:31 2017

ThreeFiddy

@author: Gary

"""

from bs4 import BeautifulSoup
import urllib


def parse_all_the_links():
    req = urllib.request.urlopen('http://feeds.feedburner.com/darknethackers?rss=1')
    xml = BeautifulSoup(req, 'xml')
    
    for item in xml.findAll('link')[1:]:
        print(item)
    

def parse_all_the_items():
    req = urllib.request.urlopen('http://feeds.feedburner.com/darknethackers?rss=1')
    xml = BeautifulSoup(req, 'xml')
    
    for item in xml.findAll('item')[1:]:
        print(item)

#parse_all_the_items()
#parse_all_the_links()