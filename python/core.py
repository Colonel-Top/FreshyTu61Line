#!/usr/bin/python
# -*-coding: utf-8 -*-
import os
import re
from datetime import datetime
import json
import random
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
message = message.lower()
#print(message)

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
db = MySQLdb.connect("10.130.90.185","regcol","skr010527","coltroit" ,use_unicode=True, charset='utf8')
cur = db.cursor()


if  "!sos" in message:
    #line_bot_api = LineBotApi('AgIQnH2clTRGpu74YMKmHiVMvWsLo0Eg7qOum7xcoaKSjcAp24BfinEtfMTPefvMq9zYr/MnW+MLtPr8+Kd5vKL+VQIBIHWB9grdWkqr3c1vemv4bBAP5n9nRYfG988Z+s8Ps6pfh6mvo+TKMtcqIgdB04t89/1O/w1cDnyilFU=')
    #message = message.replace("!sos","[SOS]")
    #line_bot_api.push_message("Ufb00beda08083bcf402fbd2160b75574", TextSendMessage(message))
    print ("*Master Administrator\nContact: http://line.me/ti/p/~promsurin\nTelephone:0625461939")
    
    exit()
if  "!unbanid" in message and sys.argv[2] == "Ufb00beda08083bcf402fbd2160b75574":
    try:
        message = message.replace('!unbanid','')
        if len(message) == 0:
            print("Empty User ID นะคะ")
            exit()
        newquery = "SELECT id,userId FROM `BanUserId` WHERE id= (\"" + str(message) + "\")"
        cur.execute(newquery)
        results = cur.fetchone()
        if results != None:
            #print(results)
            query = "DELETE FROM `BanUserId` WHERE `id` =\""+ str(message) +"\""
            cur.execute(query)
            db.commit()
            db.close()
            print("ท่านได้ทำการยกเลิกการแบนสตาฟไลน์นี้เรียบร้อยค่ะ")
            line_bot_api = LineBotApi('AgIQnH2clTRGpu74YMKmHiVMvWsLo0Eg7qOum7xcoaKSjcAp24BfinEtfMTPefvMq9zYr/MnW+MLtPr8+Kd5vKL+VQIBIHWB9grdWkqr3c1vemv4bBAP5n9nRYfG988Z+s8Ps6pfh6mvo+TKMtcqIgdB04t89/1O/w1cDnyilFU=')
            line_bot_api.push_message(results[1], TextSendMessage("คุณได้ถูกทำการปลดแบนจาก Master Administrator เรียบร้อยค่ะ แจ้งปัญหาโทร: 0625461939 หรือ !sos"))
            print("Unbanned ID: "+message+" Successfully (USER: "+str(results[1]) + ")")
            exit()
        else:
            print("ไม่พบ User ดังกล่าวในระบบแบนค่ะ")
            exit()
        
    except Exception as E:
        print(E)
        db.rollback()
        db.close()
        exit()
if  "!unban" in message and sys.argv[2] == "Ufb00beda08083bcf402fbd2160b75574":
    try:
        message = message.replace('!unban','')
        if len(message) == 0:
            print("Empty User ID นะคะ")
            exit()
        newquery = "SELECT id FROM `BanUserId` WHERE userId= (\"" + str(message) + "\")"
        cur.execute(newquery)
        results = cur.fetchone()
        if results != None:
            #print(results)
            query = "DELETE FROM `BanUserId` WHERE `userId` =\""+ str(message) +"\""
            cur.execute(query)
            db.commit()
            db.close()
            print("ท่านได้ทำการยกเลิกการแบนสตาฟไลน์นี้เรียบร้อยค่ะ")
            line_bot_api = LineBotApi('AgIQnH2clTRGpu74YMKmHiVMvWsLo0Eg7qOum7xcoaKSjcAp24BfinEtfMTPefvMq9zYr/MnW+MLtPr8+Kd5vKL+VQIBIHWB9grdWkqr3c1vemv4bBAP5n9nRYfG988Z+s8Ps6pfh6mvo+TKMtcqIgdB04t89/1O/w1cDnyilFU=')
            line_bot_api.push_message(message, TextSendMessage("คุณได้ถูกทำการปลดแบนจาก Master Administrator เรียบร้อยค่ะ แจ้งปัญหาโทร: 0625461939 หรือ !sos"))
            print("Unbanned ID: "+message+" Successfully")
            exit()
        else:
            print("ไม่พบ User ดังกล่าวในระบบแบนค่ะ")
            exit()
        
    except Exception as E:
        print(E)
        db.rollback()
        db.close()
        exit()

if '!aboutbot' in message:
    print("Bot: Helecho Secretario\nPurpose: Freshy Registration System")
    print("Create By: Promsurin Phutthammawong TU82 \nElectric/Computer Engineering #15\nSOS: 0625461939")
    exit()
    
query = "SELECT COUNT(`id`) FROM `BanUserId` WHERE userId =\""+ str(sys.argv[2])+"\""
cur.execute(query)
results = cur.fetchone()[0]
if results != 0:
    print('คุณถูกแบนโดย Master Administrator\nติดต่อขอปลดแบน:0625461939 หรือ !sos,!aboutbot')
    exit()

now = datetime.now()

    
if  "!ban" in message and sys.argv[2] == "Ufb00beda08083bcf402fbd2160b75574":
    try:
        message = message.replace('!ban','')
        if len(message) == 0:
            print("Empty User ID นะคะ")
            exit()
        newquery = "INSERT INTO `BanUserId` (`userId`) VALUE (\"" + str(message) + "\")"
        cur.execute(newquery)
        lastId=cur.lastrowid
        line_bot_api = LineBotApi('AgIQnH2clTRGpu74YMKmHiVMvWsLo0Eg7qOum7xcoaKSjcAp24BfinEtfMTPefvMq9zYr/MnW+MLtPr8+Kd5vKL+VQIBIHWB9grdWkqr3c1vemv4bBAP5n9nRYfG988Z+s8Ps6pfh6mvo+TKMtcqIgdB04t89/1O/w1cDnyilFU=')
        stringsend = "คุณถูกแบนโดย Master Administrator: BANID:["+str(lastId)+"]\nติดต่อการปลดแบน: 0625461939 หรือพิมพ์ !sos,!aboutbot"
        line_bot_api.push_message(message, TextSendMessage(stringsend))
        db.commit()
        db.close()
        print("Banned ID: \n"+message+"\nSuccessfully ["+str(lastId) +"]")
        exit()
    except Exception as E:
        print("ไอดีผู้ใช้ผิดค่ะไม่สามารถแบนได้ค่ะ")
        db.rollback()
        db.close()
        exit()

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
if  message == "!roundrobin":
    import socket
    print ("[Server: "+socket.gethostname()+" ]")
    exit()

