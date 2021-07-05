#import smtplib
#from email import encoders
#from email.mime.text import MIMEText
#from email.mime.base import MIMEBase
#from email.mime.multipart import MIMEMultipart
#server = smtplib.SMTP('smtp.gmail.com',25)
#server.ehlo()
#server.login('mail@gmail.com','password123')
#msg = MIMEMultipart()
#msg['From'] = 'mail'
#msg['To'] = 'testmails@spaml.de'
#msg['Subject'] = 'Just A Test'
#server.send_message('mail@gmail.com','zouwau@spaml.de','testing with python')
import math
import socket
import threading
import os
import re
contentmath = dir(math)
contentsocket = dir(socket)
contentthreading = dir(threading)
#print(contentsocket)
#print("\t")
#print(contentmath)
#print("\t")
#print(contentthreading)

#fo = open("test.txt")
#print(fo.name)
#print(fo.closed)
#print(fo.mode)
#os.rename('test.txt','testname.txt')
try:
 fo = open("testname.txt","wb")
 fo.write("Python is amazing")
 #fo.close
except:
    print("Error in writting in the file")
else:
    print("Content written successfully")
    fo.close() 

state = "Dogs are better than cats"
searchObj = re.search(r'(.*) are (.*?) .*', state,re.M|re.I)

if searchObj:
    print("searchObj.group() : ",searchObj.group())
    print("searchObj.group(1) : ",searchObj.group(1))
    print("searchObj.group(2) : ",searchObj.group(2))
else:
    print("Nothing found")
