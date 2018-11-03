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
    file1 = open("./text/commit_messages.txt","a")
    file1.write("{}\n".format(text))
    file1.close()

print "Text file with commit messag created"

message_file = open("./text/commit_messages.txt","r")
lines = message_file.read()

#commit_key = re.search('aarumug',lines)

commit_key = re.findall("aarumug2",lines)

for i in commit_key:
    print commit_key

#print commit_key
'''
if commit_key in None:
    print "No keyword found"
else:
    print commit_key.group(1)
'''    
    



