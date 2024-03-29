import smtplib
import pandas
from datetime import datetime as dt
today = dt.today()
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
attachments = []

def send_email():
    print("sending emails")
    df = pandas.read_csv('contacts.csv')
    for index, row in df.iterrows():
        msg = MIMEMultipart()
        msg["Subject"] = "Open Jobs on Indeed.com"
        msg["From"] = "noreply@etteplan.com"
        msg["To"] = row['email']
        name = row['name']
        name_stripped = name.strip()

        # Add email body
        body = MIMEText(f"Hello {name_stripped}, here's attached files gererated by AJS-application. \nEmail generated by AJS/Etteplan.")
        msg.attach(body)

        # # Add attachments to be send the list below
        attachments = ['jobs.docx', 'jobs2.docx', 'filtered.json', 'formated.md']

        for attachment_path in attachments:
            with open(attachment_path, "rb") as file:
                attachment = MIMEApplication(file.read())
                attachment.add_header(
                    "Content-Disposition", "attachment", filename=attachment_path
                )
            msg.attach(attachment)
            
        # Actual server address and port            
        server = smtplib.SMTP("82.195.202.152", 25)  
        server.send_message(msg)
        server.quit()
        print(f"Email #{index} send!")

if __name__ == '__main__':
    send_email()