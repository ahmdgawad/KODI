# -*- coding: utf-8 -*-
from LIBRARY import *

website0a = 'http://alfatimi.tv'
script_name = 'ALFATIMI'

def MAIN(mode,url,category):
	if mode==60: MENU()
	elif mode==61: TITLES(url,category)
	elif mode==62: EPISODES(url)
	elif mode==63: PLAY(url)
	elif mode==64: SEARCH()
	elif mode==65: MOSTS(category)
	return

def MENU():
	addDir('بحث في الموقع','',64)
	addDir('ما يتم مشاهدته الان',website0a,65,icon,'',1)
	addDir('الاكثر مشاهدة',website0a,65,icon,'',2)
	addDir('اضيفت مؤخرا',website0a,65,icon,'',3)
	addDir('فيديو عشوائي',website0a,65,icon,'',4)
	addDir('افلام ومسلسلات',website0a,61,icon,'',-1)
	addDir('البرامج الدينية',website0a,61,icon,'',-2)
	addDir('English Videos',website0a,61,icon,'',-3)
	#TITLES(website0a,'-2')
	xbmcplugin.endOfDirectory(addon_handle)
	return

def TITLES(url,category):
	#xbmcgui.Dialog().ok('', category)
	moviesLIST = ['1239','1250','1245','20','1259','218','485','1238','1258','292']
	englishLIST = ['3030','628']
	if category in ['-1','-2','-3']:
		html = openURL(website0a+'/menu_level.php','','','','ALFATIMI-TITLES-1st')
	else:
		html = openURL(website0a+'/menu_level.php?cat='+category,'','','','ALFATIMI-TITLES-2nd')
	items = re.findall('href=\'(.*?)\'.*?>(.*?)<.*?>(.*?)</span>',html,re.DOTALL)
	startADD = False
	for link,title,count in items:
		cat = re.findall('cat=(.*?)&',link,re.DOTALL)[0]
		title = unescapeHTML(title)
		titleCAT = '[[ ' + title + ' ]]'
		if category=='-1':
			if cat in moviesLIST:
				addDir(titleCAT,website0a,61,icon,'',cat)
		elif category=='-2':
			if cat not in moviesLIST and cat not in englishLIST:
				addDir(titleCAT,website0a,61,icon,'',cat)
		elif category=='-3':
			if cat in englishLIST:
				addDir(titleCAT,website0a,61,icon,'',cat)
		elif startADD==False:
			if category==cat: startADD = True
		elif count=='1':
			if 'http' not in link: link = 'http:'+link
			addLink(title,link,63)
		else: addDir(titleCAT,website0a,61,icon,'',cat)
	if category not in ['-1','-2','-3']:
		EPISODES(website0a+'/videos.php?cat='+category)
	xbmcplugin.endOfDirectory(addon_handle)
	return

def EPISODES(url):
	#xbmcgui.Dialog().ok(url , url)
	html = openURL(url,'','','','ALFATIMI-EPISODES-1st')
	html_blocks = re.findall('pagination(.*?)pagination',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('grid_view.*?src="(.*?)".*?<h2.*?href="(.*?)">(.*?)<',block,re.DOTALL)
	link = ''
	for img,link,title in items:
		if 'http' not in link: link = 'http:'+link
		addLink(title,link,63,img)
	html_blocks=re.findall('(.*?)div',block,re.DOTALL)
	block=html_blocks[0]
	items=re.findall('href="(.*?)".*?>(.*?)<',block,re.DOTALL)
	for link,page in items:
		link = website0a + '/videos.php' + link
		title = unescapeHTML(page)
		title = 'صفحة ' + title
		vars = re.findall('cat=(.*?)&page=(.*?)nnn',link+'nnn',re.DOTALL)
		category = vars[0][0]
		page = vars[0][1]
		#xbmcgui.Dialog().ok(category, page)
		if page=='1':
			addDir(title,website0a,61,icon,'',category)
		else: addDir(title,link,62)
	if 'page' in url: xbmcplugin.endOfDirectory(addon_handle)
	return link

def PLAY(url):
	if 'videos.php' in url:
		url = EPISODES(url)
	html = openURL(url,'','','','ALFATIMI-PLAY-1st')
	items = re.findall('playlistfile:"(.*?)"',html,re.DOTALL)
	url = items[0]
	if 'http' not in url: url = 'http:'+url
	#xbmcgui.Dialog().ok(url,'')
	PLAY_VIDEO(url,script_name)
	return

def SEARCH():
	search = KEYBOARD()
	if search == '': return
	new_search = search.replace(' ','+')
	url = website0a + '/search_result.php?query=' + new_search
	html = openURL(url,'','','','ALFATIMI-SEARCH-1st')
	html_blocks = re.findall('search_subs(.*?)</ul>',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('cat=(.*?)&.*?>(.*?)<',block,re.DOTALL)
	for category,title in items:
		addDir(title,website0a,61,icon,'',category)
	xbmcplugin.endOfDirectory(addon_handle)
	return

def MOSTS(category):
	if   category=='1': payload = { 'mode' : 'recent_viewed_vids' }
	elif category=='2': payload = { 'mode' : 'most_viewed_vids' }
	elif category=='3': payload = { 'mode' : 'recently_added_vids' }
	elif category=='4': payload = { 'mode' : 'random_vids' }
	url = 'http://alfatimi.tv/ajax.php'
	headers = { 'Content-Type' : 'application/x-www-form-urlencoded' }
	data = urllib.urlencode(payload)
	html = openURL(url,data,headers,'','ALFATIMI-GROUPS-1st')
	items = re.findall('href="(.*?)".*?title="(.*?)".*?src="(.*?)".*?href',html,re.DOTALL)
	for link,title,img in items:
		title = title.strip(' ')
		if 'http' not in link: link = 'http:'+link
		addLink(title,link,63,img)
	xbmcplugin.endOfDirectory(addon_handle)
	return



