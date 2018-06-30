#!/usr/bin/python
# -*-coding: utf-8 -*-
import os
import re

import MySQLdb

import json
import time
import sys

if len(sys.argv) < 2:
    sys.exit(0)
message = sys.argv[1]
db = MySQLdb.connect("10.130.88.38","regcol","skr010527","coltroit" )
cur = db.cursor()

#message = "Debugging "

#print (message)

result = ''
valuetopush = True

query = "SELECT state FROM `server` WHERE name =\""+ "register" +"\""
cur.execute(query)
res = cur.fetchone()
res = res[0]
if (res == 0):
    valuetopush = False


if valuetopush == True:
    query = "SELECT COUNT(`id`) FROM `LineUserId` WHERE userId =\""+ str(message)+"\""
    
    cur.execute(query)
    results = cur.fetchone()[0]
    if results != 0:
        valuetopush = False
        print('You already verify fuck off!')
    else:

        newquery = "INSERT INTO `LineUserId` (`userId`) VALUE (\"" + str(message) + "\")"
        cur.execute(newquery)
        lastId=cur.lastrowid
        db.commit()
        
        db.close()

        #print("INSERT INTO LineUserId (No,userId,RegDate) VALUE (%s,%s,%s)"%(str(lastNumber),message,gdate))
        print('Verify Staff Successful \nWelcome to our system Master your ID: #'+str(lastId))
else:
        print('Verify Staff has closed \nAny Attack or trying breach will log and punishment by law\n//Colonel Master Admin & Developers \nSOS:0625461939')
    
