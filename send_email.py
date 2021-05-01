'''
   import smtplib
# set the sender mail id
sender = 'sendermailid'
Subject = input("Subject?")
Body = input("Body?")
Recipient = input("Recipient?")


try:
   smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
   smtpObj.sendmail(sender=sender, receivers=Recipient, message=Body)
   print("Email sent!")
except smtplib.SMTPException:
   print( "Error: unable to send email")

   '''




# Python code to illustrate Sending mail from
# your Gmail account
import smtplib
sender = 'arunlahoriseo905@gmail.com'
passw = 'password@gmail@'
Subject = input("Subject?")
Body = input("Body?")
Recipient = input("Recipient?")

# creates SMTP session
s = smtplib.SMTP('localhost')

# start TLS for security
s.starttls()

# Authentication
s.login(sender, passw)


# sending the mail
s.sendmail(sender, Recipient, Body)

# terminating the session
s.quit()