if  message == "!update":
    print ("change value from 4500 to 5000")
    exit()
    
if  message == "!nreg" and sys.argv[2] == "Ufb00beda08083bcf402fbd2160b75574":
    query = "SELECT state FROM server WHERE name = \"nregister\""
    cur.execute(query)
    reg = cur.fetchone()
    reg = reg[0]
    onoroff = "off"
    upque = "UPDATE server SET state=0 WHERE name=\"nregister\""
    if reg == 0:
         upque = "UPDATE server SET state=1 WHERE name=\"nregister\""
         onoroff = "on"
    cur.execute(upque)
    db.commit()
    db.close()
    
    print("Normal Register Change status to "+onoroff)
    exit()
if  message == "!freshyreg" and sys.argv[2] == "Ufb00beda08083bcf402fbd2160b75574":
    query = "SELECT state FROM server WHERE name = \"freshyreg\""
    cur.execute(query)
    reg = cur.fetchone()
    reg = reg[0]
    onoroff = "off"
    upque = "UPDATE server SET state=0 WHERE name=\"freshyreg\""
    if reg == 0:
         upque = "UPDATE server SET state=1 WHERE name=\"freshyreg\""
         onoroff = "on"
    cur.execute(upque)
    db.commit()
    db.close()
    
    print("Freshy Register Change status to "+onoroff)
    exit()
def printerror():
    error = ["Hey Hey! you don't have this permission, Sorry i can't proceed your request bitch",
             "Ahhh i don't think you can use this permission, sorry i'm out",
             "Hmmmmmm Who dafuq are you, sorry can't proceed",
             "Error: Out of permission ya",
             "Nope i won't proceed your request you don't have permission"]
    print(random.choice(error))
    exit()
master = 0


checkuser = "SELECT COUNT(id) FROM `NormalUserId` WHERE  userId= \""+sys.argv[2]+"\""
cur.execute(checkuser)
resultcheck = cur.fetchone()
#print(resultcheck)
if resultcheck[0] != 0:
    master = 1

    
checkuser = "SELECT COUNT(id) FROM `LineUserId` WHERE  userId= \""+sys.argv[2]+"\""
cur.execute(checkuser)
resultcheck = cur.fetchone()
if resultcheck[0] != 0:
    master = 2


night = ['Goodnight','goodnight','ราตรีสวัสดิ์ค่ะ','กู้ดไนท์ค่ะ','ฝันดีค่ะ','อย่าลืมห่มผ้านะคะ','ราตรีสวัสดิ์ค่ะ','อากาศเปลี่ยนแปลงบ่อยดูแลสุขภาพนะคะ','ฝันดี','ไปนอน']
listinsult = ['ตาย','บ้าบอ','ห่วย','เกรียน','เหี้ย','สัส','ฟัคยู','ฟัค','หยิ่ง','ตีน','useless', 'use less','fuck','suck','dick','shit','bitch','ควย','kuy','noob','นูบ','นู้บ','หรี่','กาก','เวร','สถุน']
for tmp in listinsult:
    if tmp in message and sys.argv[2] != "Ufb00beda08083bcf402fbd2160b75574":
        reinsult2 = ['ผี','ผี','ดอก','บลิซซาร์ดไม่คว่ำถ้วย','บลิซซาร์ดไม่คว่ำถ้วย','บลิซซาร์ดไม่คว่ำถ้วย','บลิซซาร์ดไม่คว่ำถ้วย','แหวกกอหญ้า','บ้าห้าร้อยจำพวก','ปลวกใต้หลังคา','หน้าปลาจวด',
        'บ้องกัญชา','ปลาไม่กินเบ็ด','เห็ดสามสี','อิเห็ดต้มยำ','อิเห็ดต้มยำ',
        'กะโหลกซออู้','กู่ไม่กลับ','ตับย่างเกลือ',
        'เชื้ออหิวาต์','ม้าขี้ครอก','หอกขึ้นสนิม','ขิมสายขาด',
        'ชาติสุนัข','ตะหวักตะบวย','กล้วยตากแห้ง','แกงฟักทอง',
        'คลองเจ็ดคด','ชะมดเช็ด','เกล็ดเต็มตัว','มั่วไม่รู้จบ',
        'ศพขึ้นอืด','หืดขึ้นคอ','ปลาหมอแถกเหงือก','เผือกรมควัน',
        'มันสำปะหลัง','โกดังเก็บศพ','กบผัดเผ็ด','เป็ดทอดกระเทียม',
        'ดีไม่ห่างเหิน','เดินไม่ดูทาง','ก้างติดคอ','หม้อก้นทะลุ',
        'หัว***','กระจาดปลาแห้ง',
        'ปลาทูแม่กลอง','สององคต','หดหัวในกระฎอง','สมองเท่าเมล็ดถั่ว',
        'ตัวกินไก่','ใจปลาซิว','หิวตลอดศก','ซกมกเป็นนิจสิน',
        'หินใต้บาดาล','เพลงผิดคีย์','สีทาบ้าน',
        'จานเปื้อนคราบ','แมลงสาบทรงเครื่อง','เปลืองข้าวสุก','กระปุกตังไฉ่',
        'มารสังคม','ผ้าห่มสีซีด','ศพไม่ฉีดฟอร์มาลิน','กระถินริมรั้ว',
        'บัวเต่าถุย','กุ๊ยไร้สังกัด','ผัดผักไฟแดง','แพนงกระดูกหมู',
        'สาคูน้ำกะทิ','กะปิค้างคืน','หื่นเป็น...','ขวานผ่าซาก',
        'กากสิ่งปฏิกูล','พะยูนตากแดด','แรดสองนอ','จอหนังตะลุง',
        'ถุงสองใบ','ไข่ลูกเดียว','เคียวห่วยๆ','ถ้วยสังขยาบูด',
        'กระต่ายขูดมะพร้าว','ชาวสวนทุเรียน','ตะเพียนหางยาว','ว่าวหางขาด',
        'ฉลาดแต่เรื่องโง่','โมฆบุรุษ','มนุษย์สามานย์','เชี่ยวชาญแต่เรื่องชั่ว',
        'แกงคั่วหอยขม','นิยมแต่เรื่องผิด','จิตวิปลาส','ทาสเงินตรา',
        'ชฎายอดหัก','ไม้หลักปักขี้เลน','จิ้งเหลนหางไหม้','ตะไคร่ในท่อน้ำ',
        'ดำตับเป็ด','พูดเท็จหน้าด้านๆ','คอห่านส้วมซึม','อึมครึมตลอดชาติ',
        'หาดจอมเทียน','เชี่ยนตะบันหมาก','ปากปลากะโห้','โถส้วมสาธารณะ',
        'กระบะใส่ขี้แมว','เรือแจวยี่สิบฝีพาย','ควายเขาหัก','ปลักโคลนเลน',
        'ตาเถรตกใต้ถุน','เนรคุณแผ่นดินเกิด','ระเบิดแสวงเครื่อง','ครกกระเดื่องตำข้าว',
        'มะพร้าวห้าวยัดปาก','สากกระเบือยัดก้น','คนไททิ้งแผ่นดิน',
        'ไพร่เพื่อทัก','บักหำน้อย','กบฏต่อราชบัลลังก์','ลานจอดนกเอี้ยง']
        prefixinsult = ['ไอ้','อี','อิ','ไอ']
        print(random.choice(prefixinsult)+""+random.choice(reinsult2)+"ค่ะ\n\nพิมพ์สุภาพๆไม่ได้หรอคะ ? ไลน์นี้ใช้ทำงานไม่ได้ใช้เล่นค่ะ\n\n[Your Activity reported to master admin]")
        line_bot_api = LineBotApi('AgIQnH2clTRGpu74YMKmHiVMvWsLo0Eg7qOum7xcoaKSjcAp24BfinEtfMTPefvMq9zYr/MnW+MLtPr8+Kd5vKL+VQIBIHWB9grdWkqr3c1vemv4bBAP5n9nRYfG988Z+s8Ps6pfh6mvo+TKMtcqIgdB04t89/1O/w1cDnyilFU=')
        line_bot_api.push_message("Ufb00beda08083bcf402fbd2160b75574", TextSendMessage(sys.argv[2]))
        level = "User ระดับทั่วไป"
        if master == 1:
            level = "Administrator ระดับธรรมดา"
        elif master == 2:
            level = "Administrator ระดับทะเบียน"
        line_bot_api.push_message("Ufb00beda08083bcf402fbd2160b75574", TextSendMessage(level))
        line_bot_api.push_message("Ufb00beda08083bcf402fbd2160b75574", TextSendMessage("Submit weird words to you sir: "))
        line_bot_api.push_message("Ufb00beda08083bcf402fbd2160b75574", TextSendMessage(message))
        exit()
