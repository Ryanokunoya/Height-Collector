import smtplib
from email.mime.text import MIMEText


def send_email(email, height, average_height, count):
    from_email = "felixzhu47@gmail.com"
    from_password = "Ryan0407"
    to_email = email

    subject = "Height data"
    message = "Hello, your height is <strong>%s</strong>. Average height of all is <strong><em>%s</em></strong> and that is calculated out <strong>%s</strong> of people" % (
        height, average_height, count)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
