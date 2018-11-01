#!/usr/bin/python

'''
Creating this code to Merge codes between SVN Branches

Created by BroMount on 1 Nov 2018

Contributors

Archana Elangovan

'''

import pysvn
import getpass

client = pysvn.Client()

def get_login( realm, username, may_save ):
    name = raw_input ("Enter your SVN username : ")
    password = getpass.getpass("Enter your password : ")
    return True,name,password,False

client.callback_get_login = get_login
client.checkout('https://URL','./repository/branches')