for tmp in night:
    if tmp in message:
        print(random.choice(night))
        exit()
        
'''if master ==  0 :
    error = ["Hey Hey! you don't have this permission bitch",
             "What The Fuck, you don't have permission here GTFO",
             "Hmmmmmm Who dafuq are you ?",
             "Error: You are ran out of permission ya"]
    print(random.choice(error))
    exit()'''
def checkmasteradmin():
    if master != 2:
        printerror()
def checknormaladmin():
    if master == 0:
        printerror()

if '!help' == message:
    if master == 1: #normal admin
        print("[HELP]/[ช่วยเหลือคำสั่ง]\n\nคำสั่ง\nพิมพ์ CODE (4 - 5 ตำแหน่ง) จะขึ้นข้อมูลทันที\n!unreg : ถอนตัวออกจากการเป็นสตาฟ (ไม่จำเป็นต้องถอนหลังจากงานระบบจะตัดเอง)\n!sos : สำหรับแสดงข้อมูลการติดต่อเหตุจำเป็น/ด่วน/ติดต่อผู้พัฒนา\n!info:แสดงข้อมูลทั่วไป\n!aboutbot : แสดงข้อมูลเกี่ยวกับบอท\n!f[headline] : เช็คจำนวนข้าวน้องในไลน์")
    elif master == 2: #master
        print("[HELP]/[ช่วยเหลือคำสั่ง]\n\nคำสั่ง\nพิมพ์ CODE (4 - 5 ตำแหน่ง) จะขึ้นข้อมูลทันที\nsxxxx : ทำการลงทะเบียน Freshy ด้วย code xxxx\nคำสั่งย่อย yes : ยืนยันการลงทะเบียนโค้ดนี้\nคำสั่งย่อย no : ยกเลิกการยืนยันการลงทะเบียนโค้ดนี้\n!info :แสดงข้อมูลทั่วไป\n!f[headline] : เช็คจำนวนข้าวน้องในไลน์\n!regann : ทำการประกาศไปยังสตาฟฝ่ายทะเบียนที่เป็น Master ทุกคน\n!ann : ประกาศไปยังสตาฟทุกคนที่อยู่ในระบบไลน์\n!status : แสดงสถานะการค้างโค้ดของคุณ\n!unreg : ถอนตัวออกจากการเป็นสตาฟ (ไม่จำเป็นต้องถอนหลังจากงานระบบจะตัดเอง)\n!sos : สำหรับแสดงข้อมูลการติดต่อเหตุจำเป็น/ด่วน/ติดต่อผู้พัฒนา\n!aboutbot : แสดงข้อมูลเกี่ยวกับบอท\n\nco[xxxx]: Checkout น้อง\ncl[xxxx]: Check ว่าน้อง Checkout ไปรึยัง\ncc[xxxx]: Cancel Checkout\n!f[headline] : เช็คจำนวนข้าวน้องในไลน์")
        if sys.argv[2] == "Ufb00beda08083bcf402fbd2160b75574":
            print("\n\n!reg : เปิด/ปิดลงทะเบียน สตาฟระดับ Master\n!nreg : เปิด/ปิด ลงทะเบียนสตาฟทั่วไป\n!ban[id] : ban userid\n!unban[id] : unban userid\n!unbanid[idnumber] : Unban ด้วย PK ของ Ban\n!roundrobin : แสดง เซิฟเวอร์ปัจจุบันที่ Proceed")
    else:
        print("[HELP]/[ช่วยเหลือคำสั่ง]\n\nคำสั่ง\n!sos : สำหรับแสดงข้อมูลการติดต่อเหตุจำเป็น/ด่วน/ติดต่อผู้พัฒนา\n!aboutbot : แสดงข้อมูลเกี่ยวกับบอท")
    exit()
