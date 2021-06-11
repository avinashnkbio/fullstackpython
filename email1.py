import smtplib
  
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("youremail", "yourpassword")
  
msg = "FIRST EMAIL USING PYTHON!"
server.sendmail("youremail", "email-of-receiver", msg)
server.quit()
print("Email Sent")