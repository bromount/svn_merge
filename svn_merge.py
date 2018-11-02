#!/usr/bin/python

'''
Creating this code to Merge codes between SVN Branches

Created by BroMount on 1 Nov 2018

'''

import pysvn
import getpass
from datetime import datetime

client = pysvn.Client()

url = 'URL'

def get_login( realm, username, may_save ):
    name = raw_input ("Enter your SVN username : ")
    password = getpass.getpass("Enter your password : ")
    return True,name,password,False

client.callback_get_login = get_login
#client.checkout(URL,'./repository/branches')

commit_messages = client.log(url)
for i, commit in enumerate(commit_messages):
    commit_time = datetime.utcfromtimestamp(commit.date).strftime('%Y-%m-%d %H:%M:%S')
    print i, commit.message, commit.revision, commit.author, commit_time


