import smtplib
import requests

from conf import EMAIL_RECEIVER , MAILGUN_APIKEY

from email.mime.text import MIMEText


def send_api_email(subject, body):
    return requests.post(
        "https://api.mailgun.net/v3/inprobes/messages",
        auth=("api", MAILGUN_APIKEY),
        data={
            "from": "CHECK MAIL GUN DOCS",
            "to": ["CHECK DOCS", "CHECK DOCS"],
            "subject": subject,
            "text": body
        }
    )


def send_smtp_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "CHECK MAILGUN DOCS"
    msg['To'] = EMAIL_RECEIVER

    with smtplib.SMTP('smtp.mailgun.org', 587) as mail_server:
        mail_server.login('***********', MAILGUN_APIKEY)
        mail_server.sendmail(msg['From'], msg['To'], msg.as_string())
        # mail_server.quit()
