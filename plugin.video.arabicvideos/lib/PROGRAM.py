# -*- coding: utf-8 -*-
from LIBRARY import *

def MAIN(mode,text):
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
		search = KEYBOARD('Write a message   اكتب رسالة')
		if search == '': return
		message = search
		subject = 'Message: From Arabic Videos'
		result = SEND_EMAIL(subject,message,'yes','')

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
		#idCode = xbmc.getInfoLabel( "System.AddonVersion(plugin.video.arabicvideos)" )
		var1 = dummyClientID()
		var2 = ''
		#xbmcgui.Dialog().ok(var2,var1)
		html = openURL('http://emademad.com/testtest.html')
		xbmcgui.Dialog().ok(html,html)
		
		
		#scriptNAME = os.path.basename(__file__).split('.')[0]
		#xbmcgui.Dialog().ok(scriptNAME,'')
		#url = ''
		#play_item = xbmcgui.ListItem(path=url)
		#xbmcplugin.setResolvedUrl(addon_handle, True, play_item)
		#return