if '!regann' in message:
    checkmasteradmin()
    line_bot_api = LineBotApi('AgIQnH2clTRGpu74YMKmHiVMvWsLo0Eg7qOum7xcoaKSjcAp24BfinEtfMTPefvMq9zYr/MnW+MLtPr8+Kd5vKL+VQIBIHWB9grdWkqr3c1vemv4bBAP5n9nRYfG988Z+s8Ps6pfh6mvo+TKMtcqIgdB04t89/1O/w1cDnyilFU=')
    message = message.replace('!regann','ประกาศสตาฟฝ่ายทะเบียน: ')
    cur.execute("SELECT userId FROM `LineUserId`")
    for row in cur:
        if row[0] != None:
            line_bot_api.push_message(row[0], TextSendMessage(message))
    db.close()
    print("การประกาศถึงสตาฟฝ่ายทะเบียน: \n["+message +"] \nได้ทำการประกาศเรียบร้อย")
    exit()
if '!reply' in message and sys.argv[2] == "Ufb00beda08083bcf402fbd2160b75574":
    checkmasteradmin()
    line_bot_api = LineBotApi('AgIQnH2clTRGpu74YMKmHiVMvWsLo0Eg7qOum7xcoaKSjcAp24BfinEtfMTPefvMq9zYr/MnW+MLtPr8+Kd5vKL+VQIBIHWB9grdWkqr3c1vemv4bBAP5n9nRYfG988Z+s8Ps6pfh6mvo+TKMtcqIgdB04t89/1O/w1cDnyilFU=')
    message = message.replace('!reply','')
    newmsg = "Developer: " + message
    line_bot_api.push_message(newmsg, TextSendMessage(message))
    print("Message Sent!")
    exit()
if '!info' == message:
    checknormaladmin()
    #normal
    cur.execute("SELECT COUNT(id) FROM `NormalUserId`")
    normalstaff = cur.fetchone()[0]
    cur.execute("SELECT COUNT(id) FROM `tickets`")
    ticket = cur.fetchone()[0]
    cur.execute("SELECT COUNT(id) FROM `freshies`")
    users = cur.fetchone()[0]
    #master
    cur.execute("SELECT COUNT(id) FROM `LineUserId`")
    masterstaff = cur.fetchone()[0]
    
    cur.execute("SELECT COUNT(id) FROM `freshies` WHERE `gender`=\"ชาย\"")
    maleusers = cur.fetchone()[0]
    cur.execute("SELECT COUNT(id) FROM `freshies` WHERE `gender`=\"หญิง\"")
    femaleusers = cur.fetchone()[0]
    cur.execute("SELECT COUNT(id) FROM `BanUserId`")
    banstaff = cur.fetchone()[0]
    if master >= 1:
        print("[Server Status Report]\n\nยอด Staff ทั่วไป: "+str(normalstaff) + " คน\nยอดคนเข้างานปัจจุบัน: "+str(ticket)+" คน\nยอดน้องลงทะเบียนในระบบ: "+str(users)+" คน")
        
        if master == 2:
            cur.execute(" SELECT COUNT(freshies.id) FROM `freshies` JOIN `tickets` ON (freshies.id) = tickets.freshy_id WHERE freshies.gender=\"ชาย\"")
            boardmale = cur.fetchone()[0]
            cur.execute(" SELECT COUNT(freshies.id) FROM `freshies` JOIN `tickets` ON (freshies.id) = tickets.freshy_id WHERE freshies.gender=\"หญิง\"")
            boardfemale = cur.fetchone()[0]
            print("\nยอด Staff ลงทะเบียนหน้างาน: "+str(masterstaff) +" คน\nยอดน้องลงทะเบียนเพศชาย : "+str(maleusers) + " คน\nยอดน้องลงทะเบียนเพศหญิง : "+ str(femaleusers)+ " คน\n")
            print("ยอดน้องเข้างานเพศชาย : "+str(boardmale) + " คน\nยอดน้องเข้างานเพศหญิง : "+ str(boardfemale)  + " คน\n")
    db.close()
    exit()

if '!ann' in message:
    checkmasteradmin()
    line_bot_api = LineBotApi('AgIQnH2clTRGpu74YMKmHiVMvWsLo0Eg7qOum7xcoaKSjcAp24BfinEtfMTPefvMq9zYr/MnW+MLtPr8+Kd5vKL+VQIBIHWB9grdWkqr3c1vemv4bBAP5n9nRYfG988Z+s8Ps6pfh6mvo+TKMtcqIgdB04t89/1O/w1cDnyilFU=')
    message = message.replace('!ann','ประกาศ: ')
    cur.execute("SELECT userId FROM `LineUserId`")
    for row in cur:
        if row[0] != None:
            line_bot_api.push_message(row[0], TextSendMessage(message))
    cur.execute("SELECT userId FROM `NormalUserId`")
    for row in cur:
        if row[0] != None:
            line_bot_api.push_message(row[0], TextSendMessage(message))
    db.close()
    print("การประกาศถึงสตาฟทุกฝ่าย:\n ["+message +"] \nได้ทำการประกาศเรียบร้อย")
    exit()
