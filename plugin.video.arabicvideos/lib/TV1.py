# -*- coding: utf-8 -*-
from LIBRARY import *

script_name='TV1'
website0a = 'http://emadmahdi.pythonanywhere.com/listplay'

def MAIN(mode,url):
	if mode==100: ITEMS()
	elif mode==101: PLAY(url)
	return

def ITEMS():
	client = dummyClientID(32)
	payload = { 'id' : '' , 'user' : client , 'function' : 'list' }
	data = urllib.urlencode(payload)
	html = openURL(website0a,data,'','','TV1-ITEMS-1st')
	#html = html.replace('\r','')
	#xbmcgui.Dialog().ok(html,html)
	#file = open('s:/emad.html', 'w')
	#file.write(html)
	#file.close()
	items = re.findall('(.*?):(.*?):(.*?)\r\n',html,re.DOTALL)
	if items:
		items = set(items)
		itemsSorted = sorted(items, reverse=False, key=lambda key: key[0].lower())
		itemsSorted = sorted(itemsSorted, reverse=False, key=lambda key: key[1].lower())
		for id,title,img in itemsSorted:
			#xbmcgui.Dialog().ok(id,id)
			quality = id[0:2]
			id = id[2:99]
			title = title + ' ' + quality
			title = title.replace('Al ','Al')
			title = title.replace('El ','El')
			addLink(title,quality+id,101,img,'','yes')
	elif html=='Not Allowed':
		addLink('للأسف لا توجد قنوات تلفزونية لك','',9999)
		addLink('هذه الخدمة مخصصة للاقرباء والاصدقاء فقط','',9999)
		addLink('=========================','',9999)
		addLink('Unfortunately, no TV channels for you','',9999)
		addLink('It is for relatives & friends only','',9999)
	xbmcplugin.endOfDirectory(addon_handle)
	return

def PLAY(id):
	quality = id[0:2]
	id = id[2:99]
	#xbmcgui.Dialog().ok(quality,id)
	headers = { 'Content-Type' : 'application/x-www-form-urlencoded' }
	payload = { 'id' : id , 'user' : dummyClientID(32) , 'function' : 'play' }
	from requests import request as requests_request
	response = requests_request('POST', website0a, data=payload, headers=headers)
	html = response.text
	#xbmcgui.Dialog().ok(html,html)
	if quality=='HD': link='3'
	elif quality=='SD': link='2'
	else: link = '1'
	items = re.findall('"link'+link+'":"(.*?)"',html,re.DOTALL)
	url = items[0]
	url = url.replace('\/','/')
	#url = url.replace('#','')
	#xbmcgui.Dialog().ok(url,id)
	PLAY_VIDEO(url,script_name,'yes')
	return


