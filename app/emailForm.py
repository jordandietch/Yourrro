import smtplib

def emailForm(form):
	to = 'emailgoeshere@gmail.com'
	gmail_user = 'emailgoeshere@gmail.com'
	gmail_pwd = 'passwordgoeshere'
	smtpserver = smtplib.SMTP("smtp.gmail.com",587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo
	smtpserver.login(gmail_user, gmail_pwd)
	header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:YOURRRO.COM Inquiry \n'
	msg = header + '\n This is a YOURRRO.COM inquiry from \n\n' + form.property_address.data + '\n\n' + form.email_address.data + '\n\n' + form.phone_number.data + '\n\n' + form.name.data
	smtpserver.sendmail(gmail_user, to, msg)
	smtpserver.close()