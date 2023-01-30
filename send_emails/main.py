import smtplib
from decouple import config

HOST = 'smtp.mydomain.com'
SUBJECT = 'Test email from sender'
TO = 'user.mydomain.com'
FROM = 'sender@mydomain.com'
text = 'fire burning praying things to get better'
BODY = '\r\n'.join((
    f"From : {FROM}",
    f"To : {TO}",
    f"Subject :{SUBJECT}","",text
))

server = smtplib.SMTP(HOST)
server.sendmail(FROM,[TO],BODY)
server.quit()