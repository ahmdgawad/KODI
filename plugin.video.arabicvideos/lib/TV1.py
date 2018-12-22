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
	payload = { 'id' : id , 'userID' : client , 'functionID' : 'list' }
	data = urllib.urlencode(payload)
	html = openURL(website0a,data,'','','TV1-ITEMS-1st')
	html = html.replace('Al ','Al')
	html = html.replace('\r','')
	#xbmcgui.Dialog().ok(html,html)
	items = re.findall('(.*?):(.*?):(.*?)\n',html,re.DOTALL)
	if items:
		items = set(items)
		itemsSorted = sorted(items, reverse=False, key=lambda key: key[1].lower())
		for link,title,img in itemsSorted:
			addLink(title,link,101,img,'','yes')
	else:
		addLink('للأسف لا توجد قنوات تلفزونية لك','',9999)
		addLink('هذه الخدمة مخصصة للاقرباء والاصدقاء فقط','',9999)
		addLink('=========================','',9999)
		addLink('Unfortunately, no TV channels for you','',9999)
		addLink('It is for relatives & friends only','',9999)
	xbmcplugin.endOfDirectory(addon_handle)
	return

def PLAY(id):
	headers = { 'Content-Type' : 'application/x-www-form-urlencoded' }
	payload = { 'id' : id , 'userID' : dummyClientID(32) , 'functionID' : 'play' }
	from requests import request as requests_request
	response = requests_request('POST', website0a, data=payload, headers=headers)
	html = response.text
	#xbmcgui.Dialog().ok(html,html)
	items = re.findall('link3":"(.*?)"',html,re.DOTALL)
	url = items[0]
	url = url.replace('\/','/')
	url = url.replace('#','')
	#xbmcgui.Dialog().ok(url,id)
	PLAY_VIDEO(url,script_name,'yes')
	return