if '!unreg' == message:
    if master == 2: #master admin
        try:
            query = "DELETE FROM `LineUserId` WHERE `userId` =\""+ sys.argv[2] +"\""
            cur.execute(query)
            db.commit()
            db.close()
            print("คุณได้ทำการยกเลิกการเป็นสตาฟไลน์เรียบร้อย\nขอให้โชคดี //บอทแอดมินเอลเลทโต้")
            exit()
        except Exception as E:
            print("ERROR: "+str(E))
            db.rollback()
            db.close()
            exit()
    elif master == 1: #normal admin
        try:
            query = "DELETE FROM `NormalUserId` WHERE `userId` =\""+ sys.argv[2] +"\""
            cur.execute(query)
            db.commit()
            db.close()
            print("คุณได้ทำการยกเลิกการเป็นสตาฟไลน์เรียบร้อย\nขอให้โชคดี //บอทแอดมินเอลเลทโต้")
            exit()
        except Exception as E:
            print("ERROR: "+str(E))
            db.rollback()
            db.close()
            exit()
if master == 2 and "!status" == message:
    query = "SELECT state FROM `LineUserId` WHERE `userId` =\""+ sys.argv[2] +"\""
    cur.execute(query)
    results = cur.fetchone()[0]
    if results != 0 and len(message)<=5 and len(message)>=1:
        print("[!]คุณได้ค้างการ Confirm ลงทะเบียนของ Freshy ID: "+str(results)+"\n")
    else:
        print("[O]คุณไม่มีการค้างการ Confirm โค้ดใดๆ")
if master == 2:
    query = "SELECT state FROM `LineUserId` WHERE `userId` =\""+ sys.argv[2] +"\""
    cur.execute(query)
    results = cur.fetchone()[0]
    if results != 0 and len(message)<=5 and len(message)>=1:
        print("[!]คุณได้ค้างการ Confirm ลงทะเบียนของ Freshy ID: "+str(results)+"\n")

if len(message) == 6 and 'co' in message:
    checkmasteradmin()
    message = message.replace('co','')
    query = "SELECT COUNT(id) FROM `checkout` WHERE code=\""+message+"\""
    cur.execute(query)
    
    checkinornot = cur.fetchone()
    if(checkinornot[0] != 0):
        print("Code: "+message+" Already Checkout")
        exit()
    query = "INSERT INTO `checkout` (code) VALUES (\""+message+"\")"
    cur.execute(query)
    db.commit()
    db.close()
    print("Check-out Successfuly with Code: "+str(message))
    exit()
if len(message) == 6 and 'cc' in message:
    checkmasteradmin()
    message = message.replace('cc','')
    query = "SELECT COUNT(id) FROM `checkout` WHERE code=\""+message+"\""
    cur.execute(query)
    
    checkinornot = cur.fetchone()
    if(checkinornot[0] == 0):
        print("Code: "+message+" Not Found")
        exit()
    query = "DELETE FROM `checkout` WHERE code=\""+message+"\""
    cur.execute(query)
    print("Check-out Deleted with Code: "+str(message))
    line_bot_api = LineBotApi('AgIQnH2clTRGpu74YMKmHiVMvWsLo0Eg7qOum7xcoaKSjcAp24BfinEtfMTPefvMq9zYr/MnW+MLtPr8+Kd5vKL+VQIBIHWB9grdWkqr3c1vemv4bBAP5n9nRYfG988Z+s8Ps6pfh6mvo+TKMtcqIgdB04t89/1O/w1cDnyilFU=')
    stringcancel = "[!]Freshy ID: " + str(message)+" ได้ถูกยกเลิกการ Checkout"
    db.commit()
    cur.execute("SELECT userId FROM `LineUserId`")
    for row in cur:
        if row[0] != None:
            line_bot_api.push_message(row[0], TextSendMessage(stringcancel))
    db.close()
    exit()
if len(message) == 6 and 'cl' in message:
    checkmasteradmin()
    message = message.replace('cl','')
    query = "SELECT COUNT(id),date FROM `checkout` WHERE code=\""+message+"\""
    cur.execute(query)
    
    checkinornot = cur.fetchone()
    #print(checkinornot[0])
    if(checkinornot[0] == 0):
        print("Code: "+message+" ไม่ได้ทำการ Checkout")
        exit()
    else:
        print("Code นี้ได้ทำการ Check-out จากงานเรียบร้อยแล้วเมื่อเวลา: "+str(checkinornot[1]))
    exit()

if len(message) == 4 and 'f' in message:
    checknormaladmin()
    if(message[0:1] != 'f'):
        exit()
    message = message.replace('f','')
    print("จำนวนพิเศษอาหารในไลน์: " + message)
    
    query = "SELECT COUNT(freshies.vegetarian)FROM freshies WHERE freshies.id in (SELECT freshy_id from tickets where seat_id like \""+message+"%\") AND freshies.vegetarian = 1"
    cur.execute(query)
    vegan = cur.fetchone()
    
    query = "SELECT COUNT(freshies.islamic)FROM freshies WHERE freshies.id in (SELECT freshy_id from tickets where seat_id like \""+message+"%\") AND freshies.islamic = 1"
    cur.execute(query)
    halal = cur.fetchone()

    query = "SELECT COUNT(freshies.id)FROM freshies WHERE freshies.id in (SELECT freshy_id from tickets where seat_id like \""+message+"%\")"
    cur.execute(query)
    normf = cur.fetchone()
    
    print("อาหารอิสลาม: " + str(halal[0]))
    print("อาหารเจ: " + str(vegan[0]))
    alls = 50 - int(halal[0]) - int(vegan[0])
    print("อาหารธรรมดา: "+str(normf[0]))

if len(message) == 5 and 's' not in message and 'c' not in message :
    
    '''if intornot(message) == True:
        
        if int(message) <= 1000:
            checknormaladmin()
            print("ERROR: To call code info number must > 1000")
            exit()
    elif intornot(message) == False:
            #print("ERROR: To call code info 4 characters must > 1000")
            exit()'''
    checknormaladmin()
    query = "SELECT id,name,surname,nickname,disfood,disease,telephone FROM freshies WHERE id IN (SELECT freshy_id FROM tickets WHERE seat_id = "+"\""+str(message)+"\"" + ")"
    cur.execute(query)
    results = cur.fetchone()
    
    if results == None:
        print('Seat: '+message+' not found!')
    else:
        query = "SELECT seat_id FROM tickets WHERE freshy_id = " +str( results[0])
        cur.execute(query)
        seatres = cur.fetchone()
        #print(results[1])
        cur.execute("SELECT STUDENTCODE FROM `reg_data` WHERE STUDENTNAME=\"{}\" AND STUDENTSURNAME=\"{}\"".format(str(results[1]),str(results[2])))
        numcode = cur.fetchone()
        if numcode == None:
            numcode = "ไม่พบเลขนักศึกษา MATCH ชื่อ,นามสกุลนี้"
        else:
            numcode = str(numcode[0])
        stringout= 'Code: [ ' + message+' ]\nชื่อ: '+str(results[1]) +'\nนามสกุล: '+str(results[2]) +'\nชื่อเล่น: '+str(results[3]) + "\nรหัสนักศึกษา: "+ numcode +'\nSeatID: '
        if seatres != None:
            print (stringout+seatres[0]+'\nอาหารที่แพ้: '+str(results[4])+'\nโรคประจำตัว: ' +str(results[5]) + '\nเบอร์โทร: '+str(results[6]))
        else:
            print (stringout+' ยังไม่ได้ลงทะเบียนเข้างาน'+'\nอาหารที่แพ้: '+str(results[4])+'\nโรคประจำตัว: ' +str(results[5]) + '\nเบอร์โทร: '+str(results[6]))
    db.commit()
    db.close()
    exit()
    
