# Mail Scheduler

A mail scheduler program is a software tool designed to automatically send emails with attachements (e.g. PDF files) at specific times every day.

## Installation packages

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following packages.

```bash
pip install smtplib
pip install schedule
pip install email
pip install datetime
```

### Run the scheduler:
1. Clone the Repository:

- Run the following command to clone the repository:
```bash
git clone https://github.com/Mostafa-Medhat/Mails-Scheduler.git
```

2. Open the Python Script:

- Navigate into the cloned repository directory.
- Use any text editor or Integrated Development Environment (IDE) to open the mail_scheduler.py file.

- Change the Email Content:

Inside the mail_scheduler.py file, locate the section where the email content is defined.
Modify the content of the email, including the subject, body, recipient's email address, and any attachments if needed, to your desired values.
```python
# Add a text part (description/content) to the email
    email_content = """Hello,

Please find the attached PDF file for your reference.

Regards,
Your Name
"""
```

- Change/Remove Attached Files:

If you want to attach a file, make sure the file exists in the same directory as the Python script.
Update the file path in the script accordingly.
If you don't want to attach a file, you can remove or comment out the lines of code related to attaching a file.
```python
  # Attach the PDF file
    SendFile = 'Your File.pdf'
    with open(SendFile, 'rb') as pdf_file:
        pdf_attachment = MIMEApplication(pdf_file.read(), _subtype="pdf")
        pdf_attachment.add_header('content-disposition', 'attachment', filename=SendFile)
    msg.attach(pdf_attachment)
```

- Change Time Settings:
Modify the scheduled time by changing "19:00" to your desired time, following the format HH:MM (24-hour format).
```python
# Schedule the email to be sent daily at a specific time (e.g., 19:00 "7:00 PM")
schedule.every().day.at("19:00").do(send_email)
```
- Save the Changes.


3. Run the script:  
- Open Command Prompt in the the mail_scheduler directory and type the following command:

```bash
python mail_scheduler.py
```
- This command will execute the Python script, which will schedule and send the email according to the specified time settings.


### Future Version:
    Future versions of the mail scheduler will include a user interface (UI) instead of a script-based approach.
