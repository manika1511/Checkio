import sendgrid
from sendgrid.helpers.mail import Email, Mail, Content
import ssl
import os

ssl._create_default_https_context = ssl._create_unverified_context

API_KEY = 'SENDGRID_API_KEY'
SUBJECT = 'Welcome'
BODY = 'Hi {}'

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get(API_KEY))

def send_email(email, name):
    from_email = Email('from email')
    to_email = Email(email)
    subject = SUBJECT
    content = Content("text/plain", "Hi " + name)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    send_email('somebody@gmail.com', 'Some Body')
    print('Done')

