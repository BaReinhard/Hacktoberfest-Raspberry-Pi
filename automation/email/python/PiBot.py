#send email from script (you need an account gmail)

#!/usr/bin/python
import sys
import smtplib

text="I am a Raspberry Pi"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.login("YourEmail", "YourPassword")
server.sendmail("YourEmail", "RecipientEmail", text)
server.quit()
print 'Email sent!'