if len(message) == 4 or len(message) == 5 and 's' not in message and 'c' not in message:
    
    if intornot(message) == True:
        
        if int(message) <= 1000:
            checknormaladmin()
            print("ERROR: To call code info number must > 1000")
            exit()
    elif intornot(message) == False:
            #print("ERROR: To call code info 4 characters must > 1000")
            exit()
    checknormaladmin()
    query = "SELECT id,name,surname,nickname,disfood,disease FROM freshies WHERE id = " + str(message)
    cur.execute(query)
    results = cur.fetchone()
    
    if results == None:
        print('Code: '+message+' not found!')
    else:
        query = "SELECT seat_id FROM tickets WHERE freshy_id = " +str( results[0])
        cur.execute(query)
        seatres = cur.fetchone()
        #print(results[1])
        cur.execute("SELECT STUDENTCODE FROM `reg_data` WHERE STUDENTNAME=\"{}\" AND STUDENTSURNAME=\"{}\"".format(str(results[1]),str(results[2])))
        numcode = cur.fetchone()
        if numcode == None:
            numcode = "ไม่พบเลขนักศึกษา MATCH ชื่อ,นามสกุลนี้"
        else:
            numcode = str(numcode[0])
            
        stringout= 'Code: [ ' + message+' ]\nชื่อ: '+str(results[1]) +'\nนามสกุล: '+str(results[2]) +'\nชื่อเล่น: '+str(results[3]) +'\nSeatID: '
        if seatres != None:
            print (stringout+seatres[0]+'\nอาหารที่แพ้: '+str(results[4])+'\nโรคประจำตัว: ' +str(results[5]) + "\nเลขนักศึกษา: " + numcode)
        else:
             print (stringout+' ยังไม่ได้ลงทะเบียนเข้างาน'+'\nอาหารที่แพ้: '+str(results[4])+'\nโรคประจำตัว: ' +str(results[5])+ "\nเลขนักศึกษา: " + numcode)
    db.commit()
    db.close()
    exit()

if 'ลงทะเบียนล่าสุด' in message:
    checknormaladmin()
    query = "SELECT id,name,surname,nickname,disfood FROM freshies ORDER BY id DESC LIMIT 1"
    cur.execute(query)
    results = cur.fetchone()
    if results == None:
        print('Empty or data not found!')
    else:
        query = "SELECT seat_id FROM tickets WHERE freshy_id = " +str( results[0])
        cur.execute(query)
        seatres = cur.fetchone()
        #print(results[1])
        stringout= 'Code: [ ' + str(results[0])+' ]\nชื่อ: '+str(results[1]) +'\nนามสกุล: '+str(results[2]) +'\nชื่อเล่น: '+str(results[3]) +'\nSeatID: '
        if seatres != None:
            print (stringout+seatres[0]+'\nอาหารที่แพ้: '+str(results[4]))
        else:
             print (stringout+' ยังไม่ได้ลงทะเบียนเข้างาน/ไม่มีที่นั่ง'+'\nอาหารที่แพ้: '+str(results[4]))
    db.close()
    exit()
    
if len(message) >= 5 and 'c' in message and len(message) <= 7:
    checkmasteradmin()
    if(message[0:1] != 'c' and message[0:1] != 's'):
        print("Did u mean cxxxx ? (Use for cancel)")
        print("Did u mean sxxxx ? (Use for submit)")
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
        insquery = "INSERT INTO `activity_log` (`activity`) VALUES (" + "\""+ "Freshy ID: " + str(message)+" ได้ทำการถูกยกเลิกการลงทะเบียนโดยสตาฟ"  +"\""  +")"
        #print(insquery)
        cur.execute(insquery)
        db.commit()
        line_bot_api = LineBotApi('AgIQnH2clTRGpu74YMKmHiVMvWsLo0Eg7qOum7xcoaKSjcAp24BfinEtfMTPefvMq9zYr/MnW+MLtPr8+Kd5vKL+VQIBIHWB9grdWkqr3c1vemv4bBAP5n9nRYfG988Z+s8Ps6pfh6mvo+TKMtcqIgdB04t89/1O/w1cDnyilFU=')
        stringcancel = "[!]Freshy ID: " + str(message)+" ได้ทำการถูกยกเลิกเนื่องจากพิมพ์ผิด" 
        cur.execute("SELECT userId FROM `LineUserId`")
        for row in cur:
            if row[0] != None:
                line_bot_api.push_message(row[0], TextSendMessage(stringcancel))
            
        print("คุณได้ทำการยกเลิกการลงทะเบียนของ Freshy ID: "+ str(message))
        db.close()
    except Exception as e:
        print(e)
        print("Error for deleting please try again\n(Contact Master Admin  : 0625461939 / !sos)")
        db.rollback()
        db.close()
        exit()
