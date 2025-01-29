import smtplib
import getpass
import tkinter as tk
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

my_email = input('Enter sender:')
password = getpass.getpass('Enter password:')
destinatary = input('Enter recipient:')
subject = input('Enter subject:')
message_body = input('Enter message body:')
document_path = input('Enter document path:')
document_name = input('Enter document name:')

email_to_send = MIMEMultipart()
email_to_send['From'] = my_email
email_to_send['to'] = destinatary
email_to_send['subject'] = subject
email_to_send.attach(MIMEText(message_body, 'plain'))
archive_attached = open(document_path, 'rb')
MIME_attach = MIMEBase('application', 'octet-stream')
MIME_attach.set_payload((archive_attached).read())

encoders.encode_base64(MIME_attach)
MIME_attach.add_header('Content-Disposition', 'attachment; filename= %s' %document_name)
email_to_send.attach(MIME_attach)

sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
sesion_smtp.starttls()
sesion_smtp.login(my_email, password)
text = email_to_send.as_string()
sesion_smtp.sendmail(my_email, destinatary, text)
sesion_smtp.quit()

