# -*- coding: utf-8 -*-
from LIBRARY import *

website0a = 'https://egy.best'
headers = { 'User-Agent' : '' }
script_name = 'EGYBEST'
menu_name='[COLOR FFC89008]EGB [/COLOR]'

def MAIN(mode,url,page):
	if   mode==120: MAIN_MENU()
	elif mode==121: FILTERS_MENU(url)
	elif mode==122: TITLES(url,page)
	elif mode==123: PLAY(url)
	elif mode==124: SEARCH()
	elif mode==125: GET_USERNAME_PASSWORD()
	return

def MAIN_MENU():
	addDir(menu_name+'اضغط هنا لاضافة اسم دخول وكلمة السر','',125)
	addDir(menu_name+'بحث في الموقع','',124)
	html = openURL(website0a,'',headers,'','EGYBEST-MAIN_MENU-1st')
	#xbmcgui.Dialog().ok(website0a, html)
	html_blocks=re.findall('id="menu"(.*?)mainLoad',html,re.DOTALL)
	block = html_blocks[0]
	items=re.findall('a><a href="(.*?)".*?></i>(.*?)<',block,re.DOTALL)
	for url,title in reversed(items):
		addDir(menu_name+title,website0a+url,121)
	xbmcplugin.endOfDirectory(addon_handle)
	return

def FILTERS_MENU(link):
	filter = link.split('/')[-1]
	#xbmcgui.Dialog().ok(str(link), str(filter))
	if '/trending/' not in link:
		addDir(menu_name+'اظهار قائمة الفيديو التي تم اختيارها',link,122,'',1)
		addDir(menu_name+'[[   ' + filter.replace('-',' + ') + '   ]]',link,122,'',1)
		addDir(menu_name+'===========================',link,9999)
	html = openURL(link,'',headers,'','EGYBEST-FILTERS_MENU-1st')
	html_blocks=re.findall('mainLoad(.*?)</div></div>',html,re.DOTALL)
	if html_blocks:
		block = html_blocks[0]
		items=re.findall('href="(.*?)".*?</i> (.*?)<',block,re.DOTALL)
		for url,title in items:
			if '/movies/' in url and 'فلام' not in title: title = 'افلام ' + title
			elif '/tv/' in url and 'مسلسل' not in title: title = 'مسلسلات ' + title
			if '/trending/' in url:
				title = 'الاكثر مشاهدة ' + title
				addDir(menu_name+title,website0a+url,122,'',1)
			else:
				link = link.replace('popular','')
				link = link.replace('top','')
				link = link.replace('latest','')
				link = link.replace('new','')
				newfilter = url.split('/')[-1]
				url = link + '-' + newfilter
				url = url.replace('/-','/')
				url = url.rstrip('-')
				url = url.replace('--','-')
				addDir(menu_name+title,url,121)
	html_blocks=re.findall('sub_nav(.*?)</div></div></div>',html,re.DOTALL)
	if html_blocks:
		block = html_blocks[0]
		items=re.findall('href="(.*?)".*?>(.*?)<',block,re.DOTALL)
		for url,title in items:
			ignoreLIST = ['- الكل -','[R]']
			if any(value in title for value in ignoreLIST): continue
			if '/movies/' in url: title = 'افلام ' + title
			elif '/tv/' in url: title = 'مسلسلات ' + title
			addDir(menu_name+title,website0a+url,121)
	xbmcplugin.endOfDirectory(addon_handle)
	return

def TITLES(url,page):
	#xbmcgui.Dialog().ok(str(url), str(page))
	if '/explore/' in url or '?' in url: url2 = url + '&'
	else: url2 = url + '?'
	url2 = url2 + 'output_format=json&output_mode=movies_list&page='+str(page)
	html = openURL(url2,'',headers,'','EGYBEST-TITLES-1st')
	name = ''
	if '/season/' in url:
		name = re.findall('<h1>(.*?)<',html,re.DOTALL)
		if name: name = escapeUNICODE(name[0]).strip(' ') + ' - '
		else: name = xbmc.getInfoLabel( "ListItem.Label" ) + ' - '
		#xbmcgui.Dialog().ok(name, name)
	items = re.findall('n<a href=\\\\"(.*?)\\\\".*?src=\\\\"(.*?)\\\\".*?title\\\\">(.*?)<',html,re.DOTALL)
	for link,img,title in items:
		if '/series/' in url and '/season\/' not in link: continue
		if '/season/' in url and '/episode\/' not in link: continue
		title = name + escapeUNICODE(title).strip(' ')
		title = title.replace('\n','')
		link = link.replace('\/','/')
		img = img.replace('\/','/')
		if 'http' not in img: img = 'http:' + img
		#xbmcgui.Dialog().notification(img,'')
		url2 = website0a + link
		if '/movie/' in url2 or '/episode/' in url2:
			addLink(menu_name+title,url2.rstrip('/'),123,img)
		else:
			addDir(menu_name+title,url2,122,img,1)
	pagingLIST = ['/movies/','/tv/','/explore/','/trending/']
	if any(value in url for value in pagingLIST):
		for n in range(0,1000,100):
			if int(page/100)*100==n:
				for i in range(n,n+100,10):
					if int(page/10)*10==i:
						for j in range(i,i+10,1):
							if not page==j and j!=0:
								addDir(menu_name+'صفحة '+str(j),url,122,icon,j)
					elif i!=0: addDir(menu_name+'صفحة '+str(i),url,122,icon,i)
					else: addDir(menu_name+'صفحة '+str(1),url,122,icon,1)
			elif n!=0: addDir(menu_name+'صفحة '+str(n),url,122,icon,n)
			else: addDir(menu_name+'صفحة '+str(1),url,122,icon,1)
	xbmcplugin.endOfDirectory(addon_handle)
	return

