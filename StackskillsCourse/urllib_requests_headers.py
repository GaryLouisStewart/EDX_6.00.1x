#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 22:53:21 2017

mucking about with headers using urllib

@author: gary
"""

import urllib

def parse_request_headers():
    
    '''
    should return HTTPError(req.full_url, code, msg, hdrs, fp)
    and Forbidden status
    '''
    
    values = {'q':'Python Programming tutorials'}
    data = urllib.parse.urlencode(values)
    url = 'https://www.google.com/search?'+data
    #data = data.encode('utf-8')
    
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"
    
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    resp_data = resp.read()
    
    print(resp_data)

parse_request_headers()