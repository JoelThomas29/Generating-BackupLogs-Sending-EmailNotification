""" Connects to the SMTP server and sends an email notification to the address as set in this program.
    The notifcation sent displays the difference of the currently generated log file with that of the file from the previous day, obtained from storing_result.py """

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import store_result 

def email():
	# sender and recepient email address
	fromaddr = 'email_address'
	toaddr = 'email_address'
	
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = 'Your Daily Configuration logs'
	msg.attach(MIMEText(store_result.difference, 'html'))
	
	# Connecting to Gmail SMTP server at port 587 (for TLS) and 465 (for SSL)
	server = smtplib.SMTP('smtp.gmail.com', 587)

	# Starting TLS encryption for security
	server.starttls()
	
	# Logging into Gmail and sending e-mail
	server.login('username', 'password')
	server.sendmail(fromaddr, toaddr, msg.as_string())
	server.quit()

