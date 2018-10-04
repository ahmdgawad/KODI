# -*- coding: utf-8 -*-
from LIBRARY import *
import RESOLVERS

website0a = 'https://www.halacima.net'
script_name='HALACIMA'

def MAIN(mode,url):
	if mode==80: MENU()
	elif mode==81: ITEMS(url)
	elif mode==82: PLAY(url)
	elif mode==83: SEARCH()

def MENU():
	addDir('بحث في الموقع',website0a,83)
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

def ITEMS(url,html=''):
	if html=='': html = openURL(url,'','','','HALACIMA-ITEMS-1st')
	html_blocks = re.findall('art_list(.*?)col-md-12',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('href="(.*?)".*?data-src="(.*?)".*?class="desc">(.*?)<',block,re.DOTALL)
	allTitles = []
	for link,img,title in items:
		title = title.replace('\n','')
		title = title.strip(' ')
		if 'الحلقة' in title and '/series/' not in url:
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
	xbmcplugin.endOfDirectory(addon_handle)

def PLAY(url):
	urlLIST = []
	html = openURL(url,'','','','HALACIMA-PLAY-1st')
	html_blocks = re.findall('class="download(.*?)div',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('href="(.*?)"',block,re.DOTALL)
	for link in items:
		urlLIST.append(link)
	url = url.replace('/article/','/online/')
	html = openURL(url,'','','','HALACIMA-PLAY-2nd')
	html_blocks = re.findall('artId.*?(.*?)col-sm-12',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall(' = \'(.*?)\'',block,re.DOTALL)
	artID = items[0]
	#xbmcgui.Dialog().ok('',artID)
	url = website0a + '/ajax/getVideoPlayer'
	headers = { 'Content-Type' : 'application/x-www-form-urlencoded' }
	items = re.findall('getVideoPlayer\(\'(.*?)\'.*?href.*?server">(.*?)<',block,re.DOTALL)
	#xbmcgui.Dialog().ok(str(len(items)),'')
	for link,title in items:
		payload = { 'Ajax' : '1' , 'art' : artID , 'server' : link }
		data = urllib.urlencode(payload)
		html = openURL(url,data,headers,'','HALACIMA-PLAY-2nd')
		html = html.replace('SRC=','src=')
		#xbmcgui.Dialog().ok(link,html)
		links = re.findall('src=\'(.*?)\'',html,re.DOTALL)
		link = links[0]
		if 'http' not in link: 		link = 'http:' + link
		urlLIST.append(link)
	urlLIST = set(urlLIST)
	serversLIST = RESOLVERS.SERVERS(urlLIST)
	items_url = []
	items_name = []
	for i in range(1,len(serversLIST)):
		if serversLIST[i]!='':
			items_url.append(serversLIST[i])
			items_name.append('Server '+str(i))
	selection = xbmcgui.Dialog().select('Select Video Link:', items_name)
	if selection == -1 : return
	url = items_url[selection]
	url = RESOLVERS.VIDEO_URL(url)
	PLAY_VIDEO(url,script_name)
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


