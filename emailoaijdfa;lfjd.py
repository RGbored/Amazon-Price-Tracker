import smtplib
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("testingggg2002@gmail.com", "testing2002")
server.sendmail("testingggg2002@gmail.com", "rgbored2002@gmail.com", "Hello How do you do?")
server.quit()