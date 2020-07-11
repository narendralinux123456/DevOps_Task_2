import os
import smtplib

EMAIL = 'np8303047651@gmail.com'
PASSWORD = 'narendra@12345'

sender = EMAIL
reciever = 'nk7860208236@gmail.com'
passwd = PASSWORD

server = smtplib.SMTP('smtp.gmail.com',587)
# Encrypts our traffic
server.starttls()
server.login(sender,passwd)
# Enter message that you want to send
message = 'Congratulations Developer--> You achieved your accuracy'
# Sends email
server.sendmail(sender,reciever,message)
# print send message
print("Email send successfully")
