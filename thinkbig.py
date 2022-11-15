import smtplib #simple mail transfer protocol
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#mime-->MultiPurpose Internet Mail Extension
#defining data
email_user="sirichalla2003@gmail.com"
email_sender="206834@siddharthamahila.ac.in"
subject="Here this is your domain mail please dnt use for other purposes."
msg=MIMEMultipart()
msg['From']=email_user
msg['To']=email_sender
msg['Subject']=subject
body=""
msg.attach(MIMEText(body,'plain'))
text=msg.as_string()
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()#transport layer

#next login to the server
server.login(email_user,"kqiduhgbmbsxczmc")#give your gmail user name and pwd

#send the mail

#message from the headers
server.sendmail(email_user,email_sender,text)
server.quit()

