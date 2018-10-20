# -*- coding: utf-8 -*-
from LIBRARY import *

website0a = 'https://www.halacima.net'
script_name='HALACIMA'

def MAIN(mode,url,page):
	if mode==80: MENU()
	elif mode==81: ITEMS(url)
	elif mode==82: PLAY(url)
	elif mode==83: SEARCH()
	elif mode==84: ITEMS('','','lastRecent',page)
	elif mode==85: ITEMS('','','pin',page)
	elif mode==86: ITEMS('','','views',page)
	return

def MENU():
	addDir('بحث في الموقع','',83)
	addDir('جديد المسلسلات','',84,icon,0)
	addDir('افلام ومسلسلات مميزة','',85,icon,0)
	addDir('الاكثر مشاهدة','',86,icon,0)
	html = openURL(website0a,'','','','HALACIMA-MENU-1st')
	html_blocks = re.findall('dropdown(.*?)nav',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('<a href="(.*?)".*?>(.*?)<',block,re.DOTALL)
	#xbmcgui.Dialog().ok(block,str(items))
	ignoreLIST = ['مسلسلات انمي']
	for link,title in items:
		title = title.strip(' ')
		if not any(value in title for value in ignoreLIST):
			addDir(title,link,81)
	xbmcplugin.endOfDirectory(addon_handle)
	return

def ITEMS(url,html='',type='',page=0):
	if type=='':
		if html=='':
			html = openURL(url,'','','','HALACIMA-ITEMS-1st')
		html_blocks = re.findall('art_list(.*?)col-md-12',html,re.DOTALL)
		block = html_blocks[0]
	else:
		if page==0: url = website0a + '/ajax/getItem'
		else: url = website0a + '/ajax/loadMore'
		headers = { 'Content-Type' : 'application/x-www-form-urlencoded' }
		payload = { 'Ajax' : '1' , 'item' : type , 'offset' : page*50 }
		data = urllib.urlencode(payload)
		block = openURL(url,data,headers,'','HALACIMA-ITEMS-2nd')
	items = re.findall('href="(.*?)".*?data-src="(.*?)".*?class="desc">(.*?)<',block,re.DOTALL)
	allTitles = []
	for link,img,title in items:
		title = title.replace('\n','')
		title = title.strip(' ')
		if 'الحلقة' in title and '/article/' not in link:
			episode = re.findall(' الحلقة [0-9]*',title,re.DOTALL)
			if episode:
				title = title.replace(episode[0],'')
		title = unescapeHTML(title)
		if title not in allTitles:
			allTitles.append(title)
			if '/article/' in link:
				addLink(title,link,82,img)
			else:
				addDir(title,link,81,img)
	html_blocks = re.findall('pagination(.*?)</div>',html,re.DOTALL)
	if html_blocks:
		block = html_blocks[0]
		items = re.findall('<li><a href="(.*?)".*?>(.*?)<',block,re.DOTALL)
		for link,title in items:
			title = title.replace('الصفحة ','')
			addDir('صفحة '+title,link,81)
	if type=='lastRecent': addDir('صفحة المزيد','',84,icon,page+1)
	elif type=='pin': addDir('صفحة المزيد','',85,icon,page+1)
	elif type=='views': addDir('صفحة المزيد','',86,icon,page+1)
	xbmcplugin.endOfDirectory(addon_handle)
	return

def PLAY(url):
	linkLIST = []
	html = openURL(url,'','','','HALACIMA-PLAY-1st')
	html_blocks = re.findall('class="download(.*?)div',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('href="(.*?)"',block,re.DOTALL)
	for link in items:
		if 'http' not in link: link = 'http:' + link
		linkLIST.append(link)
	url = url.replace('/article/','/online/')
	html = openURL(url,'','','','HALACIMA-PLAY-2nd')
	html_blocks = re.findall('artId.*?(.*?)col-sm-12',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall(' = \'(.*?)\'',block,re.DOTALL)
	artID = items[0]
	url = website0a + '/ajax/getVideoPlayer'
	headers = { 'Content-Type' : 'application/x-www-form-urlencoded' }
	items = re.findall('getVideoPlayer\(\'(.*?)\'',block,re.DOTALL)
	for link in items:
		payload = { 'Ajax' : '1' , 'art' : artID , 'server' : link }
		data = urllib.urlencode(payload)
		html = openURL(url,data,headers,'','HALACIMA-PLAY-2nd')
		html = html.replace('SRC=','src=')
		links = re.findall('src=\'(.*?)\'',html,re.DOTALL)
		if 'http' not in link: link = 'http:' + link
		linkLIST.append(links[0])
	from RESOLVERS import PLAY as RESOLVERS_PLAY
	RESOLVERS_PLAY(linkLIST,script_name,'yes')
	return

def SEARCH():
	search = KEYBOARD()
	if search == '': return
	#search = search.replace(' ','+')
	url = website0a + '/search.html'
	headers = { 'Content-Type' : 'application/x-www-form-urlencoded' }
	payload = { 'name' : search , 'search' : 'البحث' }
	data = urllib.urlencode(payload)
	html = openURL(url,data,headers,'','HALACIMA-SEARCH-1st')
	if 'art_list' in html: ITEMS('',html)
	else: xbmcgui.Dialog().ok('no results','لا توجد نتائج للبحث')
	return



