#first you need to setup enviroment variables for your gmail username and gmail password
import os #importing os will help accessing your enviroment variables 
import smtplib #we will be using smtplib library
from email.message import EmailMessage #importing this so we can have good structure for our message

# 'os.environ.get will take argument of your name of enviroment variable you want to import
my_gmail_username = os.environ.get('REPLACE_WITH_YOUR_ENV_VARIABLE_VALUE') 
my_gmail_password = os.environ.get('REPLACE_WITH_YOUR_ENV_VARIABLE_VALUE') 
CC = ''#put email adress you want to put in CC
participants=[];#replace it with list of participants you want to send email to

for participant in participants: #a simple loop
    msg = EmailMessage()    #activating method 
    msg['Subject']= "Trial"
    msg['From']=my_gmail_username
    msg['To'] = participant
    msg['CC'] = CC
    msg.set_content('''\
        REPLACE IT WITH YOUR MESSAGE
    ''')
 #connect with gmail server at port 465, we will have SSL Connection
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(my_gmail_username,my_gmail_password) #login in gmail server
        smtp.send_message(msg) #Send message 
        print("mail sent to "+participant + "with CC in "+CC) #If message gets sent ,it will print it.
    