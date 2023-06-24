import smtplib
from email.message import EmailMessage

# Get the form data
name = input("Name: ")
email = input("Email: ")
subject = input("Subject: ")
message = input("Message: ")

# Create the email message
msg = EmailMessage()
msg['From'] = email
msg['To'] = 'engleonardomoreira@gmail.com'
msg['Subject'] = subject
msg.set_content(message)

# Send the email
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login('engleonardomoreira@gmail.com', 'gspxahxeeqfdnudc')
    smtp.send_message(msg)
