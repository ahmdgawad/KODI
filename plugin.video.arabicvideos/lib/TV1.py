# -*- coding: utf-8 -*-
from LIBRARY import *
import requests

script_name='TV1'
website0a = 'http://emadmahdi.pythonanywhere.com/listplay'

def MAIN(mode,url):
	if mode==100: ITEMS()
	elif mode==101: PLAY(url)

def ITEMS():
	itemsAll = []
	for id in ['a','b','c','d','e','f']:
		payload = { 'id' : id , 'userID' : dummyClientID() , 'functionID' : 'list' }
		data = urllib.urlencode(payload)
		html = openURL(website0a,data,'','','TV1-ITEMS-1st')
		html = html.replace('Al ','Al')
		items = re.findall('&ppoint=(.*?)_.*?src="(.*?)"/>(.*?)<',html,re.DOTALL)
		itemsAll += items
	itemsAll = set(itemsAll)
	itemsSorted = sorted(itemsAll, reverse=False, key=lambda key: key[2])
	if itemsSorted:
		for link,img,title in itemsSorted:
			addLink(title,link,101,img,'','no')
	else:
		addLink('للأسف القنوات لا تعمل على جهازك','',9999)
	xbmcplugin.endOfDirectory(addon_handle)

def PLAY(id):
	headers = { 'Content-Type' : 'application/x-www-form-urlencoded' }
	payload = { 'id' : id , 'userID' : dummyClientID() , 'functionID' : 'play' }
	response = requests.post(website0a, data=payload, headers=headers)
	html = response.text
	#xbmcgui.Dialog().ok(html,html)
	items = re.findall('link3":"(.*?)"',html,re.DOTALL)
	url = items[0]
	url = url.replace('\\','')
	PLAY_VIDEO(url,script_name,'no')


