#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 22:49:52 2017

mucking about with urllib.request

@author: gary

"""
import urllib


def basic_request():
  
    req = urllib.request.urlopen('https://www.google.com')
    print(req.read())

def parse_request():
    
    '''
    should return HTTPError(req.full_url, code, msg, hdrs, fp)
    and Forbidden status
    '''
    
    values = {'q':'Python Programming tutorials'}
    data = urllib.parse.urlencode(values)
    url = 'https://www.google.com/search?'+data
    #data = data.encode('utf-8')
    
    req = urllib.request.Request(url)
    
    resp = urllib.request.urlopen(req)
    resp_data = resp.read()
    print(resp_data)
    
#basic_request()
#parse_request()