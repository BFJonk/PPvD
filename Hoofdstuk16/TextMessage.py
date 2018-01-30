from email.mime.text import MIMEText
import smtplib

msg = MIMEText("Hallo daar!")

msg['Subject'] = 'Een testbericht'
msg['From'] = 'AfzenderAdres'
msg['To'] = 'OntvangerAdres'

s = smtplib.SMTP('localhost')
s.sendmail('AfzenderAdres',
           ['OntvangerAdres'],
           msg.as_string())

print("Bericht verstuurd!")
