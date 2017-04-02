#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 21:33:27 2017

@author: gary

creating a database in sqlite3
"""

import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()


def create_table():
    c.execute("CREATE TABLE example(Language VARCHAR, Version REAL, Skill TEXT)")

def input_data():
    c.execute("INSERT INTO example VALUES('Python', '2.7', 'Beginner')")
    c.execute("INSERT INTO example VALUES('Python', '3.3', 'Intermidiate')")
    c.execute("INSERT INTO example VALUES('Python', '3.4', 'Expert')")

#create_table()
#input_data()