#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 22:18:12 2017

@author: gary
"""

import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

def input_dynamic_data():
    lang= input("What Language? ")
    version= float(input("What Version? "))
    skill= input("What skill level? ")
    
    c.execute("INSERT INTO example (Language, Version, skill) VALUES (?, ?, ?)", (lang, version, skill))
    conn.commit()

input_dynamic_data()