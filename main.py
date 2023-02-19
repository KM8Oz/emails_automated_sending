import os
import argparse
import smtplib
import time
import ssl
import configparser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Read the email configuration file
config = configparser.ConfigParser()
config.read('email.conf')

# Set the sender's email address and password from the email configuration file
sender_email = config.get('EMAIL', 'SENDER_EMAIL')
sender_password = config.get('EMAIL', 'SENDER_PASSWORD')

# Set the email subject and message
email_subject =  config.get('EMAIL', 'EMAIL_SUBJECT')
email_message =  config.get('EMAIL', 'EMAIL_MESSAGE')
file_path =  config.get('EMAIL', 'FILE_PATH')

# Set the SMTP server and port for Gmail
smtp_server = config.get('EMAIL', 'EMAIL_SERVER')
smtp_port = config.get('EMAIL', 'EMAIL_PORT')

# Define command-line arguments and help message
parser = argparse.ArgumentParser(description='Send an email from a Gmail account to another email address at a given interval.')
parser.add_argument('recipient_email', type=str, help='the email address of the recipient')
parser.add_argument('time_interval', type=int, help='the time interval in minutes')
args = parser.parse_args()
# Print authentication message
print('''
        To send email using your Gmail account, you need to create an app password. \n
        Follow these steps to create and use an app password: \n
        1. Go to your Google Account.\n
        2. Select Security.\n
        3. Under "Signing in to Google," select App Passwords. You may need to sign in.\n
        4. At the bottom, choose Select app and choose the app you are using.\n
        5. Select device and choose the device you’re using and then Generate.\n
        6. Follow the instructions to enter the App Password. The App Password is the 16-character code in the yellow bar on your device.\n
        7. Tap Done.\n
        ''')

# Log in to the Gmail SMTP server
def send_email(subject, body, file_path=None):
    message = MIMEMultipart()

    # Set up message headers
    message["From"] = sender_email
    message["To"] = args.recipient_email
    message["Subject"] = subject

    # Add message body
    message.attach(MIMEText(body, "plain"))

    # Add attachment file
    if file_path is not None:
        with open(file_path, "rb") as attachment:
            file_name = os.path.basename(file_path)
            part = MIMEApplication(attachment.read(), Name=file_name)
            part["Content-Disposition"] = f'attachment; filename="{file_name}"'
            message.attach(part)

    # Create secure SSL context and start server
    context = ssl.create_default_context()
    # with smtplib.SMTP(smtp_server, smtp_port, context=context) as server:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, args.recipient_email, message.as_string())

# Send the email every time_interval minutes
while True:
    # server.sendmail(sender_email, args.recipient_email, f'Subject: {email_subject}\n\n{email_message}')
    send_email(email_subject, email_message, file_path)
    print(f'Sent email to {args.recipient_email}.')
    time.sleep(args.time_interval * 60) # Convert time_interval from minutes to seconds
