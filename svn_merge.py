#!/usr/bin/python

'''
Creating this code to Merge codes between SVN Branches

Created by BroMount 1 Nov 2018

'''

import pysvn

client = pysvn.Client()

def get_login( realm, username, may_save ):
    name = raw_input ("Enter your SVN username : ")
    password = raw_input("Enter your password : ")
    return True,name,password,False

client.callback_get_login = get_login
client.checkout('https://URL','./examples/pysvn')