if message == "no":
    checkmasteradmin()
    query = "SELECT state FROM `LineUserId` WHERE `userId` =\""+ sys.argv[2] +"\""
    cur.execute(query)
    results = cur.fetchone()[0]
    if results == 0:
        print("เราไม่พบว่ามี Confirmation ที่ค้างอยู่ ถ้าคิดว่าระบบผิดพลาดกรุณาตรวจสอบก่อนแจ้ง Master Admin")
        exit()
    else:
        upquery = ("UPDATE `LineUserId` SET `state`=\"" + "0" +"\" WHERE `userId` = "+ "\""+sys.argv[2] + "\"" )
        cur.execute(upquery)
        db.commit()
        query = "SELECT id,name,surname,nickname FROM `freshies` WHERE `id` = \"" + str(results) + "\""
        cur.execute(query)
        results = cur.fetchone()
        stringout= 'Code: [ ' + str(results[0])+' ]\nName: '+str(results[1]) +'\nSurname: '+str(results[2]) +'\nNickname: '+str(results[3])
        print(stringout+" \n\nคุณได้ทำการยกเลิกการยืนยัน Confirm Freshy ID นี้เรียบร้อยแล้ว")
        
        db.close()
        exit()
if message == "yes":
    checkmasteradmin()
    query = "SELECT state FROM `LineUserId` WHERE `userId` =\""+ sys.argv[2] +"\""
    cur.execute(query)
    results = cur.fetchone()[0]
    if results == 0:
        print("เราไม่พบว่ามี Confirmation ที่ค้างอยู่ ถ้าคิดว่าระบบผิดพลาดกรุณาตรวจสอบก่อนแจ้ง Master Admin")
        exit()
    if results != None:
        message = results
        
        query = "SELECT seat_id FROM tickets WHERE freshy_id = " +str(message)
        cur.execute(query)
        seatres = cur.fetchone()
        #print(results[1])
        
        if seatres != None:
            query = "SELECT id,name,surname,nickname FROM `freshies` WHERE `id` = \"" + str(message) + "\""
            cur.execute(query)
            results = cur.fetchone()
            stringout= 'Code: [ ' + str(message)+' ]\nName: '+str(results[1]) +'\nSurname: '+str(results[2]) +'\nNickname: '+str(results[3]) +'\n\nSeatID: '
            print (stringout+seatres[0]+"\nUser Already Register!!!")
            upquery = ("UPDATE `LineUserId` SET `state`=\"" + "0" +"\" WHERE `userId` = "+ "\""+sys.argv[2] + "\"" )
            cur.execute(upquery)
            db.commit()
            db.close()
            exit()
        
        query = "SELECT id,name,surname,nickname FROM `freshies` WHERE `id` = \"" + str(message) + "\""
        
        cur.execute(query)
        results = cur.fetchone()
        stringout= 'Code: [ ' + str(message)+' ]\nName: '+str(results[1]) +'\nSurname: '+str(results[2]) +'\nNickname: '+str(results[3]) +'\n\nSeatID: '
        '''query = "SELECT seat_id FROM tickets WHERE freshy_id = " +str( results[0])
        #print(query)
        cur.execute(query)
        seatres = cur.fetchone()
        #print(seatres)
        if seatres == None:
            stringout = stringout + "-"
        else:
            stringout = stringout + seatres'''
        #print(results)
        if True:
            
            if True:
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
                    if(int(cur.lastrowid) > 5000):
                        db.rollback()
                        print("ERROR Seat are full already\n\nNO TICKET !!!")
                        exit()
                    #print(lastId)
                    db.commit()
                    upquery = ("UPDATE `tickets` SET `seat_id`=\"" + str(lastId) +"\" WHERE `freshy_id` = "+ str(results[0]))
                    cur.execute(upquery)
                    upquery = ("UPDATE `LineUserId` SET `state`=\"" + "0" +"\" WHERE `userId` = "+ "\""+sys.argv[2] + "\"" )
                    cur.execute(upquery)
                    db.commit()
                    
                    print (stringout+ lastId+"\n\nการลงทะเบียนเสร็จสมบูรณ์")
                    insquery = "INSERT INTO `activity_log` (`activity`) VALUES (" +"\""+ "Freshy ID: " + str(lastId)+" just got ticket!" +"\""+")"
                    cur.execute(insquery)
                    db.commit()
                    db.close()
                    exit()
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
                        if(int(blankid) > 5000):
                            db.rollback()
                            upquery = ("UPDATE `LineUserId` SET `state`=\"" + "0" +"\" WHERE `userId` = "+ "\""+sys.argv[2] + "\"" )
                            cur.execute(upquery)
                            db.commit()
                            db.close()
                            print("ERROR Seat are full already\n\nNO TICKET !!!")
                            exit()
                        #print(lastId)
                        db.commit()
                        upquery = ("UPDATE `tickets` SET `seat_id`=\"" + str(lastId) +"\" WHERE `freshy_id` = "+ str(results[0]))
                        cur.execute(upquery)
                        db.commit()
                        
                        delquery = ("DELETE FROM `stash` WHERE `lostid` = \""+ str(stashdel) +"\"")
                        cur.execute(delquery)
                        upquery = ("UPDATE `LineUserId` SET `state`=\"" + "0" +"\" WHERE `userId` = "+ "\""+sys.argv[2] + "\"" )
                        cur.execute(upquery)
                        db.commit()
                        insquery = "INSERT INTO `activity_log` (`activity`) VALUES (" + "\""+ "Freshy ID: " + str(lastId) + " just got ticket!"  +"\"" +")"
                        cur.execute(insquery)
                        db.commit()
                        db.close()
                        print (stringout+ lastId+ "\n\nการลงทะเบียนเสร็จสมบูรณ์")
                        exit()
                    except Exception as E:
                        print(E)
                        db.rollback()
                        db.close()
                        print("Error for add this code please try again\n(Due Internet Problem or There's no this code available in ticket)")
                        exit()


