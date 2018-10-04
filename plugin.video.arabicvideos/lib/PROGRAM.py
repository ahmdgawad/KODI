# -*- coding: utf-8 -*-
from LIBRARY import *

script_name='PROGRAM'

def MAIN(mode,text=''):
	if (mode==0 or mode==1):
		keyboard=text
		if keyboard=='': return
		if mode==1:
			window_id = xbmcgui.getCurrentWindowDialogId()
			window = xbmcgui.Window(window_id)
			keyboard = mixARABIC(keyboard)
			window.getControl(311).setLabel(keyboard)
		elif mode==0:
			ttype='X'
			check=isinstance(keyboard, unicode)
			if check==True: ttype='U'
			new1=str(type(keyboard))+' '+keyboard+' '+ttype+' '
			for i in range(0,len(keyboard),1):
				new1 += hex(ord(keyboard[i])).replace('0x','')+' '
			keyboard = mixARABIC(keyboard)
			ttype='X'
			check=isinstance(keyboard, unicode)
			if check==True: ttype='U'
			new2=str(type(keyboard))+' '+keyboard+' '+ttype+' '
			for i in range(0,len(keyboard),1):
				new2 += hex(ord(keyboard[i])).replace('0x','')+' '
			xbmcgui.Dialog().ok(new1,new2)
		return

	elif mode==2:
		xbmcgui.Dialog().ok('المبرمج لا يعلم الغيب','اذا كانت لديك مشكلة فاذن أقرأ قسم المشاكل والحلول واذا لم تجد الحل هناك فاذن اكتب رسالة عن المكان والوقت والحال الذي تحدث فيه المشكلة واكتب جميع التفاصيل لان المبرمج لا يعلم الغيب')
		xbmcgui.Dialog().ok('عنوان الايميل','اذا كنت تريد ان تسأل وتحتاج جواب من المبرمج فاذن يجب عليك اضافة عنوان البريد الالكتروني email الخاص بك الى رسالتك لانها الطريقة الوحيدة للوصول اليك')
		search = KEYBOARD('Write a message   اكتب رسالة')
		if search == '': return
		message = search
		subject = 'Message: From Arabic Videos'
		result = SEND_EMAIL(subject,message,'yes','','EMAIL-FROM-USERS')

		#	url = 'my API and/or SMTP server'
		#	payload = '{"api_key":"MY API KEY","to":["me@email.com"],"sender":"me@email.com","subject":"From Arabic Videos","text_body":"'+message+'"}'
		#	#auth=("api", "my personal api key"),
		#	#response = requests.request('POST',url, data=payload, headers='', auth='')
		#	response = requests.post(url, data=payload, headers='', auth='')
		#	if response.status_code == 200:
		#		xbmcgui.Dialog().ok('تم الارسال بنجاح','')
		#	else:
		#		xbmcgui.Dialog().ok('خطأ في الارسال','Error {}: {!r}'.format(response.status_code, response.content))

		#	FROMemailAddress = 'me@email.com'
		#	TOemailAddress = 'me@email.com'
		#	header = ''
		#	#header += 'From: ' + FROMemailAddress
		#	#header += '\nTo: ' + emailAddress
		#	#header += '\nCc: ' + emailAddress
		#	header += '\nSubject: من كودي الفيديو العربي'
		#	server = smtplib.SMTP('smtp-server',25)
		#	#server.starttls()
		#	server.login('username','password')
		#	response = server.sendmail(FROMemailAddress,TOemailAddress, header + '\n' + message)
		#	server.quit()
		#	xbmcgui.Dialog().ok('Response',str(response))
		return

	elif mode==9:
		#html = openURL('http://thevideo.me/embed-w8svy75ojdvo.html','','','','PROGRAM-MAIN-1st')
		var1 = dummyClientID()
		xbmcgui.Dialog().ok(var1,'')
		#url = ''
		#PLAY_VIDEO(url,script_name)
		#scriptNAME = os.path.basename(__file__).split('.')[0]
		#xbmcgui.Dialog().ok(scriptNAME,'')
		#url = ''
		#play_item = xbmcgui.ListItem(path=url)
		#xbmcplugin.setResolvedUrl(addon_handle, True, play_item)
		#return

