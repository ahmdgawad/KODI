# -*- coding: utf-8 -*-
import urllib2,xbmcplugin,xbmcgui,sys,xbmc,os,unicodedata,re,time
import urllib,HTMLParser,random

addon_handle = int(sys.argv[1])
addon_id = sys.argv[0].split('/')[2]
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))

def addLink(name,url,mode,iconimage=icon,duration='',isPlayable='yes'):
	#xbmcgui.Dialog().ok(duration,'')
	u='plugin://'+addon_id+'/?mode='+str(mode)+'&url='+quote(url)
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
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

def openURL(url,data='',headers='',showDialogs='',source=''):
	if showDialogs=='': showDialogs='yes'
	#headers={ 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36' }
	#start = time.time()
	if data=='' and headers=='': request = urllib2.Request(url)
	elif data=='' and headers!='': request = urllib2.Request(url,headers=headers)
	elif data!='' and headers=='': request = urllib2.Request(url,data=data)
	elif data!='' and headers!='': request = urllib2.Request(url,headers=headers,data=data)
	#request.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	#request.add_header('Referer',' http://www.panet.co.il/Ext/players/flv5/player.swf')
	#request.add_header('Accept',' text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
	#request.add_header('Host',' fms-eu0.panet.co.il')
	#request.add_header('Accept-Language',' en-US,en;q=0.5')
	#request.add_header('Accept-Encoding', 'deflate')
	#request.add_header('Cookie',' __auc=82d7ffe213cb1b4ce1d273c7ba1; __utma=31848767.848342890.1360191082.1360611183.1360620657.4; __utmz=31848767.1360191082.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmb=31848767.4.10.1360620660; __utmc=31848767; __asc=169c084d13ccb4fa36df421055e')
	#request.add_header('Connection',' keep-alive')
	#request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36')
	#request.add_header('Connection', 'close')
	response = ''
	code = '200'
	reason = 'OK'
	try:
		connection = urllib2.urlopen(request)
		response = connection.read()
		code = str(connection.code)
		#xbmcgui.Dialog().ok(url,response)
		#end = time.time()
		#if end-start > 4 : xbmcgui.Dialog().notification('slower than 4 sec', str(end-start) )
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
		response = 'Error {}: {!r}'.format(code, reason)
		if 'google-analytics' in url:
			send = showDialogs
		if showDialogs=='yes':
			xbmcgui.Dialog().ok('خطأ في الاتصال',response)
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
			SEND_EMAIL('Error: From Arabic Videos',response+message,showDialogs,url,source)
	#xbmcgui.Dialog().ok('',source)
	#file = open('/data/emad.html', 'w')
	#file.write(url)
	#file.write('\n\n\n')
	#file.write(response)
	#file.close()
	return response

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
	u='plugin://'+addon_id+'/?mode='+str(mode)
	if url != '' : u = u + '&url=' + quote(url)
	if page != '' : u = u + '&page=' + str(page)
	if category != '' : u = u + '&category=' + str(category)
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	liz.setProperty('fanart_image', fanart)
	#liz.setProperty('IsPlayable', 'true')
	xbmcplugin.addDirectoryItem(handle=addon_handle,url=u,listitem=liz,isFolder=True)

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
		#title = xbmc.getInfoLabel('ListItem.Label')
		#play_item.setInfo( "video", { "Title": title } )
		xbmcplugin.setResolvedUrl(addon_handle, True, play_item)
	else:
		title = xbmc.getInfoLabel('ListItem.Label')
		play_item.setInfo( "video", { "Title": title } )
		xbmc.Player().play(url,play_item)
	addonVersion = xbmc.getInfoLabel( "System.AddonVersion(plugin.video.arabicvideos)" )
	randomNumber = str(random.randrange(111111111111,999999999999))
	url = 'http://www.google-analytics.com/collect?v=1&tid=UA-127045104-1&cid='+dummyClientID()+'&t=event&sc=end&ec='+addonVersion+'&av='+addonVersion+'&an=ARABIC_VIDEOS&ea='+label+'&z='+randomNumber
	openURL(url,'','','no','LIBRARY-PLAY_VIDEO-1st')

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
	hostName = xbmc.getInfoLabel( "System.FriendlyName" )
	#ipAddress = xbmc.getInfoLabel( "Network.IPAddress" )
	macAddress = xbmc.getInfoLabel( "Network.MacAddress" )
	xbmc.sleep(600)
	macAddress = xbmc.getInfoLabel( "Network.MacAddress" )
	osVersion = xbmc.getInfoLabel( "System.OSVersionInfo" )
	#idComponents = hostName + ipAddress + macAddress + osVersion
	idComponents = hostName + macAddress + osVersion
	length = len(idComponents)
	if length < 11: step = 1
	else: step = int(length/11)
	resultNumber = 1
	for i in range(0,length,step): resultNumber *= ord(idComponents[i])
	resultText = str(resultNumber)
	result = resultText[0:16]
	#xbmcgui.Dialog().ok(str(len(resultText)),str(step))
	return result