def PLAY(url):
	#xbmcgui.Dialog().ok(url, url[-45:])
	headers = { 'User-Agent' : '' }
	html = openURL(url,'',headers,'','EGYBEST-PLAY-1st')
	rating = re.findall('<td>التصنيف</td>.*?">(.*?)<',html,re.DOTALL)
	if rating[0] in ['R','TVMA','TV-MA'       ,'PG-18','PG-16']:
		xbmcgui.Dialog().notification('الفيديو للكبار فقط','البرنامج لا يعرض هكذا افلام')
		return
	html_blocks = re.findall('tbody(.*?)tbody',html,re.DOTALL)
	if not html_blocks:
		xbmcgui.Dialog().notification('خطأ من الموقع الاصلي','ملف الفيديو غير متوفر')
		return
	block = html_blocks[0]
	items = re.findall('</td> <td>(.*?)<.*?data-call="(.*?)"',block,re.DOTALL)
	qualityLIST = []
	datacallLIST = []
	if len(items)>0:
		for qualtiy,datacall in items:
			qualityLIST.append ('mp4   '+qualtiy)
			datacallLIST.append (datacall)
	watchitem = re.findall('x-mpegURL" src="/api/\?call=(.*?)"',html,re.DOTALL)
	url = website0a + '/api?call=' + watchitem[0]
	EGUDI, EGUSID, EGUSS = GET_PLAY_TOKENS()
	if EGUDI=='':
		GET_USERNAME_PASSWORD()
		return
	headers = { 'User-Agent':'Googlebot/2.1 (+http)', 'Referer':'https://egy.best', 'Cookie':'EGUDI='+EGUDI+'; EGUSID='+EGUSID+'; EGUSS='+EGUSS }
	from requests import request as requests_request
	response = requests_request('GET', url, headers=headers, allow_redirects=False)
	html = response.text
	#xbmcgui.Dialog().ok(url,html)
	items = re.findall('#EXT-X-STREAM.*?RESOLUTION=(.*?),.*?\n(.*?)\n',html,re.DOTALL)
	if len(items)>0:
		for qualtiy,url in reversed(items):
			qualityLIST.append ('m3u8   '+qualtiy)
			datacallLIST.append (url)
	selection = xbmcgui.Dialog().select('اختر الفيديو المناسب:', qualityLIST)
	if selection == -1 : return
	url = datacallLIST[selection]
	if 'http' not in url:
		datacall = datacallLIST[selection]
		url = website0a + '/api?call=' + datacall
		headers = { 'User-Agent':'Googlebot/2.1 (+http)', 'Referer':'https://egy.best', 'Cookie':'EGUDI='+EGUDI+'; EGUSID='+EGUSID+'; EGUSS='+EGUSS }
		response = requests_request('GET', url, headers=headers, allow_redirects=False)
		html = response.text
		#xbmcgui.Dialog().ok(url,html)
		#xbmc.log(html, level=xbmc.LOGNOTICE)
		items = re.findall('"url":"(.*?)"',html,re.DOTALL)
		#datacall = items[0]

		#url = website0a + '/api?call=' + datacall
		#headers = { 'User-Agent':'Googlebot/2.1 (+http)', 'Referer':'https://egy.best', 'Cookie':'EGUDI='+EGUDI+'; EGUSID='+EGUSID+'; EGUSS='+EGUSS }
		#response = requests_request('GET', url, headers=headers, allow_redirects=False)
		#html = response.text
		#xbmc.log(escapeUNICODE(html), level=xbmc.LOGNOTICE)
		#items = re.findall('"url":"(.*?)"',html,re.DOTALL)
		url = items[0]

		#xbmcgui.Dialog().ok(url,html)
		#xbmc.log(html, level=xbmc.LOGNOTICE)
		#items = re.findall('"url":"(.*?)"',html,re.DOTALL)
		#url = items[0]
	url = url.replace('\/','/')
	#xbmc.log(url, level=xbmc.LOGNOTICE)
	#xbmcgui.Dialog().ok(url,url[-45:])
	PLAY_VIDEO(url,script_name,'yes')
	return

def SEARCH():
	search = KEYBOARD()
	if search == '': return
	new_search = search.replace(' ','+')
	url = website0a + '/explore/?q=' + new_search
	TITLES(url,1)
	return