if len(message) >= 5 and 's' in message and len(message) <= 7:
    checkmasteradmin()
    query = "SELECT state FROM `server` WHERE name =\""+ "freshyreg" +"\""
    cur.execute(query)
    res = cur.fetchone()
    res = res[0]
    if (res == 0):
        print("Register closed Disallowed Contact Master Administrator")
        exit()
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
    if results == None:
        print('Code: '+message+' not found!')
        db.close()
        exit()
    numcode = "ไม่พบเลขนักศึกษา MATCH ชื่อ,นามสกุลนี้"
    cur.execute("SELECT STUDENTCODE FROM `reg_data` WHERE STUDENTNAME=\"{}\" AND STUDENTSURNAME=\"{}\"".format(str(results[1]),str(results[2])))
    numcode = cur.fetchone()
    if numcode == None:
        numcode = "ไม่พบเลขนักศึกษา MATCH ชื่อ,นามสกุลนี้"
    else:
        numcode = str(numcode[0])
    query = "SELECT state FROM `LineUserId` WHERE `userId` =\""+ sys.argv[2] +"\""
    cur.execute(query)
    resultsc = cur.fetchone()
    
    
    if resultsc[0] != 0:
        print("นี่คือข้อมูลการค้างการ Confirm ลงทะเบียนของ Freshy ID: "+str(resultsc[0]) )
        query = "SELECT id,name,surname,nickname FROM `freshies` WHERE `id` = \"" + str(resultsc[0]) + "\""
        cur.execute(query)
        #print(query)
        resultsc = cur.fetchone()
        #print(results)
        #print("SELECT STUDENTCODE FROM `reg_data` WHERE STUDENTNAME=\"{}\" AND STUDENTSURNAME=\"{}\"".format(str(resultsc[1]),str(resultsc[2])))
        stringout= 'Code: [ ' + str(resultsc[0])+' ]\nName: '+str(resultsc[1]) +'\nSurname: '+str(resultsc[2]) +'\nNickname: '+str(resultsc[3]) +'\n\nStudent ID: '+numcode+'\n\nกรุณาตรวจสอบข้อมูลว่าถูกต้องและยืนยันโดยพิมพ์ (yes/no)'
        print(stringout)
        exit()
    
 
    query = "SELECT seat_id FROM tickets WHERE freshy_id = " +str(message)
    cur.execute(query)
    seatres = cur.fetchone()
    #print(results[1])
    
    if seatres != None:
        stringout= 'Code: [ ' + str(message)+' ]\nName: '+str(results[1]) +'\nSurname: '+str(results[2]) +'\nNickname: '+str(results[3]) +'\n\nSeatID: '
        print (stringout+seatres[0]+"\nUser Already Register!!!")
        db.close()
        exit()
    upquery = ("UPDATE `LineUserId` SET `state`=\"" + str(message) +"\" WHERE `userId` = "+ "\""+sys.argv[2] + "\"" )
    cur.execute(upquery)
    db.commit()
    stringout= 'Code: [ ' + str(message)+' ]\nName: '+str(results[1]) +'\nSurname: '+str(results[2]) +'\nNickname: '+str(results[3]) +'\n\nStudent ID: '+numcode+'\n\nกรุณาตรวจสอบข้อมูลว่าถูกต้องและยืนยันโดยพิมพ์ (yes/no)'
    print(stringout)
    db.close()


    #line_bot_api.push_message(groupdelc, TextSendMessage(printer))
    #status = 1
    #print(checkout)
    #
#print(checkout)
#print(letsend)3


        
allmsg =['ข้อมูลลงทะเบียน','ข้อมูลการลงทะเบียน','report การลงทะเบียน','report ลงทะเบียน','ยอดลงทะเบียน','รายงานการลงทะเบียน','รายงานทะเบียน','สรุปยอดลงทะเบียน','สรุปการลงทะเบียน','ลงทะเบียนตอนนี้']
for tmp in allmsg:
    if tmp in message:
        checknormaladmin()
        #normal
        cur.execute("SELECT COUNT(id) FROM `NormalUserId`")
        normalstaff = cur.fetchone()[0]
        cur.execute("SELECT COUNT(id) FROM `tickets`")
        ticket = cur.fetchone()[0]
        cur.execute("SELECT COUNT(id) FROM `freshies`")
        users = cur.fetchone()[0]
        #master
        cur.execute("SELECT COUNT(id) FROM `LineUserId`")
        masterstaff = cur.fetchone()[0]
        
        cur.execute("SELECT COUNT(id) FROM `freshies` WHERE `gender`=\"ชาย\"")
        maleusers = cur.fetchone()[0]
        cur.execute("SELECT COUNT(id) FROM `freshies` WHERE `gender`=\"หญิง\"")
        femaleusers = cur.fetchone()[0]
        cur.execute("SELECT COUNT(id) FROM `BanUserId`")
        banstaff = cur.fetchone()[0]
        if master >= 1:
            print("รายงานค่ะ\n\nยอด Staff ทั่วไป: "+str(normalstaff) + " คน\nยอดคนเข้างานปัจจุบัน: "+str(ticket)+" คน\nยอดน้องลงทะเบียนในระบบ: "+str(users)+" คน")
            if master == 2:
                cur.execute(" SELECT COUNT(freshies.id) FROM `freshies` JOIN `tickets` ON (freshies.id) = tickets.freshy_id WHERE freshies.gender=\"ชาย\"")
                boardmale = cur.fetchone()[0]
                cur.execute(" SELECT COUNT(freshies.id) FROM `freshies` JOIN `tickets` ON (freshies.id) = tickets.freshy_id WHERE freshies.gender=\"หญิง\"")
                boardfemale = cur.fetchone()[0]
                print("\nยอด Staff ลงทะเบียนหน้างาน: "+str(masterstaff) +" คน\nยอดน้องลงทะเบียนเพศชาย : "+str(maleusers) + " คน\nยอดน้องลงทะเบียนเพศหญิง : "+ str(femaleusers)+ " คน\n")
                print("ยอดน้องเข้างานเพศชาย : "+str(boardmale) + " คน\nยอดน้องเข้างานเพศหญิง : "+ str(boardfemale)  + " คน\n")
        db.close()
        exit()    	
allmsg =['thank','thanks','thx','ขอบคุณ','thank you','ขอบใจ','ขอบน้ำใจ']
for tmp in allmsg:
    if tmp in message and 'เอลเลท' in message:
        checknormaladmin()
        backf = ['ค่ะ','ค่าาาา','เหมี๊ยว ~']
        print(random.choice(backf))
        db.close()
        exit()
allmsg =['helecho','Helecho','เอลเลท','เอลเลทโต้','เอล']              
for tmp in allmsg:
    if tmp in message:
        backf = ['ค่ะ','ค่ะ ?','มีอะไรให้ช่วยหรือคะ ?','ค่าาาา','เหมียว ~']
        print(random.choice(backf))
        db.close()
        exit()
