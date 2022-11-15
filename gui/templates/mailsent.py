from email.message import EmailMessage
#from testemail import iaesyhosytrvbksr
import ssl
import smtplib
import time
url_import = input("Enter the URL: ")
email_rece = input("Enter the Email: ")
def email_secureweb():
    email_sender = 'bhattabhishek835@gmail.com'
    email_password = 'iaesyhosytrvbksr'

    email_receiver = email_rece
    change_time = time.ctime()

    subject = 'Secure web'
    body = '''
    Please check the changes at time "{current_time}"! 
    '''.format(current_time = change_time)

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver,em.as_string())

email_secureweb()

#iaesyhosytrvbksr
