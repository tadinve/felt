import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
#Next, log in to the server
server.login("chanchadsahil7@gmail.com", "S9879465512s@")

#Send the mail
msg = "Hello!" # The /n separates the message from the headers
server.sendmail("chanchadsahil7@gmail.com", "chanchadsahil@gmail.com", msg)