import smtplib


def alert_email(message):
    text = f"Subject: Low Stock Alert\n\n {message}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    # server.login("", "")  # email password
    # server.sendmail("", "", text)  # sending email, receiving email
