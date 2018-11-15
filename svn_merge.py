#!/usr/bin/python

'''
Creating this code to Merge codes between SVN Branches

Created by BroMount on 1 Nov 2018

'''

import time
import pysvn
import getpass
import re
import os

client = pysvn.Client()

#Getting URLs from User
url1 = raw_input("Please enter the Source branch URL : ")
url2 = raw_input("Please enter the Destination branch URL : ")


#Login Method using PySVN
def get_login( realm, username, may_save ):
    name = raw_input ("Enter your SVN username : ")
    password = getpass.getpass("Enter your password : ")
    return True,name,password,False

client.callback_get_login = get_login

#checkout the branch
client.checkout(url1,'./repository/source/')
print "Checkout of Source branch ",url1," is done"
client.checkout(url2,'./repository/destination/')
print "Checkout of Destination branch ",url2," is done"
	
#Fetch SVN Info	
entry = client.info('./repository/source/')
old_rev = entry.revision.number
#print('Url:',entry.url)
#print('TextTime:', entry.text_time)
#print('revisionNum:', old_rev)

#Get SVN Log 
head = pysvn.Revision(pysvn.opt_revision_kind.number, old_rev)
end = pysvn.Revision(pysvn.opt_revision_kind.number, 52000)

log_messages = client.log('./repository/source/',revision_start=head,revision_end=end,limit=0)

commit_logs = open("./repository/logs/svn_full_commits.txt", "w")
	 
for log in log_messages:
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(log.date))
    commit_logs.write('[%s]' %  log.revision.number)
    commit_logs.write('\t%s' %  timestamp)
    commit_logs.write('\t%s' %  log.author)
    commit_logs.write('\t%s\n' %  log.message)

with open('./repository/logs/svn_full_commits.txt') as f:
    log_lines = f.readlines()

pattern = raw_input("Enter your Pattern here : ")

revisionList = []
for l in log_lines:
    if re.search(pattern, l):
        m = re.match(r"\[\d+\]",l)
	if m:
            revisionList.append(m.group(0))
		 
revisionList1 = [] 
for revNum in revisionList:
    a =revNum.replace('[','')
    revisionList1.append(a.replace(']',''))

print revisionList1

commit_logs.close()

update_file = open("./repository/logs/Update_file_log.txt", "w")
conflicted_files = open("./repository/logs/Conflicted_file_log.txt", "w")
os.chdir ("./repository/destination/")
os.system ("pwd")
#os.system ("svn info")
#os.system ("svn status")
revision_updated = []
revision_conflicted = []
for i in revisionList1:
    #dry Run to get conflict data
    import subprocess
    i = str(i)
    print "Current Revision : ",i
    command = ["svn","merge","--dry-run","-c",i,url1]
    merge =(' '.join(command))
    print "Command Running",merge

    p = subprocess.Popen([merge],stdout=subprocess.PIPE, shell= True)
    output, err = p.communicate()
    print "Output is", output
    if "conflicts" in output:
        print "conflicted revision ",i
        revision_conflicted.append(i)
        conflicted_files.write(output)
    elif "U" in output:
        print "Updated version ",i
        revision_updated.append(i)
        update_file.write(output)
    else:
        print "Non conflicted revision(files might be same) ",i


print "These are the conflicted revisons :",revision_conflicted
print "These are the revisons can be updated :",revision_updated
update_file.close()
conflicted_files.close()

print "Merging the files which can be updated based on the ",pattern

for i in revision_updated:
    #dry Run to get conflict data
    import subprocess
    i = str(i)
    print "Current Revision : ",i
    command = ["svn","merge","-c",i,url1]
    merge =(' '.join(command))
    print "Command Running",merge

    p = subprocess.Popen([merge],stdout=subprocess.PIPE, shell= True)
    output, err = p.communicate()
    print "Output is", output


os.system("svn status")
os.system("svn commit -m \"This is a test\"")
print "Revisions ",revision_updated," merged to ",url2 

