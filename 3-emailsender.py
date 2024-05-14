import smtplib

to = input("Enter the email of recipient : \n")

content = input("Enter the content for mail : \n")

def sendEmail(to,content):
  server = smtplib.SMTP('smtp.gmail.com',587)
  server.ehlo()
  server.starttls()
  server.login('zorana494@fthcapital.com','2)u?UEK](n')
  server.sendmail('zorana494@fthcapital.com',to,content)
  server.close()

sendEmail(to,content)
