#Author : Krishna Parmar
#In this file, we will see how can we attach PDFs in mail.
#first you need to setup enviroment variables for your gmail username and gmail password
#IF you haven't setup it yet, you can save it in one variable in script and put that in os.environ.get, but it won't be good as everyone who will have script will be able to see your password
import os #importing os will help accessing your enviroment variables 
import smtplib #we will be using smtplib library
from email.message import EmailMessage #importing this so we can have good structure for our message

# 'os.environ.get' will take argument of your name of enviroment variable you want to import
my_gmail_username = os.environ.get('REPLACE_WITH_YOUR_ENV_VARIABLE') 
my_gmail_password = os.environ.get('REPLACE_WITH_YOUR_ENV_VARIABLE') 
CC = ''#put email adress you want to put in CC
participants=[];#replace it with list of participants you want to send email to 

#Now, you can do 2 things : 
#1-> Put your document in same folder as your script is.
#2->  Get path to your file and save it in one variable.
files = [] #list of your pdf names i.e 'name.pdf' or 'path\name.pdf'
for participant in participants: #a simple loop
    msg = EmailMessage()    #activating method 
    msg['Subject']= "Trial with PDF attachments"
    msg['From']=my_gmail_username
    msg['To'] = participant
    msg['CC'] = CC
    msg.set_content('''\
        REPLACE IT WITH YOUR MESSAGE
    ''')
    #now we will open the file.
    for file in files:
        with open(file,'rb') as f:
            file_data = f.read()
            file_name = f.name
        msg.add_attachment(file_data,maintype='application',subtype = 'octet-stream',filename=file_name)
    #connect with gmail server at port 465, we will have SSL Connection
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(my_gmail_username,my_gmail_password) #login in gmail server
        smtp.send_message(msg) #Send message 
        print("mail sent to "+participant + "with CC in "+CC) #If message gets sent ,it will print it.
    