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
			source = id[0:2]
			id = id[2:99]
			#if source=='NT': source = 'NileTC'
			title = title + ' ' + source
			title = title.replace('Al ','Al')
			title = title.replace('El ','El')
			addLink(title,source+id,101,img,'','no')
	elif html=='Not Allowed':
		addLink('للأسف لا توجد قنوات تلفزونية لك','',9999)
		addLink('هذه الخدمة مخصصة للاقرباء والاصدقاء فقط','',9999)
		addLink('=========================','',9999)
		addLink('Unfortunately, no TV channels for you','',9999)
		addLink('It is for relatives & friends only','',9999)
	xbmcplugin.endOfDirectory(addon_handle)
	return

def PLAY(id):
	source = id[0:2]
	id = id[2:99]
	from requests import request as requests_request
	if source=='HD' or source=='SD':
		headers = { 'Content-Type' : 'application/x-www-form-urlencoded' }
		payload = { 'id' : id , 'user' : dummyClientID(32) , 'function' : 'play1' }
		response = requests_request('POST', website0a, data=payload, headers=headers)
		html = response.text
		#xbmcgui.Dialog().ok(html,html)
		if source=='HD': link='3'
		else: link='2'
		items = re.findall('"link'+link+'":"(.*?)"',html,re.DOTALL)
		url = items[0]
		url = url.replace('\/','/')
		#url = url.replace('#','')
	elif source=='NT':
		headers = { 'Content-Type' : 'application/x-www-form-urlencoded' }
		payload = { 'id' : id , 'user' : dummyClientID(32) , 'function' : 'play2' }
		response = requests_request('POST', website0a, data=payload, headers=headers, allow_redirects=False)
		url = response.headers['Location']
		url = url.replace('%20',' ')
		url = url.replace('%3D','=')
		if 'Learn' in id:
			url = url.replace('NTNNile','')
			url = url.replace('learning1','Learning')
	elif source=='PL':
		headers = { 'Content-Type' : 'application/x-www-form-urlencoded' }
		payload = { 'id' : id , 'user' : dummyClientID(32) , 'function' : 'play3' }
		response = requests_request('POST', website0a, data=payload, headers=headers)
		response = requests_request('POST', response.headers['Location'], headers={'Referer':response.headers['Referer']})
		html = response.text
		#xbmcgui.Dialog().ok('',html)
		items = re.findall('source src="(.*?)"',html,re.DOTALL)
		url = items[0]
	#xbmcgui.Dialog().ok(url,'')
	PLAY_VIDEO(url,script_name,'no')
	return


