# -*- coding: utf-8 -*-
import urllib2,xbmcplugin,xbmcgui,sys,xbmc,os,unicodedata,re,time
import urllib,HTMLParser,random

addon_handle = int(sys.argv[1])
addon_id = sys.argv[0].split('/')[2]
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))

def addLink(name,url,mode,iconimage=icon,duration='',isPlayable='yes'):
	if iconimage=='': iconimage=icon
	#xbmcgui.Dialog().ok(duration,'')
	u='plugin://'+addon_id+'/?mode='+str(mode)+'&url='+quote(url)
	liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
	liz.setProperty('fanart_image', fanart)
	liz.setInfo('Video', {'mediatype': 'video'})
	if duration != '' :
		if len(duration)<=2 : duration = '00:' + duration
		if len(duration)<=5 : duration = '00:' + duration
		duration = sum(x * int(t) for x, t in zip([3600,60,1], duration.split(":"))) 	
		liz.setInfo('Video', {'duration': duration})
	if isPlayable=='yes': liz.setProperty('IsPlayable', 'true')
	xbmcplugin.setContent(addon_handle, 'videos')
	xbmcplugin.addDirectoryItem(handle=addon_handle,url=u,listitem=liz,isFolder=False)
	return

def openURL(url,data='',headers='',showDialogs='',source=''):
	if showDialogs=='': showDialogs='yes'
	if data=='' and headers=='': request = urllib2.Request(url)
	elif data=='' and headers!='': request = urllib2.Request(url,headers=headers)
	elif data!='' and headers=='': request = urllib2.Request(url,data=data)
	elif data!='' and headers!='': request = urllib2.Request(url,headers=headers,data=data)
	html = ''
	code = '200'
	reason = 'OK'
	try:
		connection = urllib2.urlopen(request)
		html = connection.read()
		code = str(connection.code)
		connection.close
	except urllib2.HTTPError as error:
		code = str(error.code)
		reason = str(error.reason)
	except urllib2.URLError as error:
		code = str(error.reason[0])
		reason = str(error.reason[1])
	if code!='200':
		message = ''
		send = 'no'
		showDialogs = 'no'
		html = 'Error {}: {!r}'.format(code, reason)
		if 'google-analytics' in url:
			send = showDialogs
		if showDialogs=='yes':
			xbmcgui.Dialog().ok('خطأ في الاتصال',html)
			if code=='502' or code=='7':
				xbmcgui.Dialog().ok('Website is not available','لا يمكن الوصول الى الموقع والسبب قد يكون من جهازك او من الانترنيت الخاصة بك او من الموقع كونه مغلق للصيانة او التحديث لذا يرجى المحاولة لاحقا')
				send = 'no'
			elif code=='404':
				xbmcgui.Dialog().ok('File not found','الملف غير موجود والسبب غالبا هو من المصدر ومن الموقع الاصلي الذي يغذي هذا البرنامج')
			if send=='yes':
				yes = xbmcgui.Dialog().yesno('سؤال','هل تربد اضافة رسالة مع الخطأ لكي تشرح فيها كيف واين حصل الخطأ وترسل التفاصيل الى المبرمج ؟')
				if yes:
					message = ' \\n\\n' + KEYBOARD('Write a message   اكتب رسالة')
		if send=='yes':
			SEND_EMAIL('Error: From Arabic Videos',html+message,showDialogs,url,source)
	#xbmcgui.Dialog().ok('',source)
	#file = open('/data/emad.html', 'w')
	#file.write(url)
	#file.write('\n\n\n')
	#file.write(html)
	#file.close()
	return html

def quote(url):
	return urllib2.quote(url,':/')

def unquote(url):
	return urllib2.unquote(url)

def unescapeHTML(string):
	if '&' in string and ';' in string:
		string = string.decode('utf8')
		string = HTMLParser.HTMLParser().unescape(string)
		string = string.encode('utf8')
	return string

def escapeUNICODE(string):
	if '\u' in string:
		string = string.decode('unicode_escape')
		string = string.encode('utf8')
	return string

def addDir(name,url='',mode='',iconimage=icon,page='',category=''):
	if iconimage=='': iconimage=icon
	u='plugin://'+addon_id+'/?mode='+str(mode)
	if url != '' : u = u + '&url=' + quote(url)
	if page != '' : u = u + '&page=' + str(page)
	if category != '' : u = u + '&category=' + str(category)
	liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	liz.setProperty('fanart_image', fanart)
	#liz.setProperty('IsPlayable', 'true')
	xbmcplugin.addDirectoryItem(handle=addon_handle,url=u,listitem=liz,isFolder=True)
	return

def mixARABIC(string):
	#if '\u' in string:
	#	string = string.decode('unicode_escape')
	#	unicode_strings=re.findall(r'\u[0-9A-F]',string)	
	#	for unicode in unicode_strings
	#		char = unichar(
	#		replace(    , char)
	string = string.decode('utf8')
	new_string = ''
	for letter in string:
		#xbmcgui.Dialog().ok(unicodedata.decomposition(letter),hex(ord(letter)))
		if ord(letter) < 256: unicode_letter = '\u00'+hex(ord(letter)).replace('0x','')
		elif ord(letter) < 4096: unicode_letter = '\u0'+hex(ord(letter)).replace('0x','')
		else: unicode_letter = '\u'+unicodedata.decomposition(letter).split(' ')[1]
		new_string += unicode_letter
	new_string = new_string.replace('\u06CC','\u0649')
	new_string = new_string.decode('unicode_escape')
	new_string = new_string.encode('utf-8')
	return new_string

