import smtplib
sender = 'sender email id'
password = 'sender_password'
subject = input("Subject?")
body = input("Body?")
recipient = input("Recipient?")

# creates SMTP session
session = smtplib.SMTP('localhost')

# start TLS for security
session.starttls()

# Authentication
session.login(sender, password)


# sending the mail
session.sendmail(sender, recipient, body)

# terminating the session
session.quit()
print("Email sent!")