def GET_USERNAME_PASSWORD():
	text = 'هذا الموقع يحتاج اسم دخول وكلمة السر لكي تستطيع تشغيل ملفات الفيديو. للحصول عليهم قم بفتح حساب مجاني من الموقع الاصلي'
	xbmcgui.Dialog().ok('الموقع الاصلي  http://egy.best',text)
	import xbmcaddon
	settings = xbmcaddon.Addon(id=addon_id)
	oldusername = settings.getSetting('egybest.user')
	oldpassword = settings.getSetting('egybest.pass')
	xbmc.executebuiltin('Addon.OpenSettings(%s)' %addon_id, True)
	newusername = settings.getSetting('egybest.user')
	newpassword = settings.getSetting('egybest.pass')
	if oldusername!=newusername or oldpassword!=newpassword:
		settings.setSetting('egybest.EGUDI','')
		settings.setSetting('egybest.EGUSID','')
		settings.setSetting('egybest.EGUSS','')
	return

def GET_PLAY_TOKENS():

	import xbmcaddon
	settings = xbmcaddon.Addon(id=addon_id)

	username = settings.getSetting('egybest.user')
	password = settings.getSetting('egybest.pass')
	if username=='' or password=='':
		settings.setSetting('egybest.EGUDI','')
		settings.setSetting('egybest.EGUSID','')
		settings.setSetting('egybest.EGUSS','')
		return ['','','']

	EGUDI = settings.getSetting('egybest.EGUDI')
	EGUSID = settings.getSetting('egybest.EGUSID')
	EGUSS = settings.getSetting('egybest.EGUSS')

	import requests

	if EGUDI!='':
		headers = { 'Cookie':'EGUDI='+EGUDI+'; EGUSID='+EGUSID+'; EGUSS='+EGUSS }
		response = requests.request('GET', website0a, headers=headers, allow_redirects=False)
		register = re.findall('ssl.egexa.com\/register',response.text,re.DOTALL)
		if register:
			settings.setSetting('egybest.EGUDI','')
			settings.setSetting('egybest.EGUSID','')
			settings.setSetting('egybest.EGUSS','')
		else:
			#xbmcgui.Dialog().ok('no new login needed, you were already logged in','')
			return [ EGUDI, EGUSID, EGUSS ]

	import random
	import string
	char_set = string.ascii_uppercase + string.digits + string.ascii_lowercase
	randomString = ''.join(random.sample(char_set*15, 15))

	url = "https://ssl.egexa.com/login/"
	payload = "------WebKitFormBoundary"+randomString+"\r\nContent-Disposition: form-data; name=\"ajax\"\r\n\r\n1\r\n------WebKitFormBoundary"+randomString+"\r\nContent-Disposition: form-data; name=\"do\"\r\n\r\nlogin\r\n------WebKitFormBoundary"+randomString+"\r\nContent-Disposition: form-data; name=\"email\"\r\n\r\n"+username+"\r\n------WebKitFormBoundary"+randomString+"\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n"+password+"\r\n------WebKitFormBoundary"+randomString+"\r\nContent-Disposition: form-data; name=\"valForm\"\r\n\r\n\r\n------WebKitFormBoundary"+randomString+"--"
	headers = {
	'Content-Type': "multipart/form-data; boundary=----WebKitFormBoundary"+randomString,
	#'Cookie': "PSSID="+PSSID+"; JS_TIMEZONE_OFFSET=18000",
	'Referer': 'https://ssl.egexa.com/login/?domain=egy.best&url=ref'
	}
	response = requests.request('POST', url, data=payload, headers=headers, allow_redirects=False)
	cookies = response.cookies.get_dict()
	if len(cookies)<3:
		xbmcgui.Dialog().ok('مشكلة في تسجيل الدخول للموقع','حاول اصلاح اسم الدخول وكلمة السر لكي تتمكن من تشغيل الفيديو بصورة صحيحة')
		return ['','','']

	EGUDI = cookies['EGUDI']
	EGUSID = cookies['EGUSID']
	EGUSS = cookies['EGUSS']
	xbmc.sleep(1000)
	url = "https://ssl.egexa.com/finish/"
	headers = { 'Cookie':'EGUDI='+EGUDI+'; EGUSID='+EGUSID+'; EGUSS='+EGUSS }
	response = requests.request('GET', url, headers=headers, allow_redirects=True)
	cookies = response.cookies.get_dict()
	#xbmcgui.Dialog().ok(str(response.text),str(cookies))
	EGUDI = cookies['EGUDI']
	EGUSID = cookies['EGUSID']
	EGUSS = cookies['EGUSS']
	settings.setSetting('egybest.EGUDI',EGUDI)
	settings.setSetting('egybest.EGUSID',EGUSID)
	settings.setSetting('egybest.EGUSS',EGUSS)
	#xbmcgui.Dialog().ok('success, you just logged in now','')
	return [ EGUDI, EGUSID, EGUSS ]




