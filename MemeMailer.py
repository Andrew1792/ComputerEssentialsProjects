import json
import requests
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase
from email import encoders

def random_meme():
    # gets meme from api then returns the image binary
    response = requests.get("http://meme-api.com/gimme")
    json_data = response.json()

    return requests.get(json_data["preview"][-1]).content

def send_email_with_attachment(to_address, subject, body, attachment):
    # Set up the email content
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    # Attach the body of the email
    msg.attach(MIMEText(body, 'plain'))

    # Attach the photo as a binary attachment
    attachment_data = attachment
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment_data)
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename=photo.jpg")  # Change the filename as needed
    msg.attach(part)

    # Set up the SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = from_address
    smtp_password = app_password

    # Start the SMTP session
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Send the email
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    # Quit the SMTP session
    server.quit()

from_address = 'FROM ADDRESS'
app_password = 'APP PASSWORD'
to_address = 'TO ADDRESS'
subject = 'Memes go brrrrrr'
body = 'This is a meme.'

while True:
    send_email_with_attachment(to_address, subject, body, random_meme())
    print(f"email sent to {to_address}")
    time.sleep(300)
