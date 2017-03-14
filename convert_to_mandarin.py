#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 16:19:28 2017

@author: gary

convert regular numbers to mandarin
"""

trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(us_num):
    '''
    us_num, a string reperesenting a US number 0 to 99
    returns the string mandarin reperesentation of us_num
    '''
    
    num_int = int(us_num)
    
    if 0 <= num_int  <= 10:
        return trans[us_num]
    elif 11 <= num_int <= 19:
        return '{} {}'.format(trans['10'], trans[us_num[-1]])
    elif num_int % 10  == 0:
        return '{} {}'.format(trans[us_num[0]], trans['10'])
    else:
        return '{} {} {}'.format(
            trans[us_num[0]], trans['10'], trans[us_num[-1]])

'''
some test cases for this problem below...
'''

#print(convert_to_mandarin('36'))
#print(convert_to_mandarin('37'))
#print(convert_to_mandarin('38'))
#print(convert_to_mandarin('39'))
#
#print(convert_to_mandarin('20'))
#print(convert_to_mandarin('21'))
#print(convert_to_mandarin('22'))
#print(convert_to_mandarin('23'))
#
#print(convert_to_mandarin('16'))
#print(convert_to_mandarin('17'))
#print(convert_to_mandarin('18'))
#print(convert_to_mandarin('19'))




