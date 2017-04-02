#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 22:24:29 2017

@author: gary
"""

import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()


def read_from_database():
    sql = "SELECT * FROM example  SET skill = Beginner WHERE skill = beginner"
    
    for row in c.execute(sql):
        print(row)
        #print(row[0])
    conn.commit()

    
def read_from_database_and_delete():
    sql = "SELECT * FROM example"
    
    for row in c.execute(sql):
        print(row)
    print(20*"#")
    
    sql = "DELETE FROM example WHERE Skill = 'Beginner'"
    
    c.execute(sql)

#def read_from_database_1():
#    sql = "SELECT * FROM example WHERE Skill == 'beginner'"
#    
#    for row in c.execute(sql):
#        print(row)
#        #print(row[0])
#    conn.commit()
#read_from_database_1()

#def read_from_database_2():
#    sql = "SELECT * FROM example"
#    
#    for row in c.execute(sql):
#        print(row)
#        #print(row[0])
#    conn.commit()
#read_from_database_2()


def read_from_database_dynamic():
    
    what_skill = input("What Skill Level are we looking for? ")
    what_language = input("What Language? ")
    what_version = float(input("What Version? "))
    
    sql = "SELECT * FROM example WHERE Skill = ? AND Language = ? AND Version = ?"
    
    for row in c.execute(sql, [(what_skill), (what_language), (what_version)]):
        print(row)
        

def update_database():
    
    sql = "UPDATE example SET Skill = Beginner WHERE Skill = beginner"
    
    for row in c.execute(sql):
        print(row)

def delete_from_database():
    
    sql = "DELETE FROM example WHERE Skill = 'Beginner'"
    c.execute(sql)
    
    conn.commit()
    
        

def delete_from_database_1():
    
    sql = "DELETE FROM example WHERE Skill = 'Expert'"
    c.execute(sql)
    
    conn.commit()
            
        
'''       
 Functions are called below. Uncomment to see what each one does.
'''
#read_from_database()
#read_from_database_1()
#read_from_database_2()
#read_from_database_and_delete()
#read_from_database_dynamic()
#update_database()
#delete_from_database()
#delete_from_database_1()