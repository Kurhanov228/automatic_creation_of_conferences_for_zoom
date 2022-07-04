import smtplib
import os
from textwrap import dedent

def send(email_from, email_to, text, password):
    headers=f"""From: {email_from}
To: {email_to}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

    """
    final_letter = headers + text
    final_letter = final_letter.encode("UTF-8")
    server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
    server.login(email_from,password)
    server.sendmail(email_from, email_to, final_letter)
    server.quit()
