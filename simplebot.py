#Author : Krishna Parmar
#GIT ID : ParmarKrishna

#first you need to setup enviroment variables for your gmail username and gmail password
#in this code, we will only see how to send simple emails (without any attachments)
import os #importing os will help accessing your enviroment variables 
import smtplib #we will be using smtplib library
from email.message import EmailMessage #importing this so we can have good structure for our message

# 'os.environ.get will take argument of your name of enviroment variable you want to import
my_gmail_username = os.environ.get('replace it with your username enviroment variable') 
my_gmail_password = os.environ.get('replace it with your password enviroment') 

participant = ['krishna.anonymous.201219@gmail.com','parmarkrishna534@gmail.com'] #list of participants you want to send email to

for participant in participant: #a simple loop
    msg = EmailMessage()    #activating method 
    msg['Subject']= " Replace it with Your Subject "
    msg['From']=my_gmail_username
    msg['To'] = participant
    msg.set_content('''
    Set your content here
    ''')
 #connect with gmail server at port 465
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(my_gmail_username,my_gmail_password) #login in gmail server
        smtp.send_message(msg) #Send message 
        print("mail sent to "+participant) #If message gets sent ,it will print it.
    