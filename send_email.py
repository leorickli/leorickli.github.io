import smtplib
from email.message import EmailMessage
from flask import Flask, request

app = Flask(__name__)

@app.route('/send_email', methods=['POST'])
def send_email():
    # Get the form data
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')

    # Create the email message
    msg = EmailMessage()
    msg['From'] = email
    msg['To'] = 'engleonardomoreira@gmail.com'  # Replace with the actual recipient email address
    msg['Subject'] = subject
    msg.set_content(message)

    # Send the email
    with smtplib.SMTP('your-smtp-server.com', 587) as smtp:
        smtp.starttls()
        smtp.login('engleonardomoreira@gmail.com', 'gspxahxeeqfdnudc')  # Replace with your actual email credentials
        smtp.send_message(msg)

    return 'Email sent successfully!'

if __name__ == '__main__':
    app.run()
