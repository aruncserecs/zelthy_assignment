# importing the required library.
import smtplib
sender_mail_id = 'sender@mail.com'
sender_password = 'sender_mail_pass'
subject = input("Subject? : ")
body = input("Body? : ")
recipient_mail_id = input("Recipient? : ")

# creates SMTP session
email = smtplib.SMTP('smtp.gmail.com', 587)

# TLS for security
email.starttls()

# authentication
# compiler gives an error for wrong credential.
email.login(sender_mail_id, sender_password)


# sending the mail
email.sendmail(sender_mail_id, recipient_mail_id, body)

print("Email sent!")
# terminating the session
email.quit()

