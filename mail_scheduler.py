import smtplib
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import date
from datetime import datetime


def send_email():
    # Set up your email details
    sender_email = 'sender@gmail.com'
    sender_password = ''
    receiver_email = 'receiver@gmail.com'
    subject = 'Mail Subject/Title'

    # Create a MIME object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Add a text part (description/content) to the email
    email_content = """Hello,

Please find the attached PDF file for your reference.

Regards,
Your Name
"""
    msg.attach(MIMEText(email_content, 'plain'))  # 'plain' indicates plain text content

    # Attach the PDF file
    SendFile = 'Your File.pdf'
    with open(SendFile, 'rb') as pdf_file:
        pdf_attachment = MIMEApplication(pdf_file.read(), _subtype="pdf")
        pdf_attachment.add_header('content-disposition', 'attachment', filename=SendFile)
    msg.attach(pdf_attachment)

    # Connect to the SMTP server and send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully.\t Date:", datetime.now())
    except Exception as e:
        print(f"Email could not be sent. Error: {str(e)}")


# Schedule the email to be sent daily at a specific time (e.g., 19:00 "7:00 PM")
schedule.every().day.at("19:00").do(send_email)

# Run the scheduler indefinitely
while True:
    schedule.run_pending()
    time.sleep(1)
