# -*- coding: utf-8 -*-
from LIBRARY import *

website0a = 'http://www.almaareftv.com'
script_name = 'ALMAAREF'

def MAIN(mode,url,category):
	if mode==40: MENU()
	elif mode==41: SEARCH()
	elif mode==42: EPISODES(url)
	elif mode==43: PLAY(url)
	elif mode==44: CATEGORIES(url,category)
	elif mode==45: TITLES(url,1)
	elif mode==46: TITLES(url,2)
	elif mode==47: TITLES(url,3)
	elif mode==48: PROGRAMS()

def MENU():
	addDir('بحث في الموقع','',41,icon)
	addDir('برامج القناة','',48,icon)
	html = openURL(website0a,'','','','ALMAAREF-MENU-1st')
	items = re.findall('<h2><a href="(.*?)">(.*?)</a></h2>',html,re.DOTALL)
	for link,name in items:
		addDir(name,link,47,icon)
	name = re.findall('recent-default.*?<h2>(.*?)</h2>',html,re.DOTALL)
	if name:
		addDir(name[0],website0a,46,icon)
	name = re.findall('categories"><div class="widget-top"><h4>(.*?)</h4>',html,re.DOTALL)
	if name:
		addDir(name[0],website0a,44,icon,'','0')
	xbmcplugin.endOfDirectory(addon_handle)

def TITLES(url,select):
	notvideosLIST = ['تطبيقات الاجهزة الذكية','جدول البرامج','اوقات برامجنا']
	html = openURL(url,'','','','ALMAAREF-TITLES-1st')
	if select==1:
		html_blocks1=re.findall('main-content(.*?)class="clear"',html,re.DOTALL)
		if html_blocks1:
			block = html_blocks1[1]
	elif select==2:
		html_blocks2=re.findall('recent-default(.*?)class="clear"',html,re.DOTALL)
		if html_blocks2:
			block = html_blocks2[0]
	if select<=2 and block:
		items=re.findall('src="(.*?)".*?href="(.*?)" rel="bookmark">(.*?)<',block,re.DOTALL)
		for img,url,title in items:
			if not any(value in title for value in notvideosLIST):
				title = unescapeHTML(title)
				addDir(title,url,42,img)
	if select==3:
		html_blocks3=re.findall('archive-box(.*?)script',html,re.DOTALL)
		if html_blocks3:
			block = html_blocks3[0]
			items=re.findall('h2.*?href="(.*?)">(.*?)<.*?src="(.*?)"',block,re.DOTALL)
			for url,title,img in items:
				if not any(value in title for value in notvideosLIST):
					title = unescapeHTML(title)
					addDir(title,url,42,img)
	if select>=2:
		html_blocks4=re.findall('class="pagination"(.*?)<h',html,re.DOTALL)
		if html_blocks4:
			block = html_blocks4[0]
			items=re.findall('href="(.*?)".*?title="(.*?)"',block,re.DOTALL)
			for url,title in items:
				title = unescapeHTML(title)
				title = 'صفحة ' + title
				if select==2: addDir(title,url,46,'')
				else: addDir(title,url,47,'')
	xbmcplugin.endOfDirectory(addon_handle)

def EPISODES(url):
	html = openURL(url,'','','','ALMAAREF-EPISODES-1st')
	html_blocks=re.findall('entry-title"><span itemprop="name">(.*?)<',html,re.DOTALL)
	name = html_blocks[0]
	name = unescapeHTML(name)
	html_blocks=re.findall('wp-playlist-script(.*?).entry',html,re.DOTALL)
	if html_blocks:
		block = html_blocks[0]
		items=re.findall('src":"(.*?)".*?title":"(.*?)".*?meta":(.*?),.*?image":{"src":"(.*?)".*?thumb":{"src":"(.*?)"',block,re.DOTALL)
		for link,title,meta,img1,img2 in items:
			img1 = img1.replace('\/','/')
			img2 = img2.replace('\/','/')
			link = link.replace('\/','/')
			title = escapeUNICODE(title)
			link = escapeUNICODE(link)
			title = title.split(' ')[-1]
			title = name + ' - ' + title
			duration = re.findall('length_formatted":"(.*?)"',meta,re.DOTALL)
			if duration: addLink(title,link,43,img2,duration[0])
			else: addLink(title,link,43,img2)
	else:
		items=re.findall('itemprop="name">(.*?)<.*?contentUrl" content="(.*?)".*?image.*?url":"(.*?)"',html,re.DOTALL)
		for title,link,img in items:
			img = img.replace('\/','/')
			title = escapeUNICODE(title)
			link = escapeUNICODE(link)
			addLink(title,link,43,img)
		#PLAY_FROM_DIRECTORY(url)
	xbmcplugin.endOfDirectory(addon_handle)

def PLAY(url):
	url = url.replace(' ','%20')
	PLAY_VIDEO(url,script_name)

def CATEGORIES(url,category):
	#xbmcgui.Dialog().ok(type, url)
	html = openURL(url,'','','','ALMAAREF-CATEGORIES-1st')
	html_blocks=re.findall('cat1.a\(0,(.*?)document.write',html,re.DOTALL)
	block= html_blocks[0]
	items=re.findall('cat1.a\((.*?),(.*?),\'(.*?)\',\'\',\'(.*?)\'',block,re.DOTALL)
	exist=False
	notvideosLIST = ['-399','5643','2306','5654','10716','10277','7946']
	for cat,parent,title,link in items:
		if parent == category and cat not in notvideosLIST:
			title = unescapeHTML(title)
			url = website0a + '/' + link
			if cat == '-165': title = 'السيد صباح شبر (60)'
			if '-' in cat: addDir(title,url,44,icon,'',cat)
			else: addDir(title,url,42,icon)
			exist=True
	if exist: xbmcplugin.endOfDirectory(addon_handle)
	else: TITLES(url,3)
	
def SEARCH():
	search = KEYBOARD()
	if search == '': return
	new_search = search.replace(' ','%20')
	url = website0a + '/?s=' + new_search
	TITLES(url,3)

def PROGRAMS():
	#xbmcgui.Dialog().ok(type, url)
	html = openURL(website0a,'','','','ALMAAREF-PROGRAMS-1st')
	html_blocks=re.findall('mega-menu-block(.*?)mega-menu',html,re.DOTALL)
	block= html_blocks[0]
	items=re.findall('href="(.*?)">(.*?)<',block,re.DOTALL)
	for link,title in items:
		addDir(title,link,44,icon)
	xbmcplugin.endOfDirectory(addon_handle)

