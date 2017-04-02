#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 22:11:58 2017

@author: gary
"""

import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()


def input_data():
    c.execute("INSERT INTO example VALUES('Python', '2.7', 'Beginner')")
    c.execute("INSERT INTO example VALUES('Python', '3.3', 'Intermediate')")
    c.execute("INSERT INTO example VALUES('Python', '3.4', 'Expert')")
    conn.commit()

input_data()