#!/usr/bin/python
# -*-coding: utf-8 -*-
import os
import re
from datetime import datetime
import json
import time
import MySQLdb
import sys
import math
if len(sys.argv) < 2:
    sys.exit(0)
#print(sys.argv[2])
from urllib.request import urlopen, URLError, HTTPError
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError


def getKey(keyin):
    keyin = int(keyin)
    secondnum = math.ceil((keyin-1000)/500)
    frontchar = chr(74) if (keyin%10)==0 else chr(int(keyin%10)+64)
    keyin = str(keyin)
    if(int(keyin) % 1000 == 0):
        lastnum = 50
    elif int(keyin[1:3]) == 50 and int(keyin[3:4]) == 0:
        lastnum = 50
    elif int(keyin)%10 == 0:
        lastnum = (int(keyin[1:3])%50)
    else:
        lastnum = (int(keyin[1:3])%50)+1
     
    if(secondnum <=10):
        secondnum = "0"+str(secondnum)
    if(lastnum <=10):
        lastnum = "0"+str(lastnum)
    return (str(frontchar)+str(secondnum)+str(lastnum))

   


message = sys.argv[1]


result = ''
#print(result)
def intornot(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
#line_bot_api = LineBotApi('AgIQnH2clTRGpu74YMKmHiVMvWsLo0Eg7qOum7xcoaKSjcAp24BfinEtfMTPefvMq9zYr/MnW+MLtPr8+Kd5vKL+VQIBIHWB9grdWkqr3c1vemv4bBAP5n9nRYfG988Z+s8Ps6pfh6mvo+TKMtcqIgdB04t89/1O/w1cDnyilFU=')
status = 0
#print("message")
db = MySQLdb.connect("10.130.88.38","regcol","skr010527","coltroit" ,use_unicode=True, charset='utf8')
cur = db.cursor()
checkuser = "SELECT COUNT(id) FROM `LineUserId` WHERE  userId= \""+sys.argv[2]+"\""
cur.execute(checkuser)
resultcheck = cur.fetchone()

now = datetime.now()

if  message == "!reg" and sys.argv[2] == "Ufb00beda08083bcf402fbd2160b75574":
    query = "SELECT state FROM server WHERE name = \"register\""
    cur.execute(query)
    reg = cur.fetchone()
    reg = reg[0]
    onoroff = "off"
    upque = "UPDATE server SET state=0 WHERE name=\"register\""
    if reg == 0:
         upque = "UPDATE server SET state=1 WHERE name=\"register\""
         onoroff = "on"
    cur.execute(upque)
    db.commit()
    db.close()
    
    print("Register Change status to "+onoroff)
    exit()

if resultcheck == None or int(resultcheck[0]) <= 0:
    print("What The Fuck you don't have permission here GTFO")
    exit()
    
if '!ann' in message:
    line_bot_api = LineBotApi('AgIQnH2clTRGpu74YMKmHiVMvWsLo0Eg7qOum7xcoaKSjcAp24BfinEtfMTPefvMq9zYr/MnW+MLtPr8+Kd5vKL+VQIBIHWB9grdWkqr3c1vemv4bBAP5n9nRYfG988Z+s8Ps6pfh6mvo+TKMtcqIgdB04t89/1O/w1cDnyilFU=')
    message = message.replace('!ann','ประกาศ: ')
    cur.execute("SELECT userId FROM `LineUserId`")
    for row in cur:
        if row[0] != None:
            line_bot_api.push_message(row[0], TextSendMessage(message))
    db.close()
    print("Announcement: "+message +" Successfully send to all staff")
    exit()
    
if len(message) == 4 :
    if intornot(message) == True:
        if int(message) <= 1000:
            print("ERROR: To call code info number must > 1000")
            exit()
    elif intornot(message) == False:
            print("ERROR: To call code info 4 characters must > 1000")
            exit()
    query = "SELECT id,name,surname,nickname FROM freshies WHERE id = " + str(message)
    cur.execute(query)
    results = cur.fetchone()
    
    if results == None:
        print('Code: '+message+' not found!')
    else:
        query = "SELECT seat_id FROM tickets WHERE freshy_id = " +str( results[0])
        cur.execute(query)
        seatres = cur.fetchone()
        #print(results[1])
        stringout= 'Code: [ ' + message+' ]\nName: '+str(results[1]) +'\nSurname: '+str(results[2]) +'\nNickname: '+str(results[3]) +'\nSeatID: '
        if seatres != None:
            print (stringout+seatres[0])
        else:
             print (stringout+' None')
    db.commit()
    db.close()
if len(message) >= 5 and 'c' in message:
    if(message[0:1] != 'c' and message[0:1] != 's'):
        print("Did u mean sxxxx ? (Use for submit)")
        print("Did u mean cxxxx ? (Use for cancel)")
        exit()
    if intornot(message[1:]) == True:
        if int(message[1:]) <= 1000:
            print("ERROR: To cancel code info number must > 1000")
            exit()
    elif intornot(message[1:]) == False:
        print("ERROR: To cancel code info 5 characters must > 1000")
        exit()
    message = message.replace('c','')
    try:
        
        sel= "SELECT id FROM `tickets` WHERE `freshy_id` = \"" + str(message) + "\""
        cur.execute(sel)
        lostid = cur.fetchone()
        if lostid == None:
            print("ERROR: No Ticket for this freshy id code")
            exit()
        lostid = lostid[0]
        query = "DELETE FROM `tickets` WHERE `freshy_id` = \"" + str(message) + "\""
        cur.execute(query)
        insquery = "INSERT INTO `stash` (`lostid`) VALUES (" + "\""+ str(lostid) +"\"" +")"
        cur.execute(insquery)
        db.commit()
        db.close()
        print("Cancelled Register of Freshy ID: "+ str(message))
    except Exception as e:
        print(e)
        print("Error for deleting please try again\n(Due Internet Problem or There's no this code available in ticket)")
        db.rollback()
        db.close()
        exit()

if len(message) >= 5 and 's' in message :
    if(message[0:1] != 'c' and message[0:1] != 's'):
        print("Did u mean sxxxx ? (Use for submit)")
        print("Did u mean cxxxx ? (Use for cancel)")
        exit()
    if intornot(message[1:]) == True:
        if int(message[1:]) <= 1000:
            print("ERROR: To register code info number must > 1000")
            exit()
    elif intornot(message[1:]) == False:
        print("ERROR: To register code info 5 characters must > 1000")
        exit()
    message = message.replace('s','')
    query = "SELECT id,name,surname,nickname FROM `freshies` WHERE `id` = \"" + str(message) + "\""
    cur.execute(query)
    results = cur.fetchone()
    #print(results)
    if results[0] == None:
        print('Code: '+message+' not found!')
        db.commit()
        db.close()
    else:
        query = "SELECT seat_id FROM tickets WHERE freshy_id = " +str( results[0])
        cur.execute(query)
        seatres = cur.fetchone()
        #print(results[1])
        stringout= 'Code: [ ' + message+' ]\nName: '+str(results[1]) +'\nSurname: '+str(results[2]) +'\nNickname: '+str(results[3]) +'\n\nSeatID: '

        if seatres != None:
            print (stringout+seatres[0]+"\nUser Already Register!!!")
        else:
            getnew = 1
            blankid = None
            try:
               
                waitchk = "SELECT lostid FROM `stash` WHERE 1 LIMIT 1"
                cur.execute(waitchk)
                stapple = cur.fetchone()
                if stapple != None:
                    getnew = 0
                    blankid = stapple[0]
            except Exception as E:
                print(E)
                db.rollback()
                db.close()
                exit()
            if getnew == 1:
                
                insquery = "INSERT INTO `tickets` (`freshy_id`,`seat_id`) VALUES (" + "\""+ str(results[0]) +"\"" + "," +  "\""+ "gen" + "\""  +")"
                cur.execute(insquery)
                lastId= getKey( int(cur.lastrowid)+1000)
                if(int(cur.lastrowid) > 4500):
                    db.rollback()
                    print("ERROR Seat are full already\n\nNO TICKET !!!")
                    exit()
                #print(lastId)
                db.commit()
                upquery = ("UPDATE `tickets` SET `seat_id`=\"" + str(lastId) +"\" WHERE `freshy_id` = "+ str(results[0]))
                cur.execute(upquery)
                db.commit()
                db.close()
                print (stringout+ lastId)
            else:
                #print("Disabled")
                try:
                    insquery = "INSERT INTO `tickets` (`id`,`freshy_id`,`seat_id`) VALUES ("  +str(blankid)   + ",\""+ str(results[0]) +"\"" + "," +  "\""+ "gen" + "\""  +")"
                    #print(insquery)
                    #print("")
                    cur.execute(insquery)
                    
                    stashdel = blankid
                    tmp1 = (int(blankid))+1000
                    tmp1 = str(tmp1)
                    lastId= getKey(tmp1)
                    if(int(blankid) > 4500):
                        db.rollback()
                        print("ERROR Seat are full already\n\nNO TICKET !!!")
                        exit()
                    #print(lastId)
                    db.commit()
                    upquery = ("UPDATE `tickets` SET `seat_id`=\"" + str(lastId) +"\" WHERE `freshy_id` = "+ str(results[0]))
                    cur.execute(upquery)
                    db.commit()
                    
                    delquery = ("DELETE FROM `stash` WHERE `lostid` = \""+ str(stashdel) +"\"")
                    cur.execute(delquery)
                    db.commit()
                    db.close()
                    print (stringout+ lastId)
                except Exception as E:
                    print(E)
                    db.rollback()
                    db.close()
                    print("Error for add this code please try again\n(Due Internet Problem or There's no this code available in ticket)")
                    exit()

    #line_bot_api.push_message(groupdelc, TextSendMessage(printer))
    #status = 1
    #print(checkout)
    #
#print(checkout)
#print(letsend)
	
