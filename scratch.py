from __future__ import print_function
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

USERNAME = 'wikipediabotus@gmail.com'
PASSWORD = 'wiki1942'
FROM_ADR = 'Wikipedia Bot<wikipediabotus@gmail.com>'

def send_mail(to, name,  subject, text):
   msg = MIMEMultipart()
   msg['From'] = FROM_ADR
   msg['To'] = name
   msg['Date'] = formatdate(localtime=True)
   msg['Subject'] = subject
   msg.attach(MIMEText(text, _charset='utf-8'))
   server.sendmail(FROM_ADR, to, msg.as_string())

send_mail("moritzschuetz1@gmail.com", "Moritz" , "TestÜ", "ÜLÜHÜ ÜCKBÜR")
