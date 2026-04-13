import smtplib
from email.message import EmailMessage

from_email_addr = "hyfgg20070723@qq.com"
from_email_pass = "kbumkthigyhfdfhc"
to_email_addr = "20119455@setu.ie"

body = "Hello from Raspberry Pi"
msg = EmailMessage()
msg.set_content(body)

msg['From'] = from_email_addr
msg['To'] = to_email_addr
msg['Subject'] = 'TEST EMAIL'

server = smtplib.SMTP('smtp.qq.com', 587)
server.starttls()
server.login(from_email_addr, from_email_pass)
server.send_message(msg)
print('Email sent')
server.quit()
