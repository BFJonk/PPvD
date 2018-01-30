from email.mime.text import MIMEText
import smtplib

msg = MIMEText(
    "<h1>Een koptekst</h1><p>Hallo daar!</p>", "html")

msg['Subject'] = 'Een HTML-testbericht'
msg['From'] = 'AfzenderAdres'
msg['To'] = 'OntvangerAdres'

s = smtplib.SMTP('localhost')
s.sendmail('AfzenderAdres',
           ['OntvangerAdres'],
           msg.as_string())

print("Bericht verstuurd!")
