# -*- coding: utf-8 -*-
from LIBRARY import *
import urllib


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
		message1 = '1.   If you can\'t see Arabic Letters then go to "Kodi Interface Settings" and change the font to "Arial"'
		message2 = '2.   If you can\'t see "Arial" in kodi skin fonts then go to "Kodi Interface Settings" and change your skin to another skin that accepts "Arial" font'
		xbmcgui.Dialog().ok('Arabic Problem',message1)
		xbmcgui.Dialog().ok('Font Problem',message2)
		return

	elif mode==3:
		message1 = 'هذا الموقع بحاجة الى ربط مشفر حاول تنزيل شهادة التشفير على كودي او استخدم اصدار اخر لكودي  مثل اصدار 17.6'
		xbmcgui.Dialog().ok('المواقع المشفرة',message1)
		return

	elif mode==4:
		search =''
		keyboard = xbmc.Keyboard(search, 'Write a message   اكتب رسالة')
		keyboard.doModal()
		if keyboard.isConfirmed(): search = keyboard.getText()
		if len(search)<2:
			xbmcgui.Dialog().ok('غير مقبول. اعد المحاولة.','Not acceptable. Try again.')
 			return
		message = mixARABIC(search)
		yes = xbmcgui.Dialog().yesno('هل ترسل هذه الرسالة',message)
		if yes: 
			url = 'http://emadmahdi.pythonanywhere.com/sendemail'
			payload = {'message' : quote(message), 'subject' : 'From Arabic Videos' }
			data = urllib.urlencode(payload)
			html = openURL(url,data)
			result = html[0:6]
			if result != 'Error ':
				xbmcgui.Dialog().ok('تم الارسال','')

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

	elif mode==5:
		yes = xbmcgui.Dialog().yesno('الحل هو اخبار المبرمج بالتفاصيل','هل تريد اخبار المبرمج الان ؟')	
		if yes: MAIN(4,'')
		return

	elif mode==9:
		url = ''
		play_item = xbmcgui.ListItem(path=url)
		xbmcplugin.setResolvedUrl(addon_handle, True, play_item)
		return

