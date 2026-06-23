import smtplib
def alert_email(message):
    text = f"Subject: dsadsada \n\n {message}"

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()

   # server.login("","") email password
   # server.sendmail("","",text) email receving email

