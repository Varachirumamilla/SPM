import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('chvaralakshmi2019@gamil.com ','yvinqeoxhnlbyzza')
    msg=EmailMessage()
    msg['From']='chvaralakshmi2019@gamil.com'
    msg['Subject']=subject
    msg['To']=to
    msg.set_content(body)
    server.send_message(msg)
    server.quit()