def KEYBOARD(label='Search'):
	search =''
	keyboard = xbmc.Keyboard(search, label)
	keyboard.doModal()
	if keyboard.isConfirmed(): search = keyboard.getText()
	search = search.strip(' ')
	if len(search.decode('utf8'))<2:
		xbmcgui.Dialog().ok('Wrong entry. Try again','خطأ في الادخال. أعد المحاولة')
		return ''
	new_search = mixARABIC(search)
	return new_search

def PLAY_VIDEO(url,label,showWatched='yes'):
	play_item = xbmcgui.ListItem(path=url)
	if showWatched=='yes':
		#xbmcgui.Dialog().ok(url,label)
		#title = xbmc.getInfoLabel('ListItem.Title')
		#title = xbmc.getInfoLabel('ListItem.Label')
		#play_item.setInfo( "video", { "Title": title } )
		xbmcplugin.setResolvedUrl(addon_handle, True, play_item)
	else:
		title = xbmc.getInfoLabel('ListItem.Label')
		play_item.setInfo( "video", { "Title": title } )
		xbmc.Player().play(url,play_item)
	addonVersion = xbmc.getInfoLabel( "System.AddonVersion(plugin.video.arabicvideos)" )
	randomNumber = str(random.randrange(111111111111,999999999999))
	url = 'http://www.google-analytics.com/collect?v=1&tid=UA-127045104-2&cid='+dummyClientID()+'&t=event&sc=end&ec='+addonVersion+'&av='+addonVersion+'&an=ARABIC_VIDEOS&ea='+label+'&z='+randomNumber
	openURL(url,'','','no','LIBRARY-PLAY_VIDEO-1st')
	return

def SEND_EMAIL(subject,message,showDialogs='yes',url='',source=''):
	yes = True
	html = ''
	if showDialogs=='yes':
		yes = xbmcgui.Dialog().yesno('هل ترسل هذه الرسالة الى المبرمج',message.replace('\\n','\n'))
	if yes:
		addonVersion = xbmc.getInfoLabel( "System.AddonVersion(plugin.video.arabicvideos)" )
		kodiVersion = xbmc.getInfoLabel( "System.BuildVersion" )	
		kodiName = xbmc.getInfoLabel( "System.FriendlyName" )
		message = message+' \\n\\n==== ==== ==== \\nAddon Version: '+addonVersion+' \\nEmail Sender: '+dummyClientID()+' \\nKodi Version: '+kodiVersion+' \\nKodi Name: '+kodiName
		#xbmc.sleep(4000)
		#playerTitle = xbmc.getInfoLabel( "Player.Title" )
		#playerPath = xbmc.getInfoLabel( "Player.Filenameandpath" )
		#if playerTitle != '': message += ' \\nPlayer Title: '+playerTitle
		#if playerPath != '': message += ' \\nPlayer Path: '+playerPath
		#xbmcgui.Dialog().ok(playerTitle,playerPath)
		if url != '': message += ' \\nURL: ' + url
		if source != '': message += ' \\nSource: ' + source
		url = 'http://emadmahdi.pythonanywhere.com/sendemail'
		payload = { 'subject' : quote(subject) , 'message' : quote(message) }
		data = urllib.urlencode(payload)
		html = openURL(url,data,'','','LIBRARY-SEND_EMAIL-1st')
		result = html[0:6]
		if showDialogs=='yes':
			if result == 'Error ':
				xbmcgui.Dialog().ok('Failed sending the message','خطأ وفشل في ارسال الرسالة')
			else:
				xbmcgui.Dialog().ok('Message sent','تم ارسال الرسالة')
	return html

def dummyClientID():
	#ipAddress = xbmc.getInfoLabel( "Network.IPAddress" )
	for i in range(0,6):
		hostName = xbmc.getInfoLabel( "System.FriendlyName" )
		if hostName!='Busy': break
		if i!=5: xbmc.sleep(500*pow(2,i))
	for j in range(0,6):
		macAddress = xbmc.getInfoLabel( "Network.MacAddress" )
		if macAddress!='Busy': break
		if j!=5: xbmc.sleep(500*pow(2,j))
	for k in range(0,6):
		osVersion = xbmc.getInfoLabel( "System.OSVersionInfo" )
		if osVersion!='Busy': break
		if k!=5: xbmc.sleep(500*pow(2,k))
	idComponents = macAddress + hostName + osVersion
	#idComponents = 'busykodilocalhostbusy' + 'a'
	idComponents1 = idComponents.lower().decode('utf8')
	listREMOVE1 = [' ',':','\.','\(','\)']
	idComponents2 = re.sub('|'.join(listREMOVE1), '', idComponents1)
	listREMOVE2 = ['kodi','localhost','android','api','level','kernel','linux','windows','nt','busy']
	idComponents3 = re.sub('|'.join(listREMOVE2), '', idComponents2)
	#xbmcgui.Dialog().ok(idComponents3,str(i)+'-'+str(j)+'-'+str(k))
	#idComponents3 = 'busybusy'
	length = len(idComponents3)
	result = ''
	if length>0:
		resultNumber = 1
		for i in range(0,length): resultNumber *= ord(idComponents3[i])
		resultText = str(resultNumber)
		middle = int(len(resultText)/2)
		start = middle - 10
		if start<0: start = 0
		result = resultText[start:start+20]
	if len(result)<20:
		length = len(result)
		result = '12345678901234567890'[0:20-length] + result
	return result


