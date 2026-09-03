import smtplib
from email.mime.text import MIMEText
from config import *

def send_email(to_addr,subject,body):
    msg=MIMEText(body)
    msg['Subject']=subject
    msg['From']=SMTP_USER
    msg['To']=to_addr
    try:
        s=smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
        s.starttls()
        s.login(SMTP_USER,SMTP_PASSWORD)
        s.send_message(msg)
        s.quit()
        return True
    except Exception:
        return False
