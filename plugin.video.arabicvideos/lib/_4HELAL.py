# -*- coding: utf-8 -*-
from LIBRARY import *
import RESOLVERS

website0a = 'http://www.4helal.tv'
script_name='4HELAL'
headers = { 'User-Agent' : '' }

def MAIN(mode,url):
	if mode==90: MENU()
	elif mode==91: ITEMS(url)
	elif mode==92: PLAY(url)
	elif mode==93: SEARCH()

def MENU():
	addDir('بحث في الموقع',website0a,93)
	html = openURL(website0a,'',headers,'','4HELAL-MENU-1st')
	html_blocks = re.findall('mainmenu(.*?)nav',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('<li><a href="(.*?)".*?>(.*?)<',block,re.DOTALL)
	#xbmcgui.Dialog().ok(block,str(items))
	ignoreLIST = ['مسلسلات انمي']
	ignoreLIST = []
	for link,title in items:
		title = title.strip(' ')
		if not any(value in title for value in ignoreLIST):
			addDir(title,link,91)
	xbmcplugin.endOfDirectory(addon_handle)

def ITEMS(url,html=''):
	if html=='': html = openURL(url,'',headers,'','4HELAL-ITEMS-1st')
	html_blocks = re.findall('movies-items(.*?)class="clear',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('background-image:url\((.*?)\).*?href="(.*?)".*?movie-title">(.*?)<',block,re.DOTALL)
	allTitles = []
	for img,link,title in items:
		#title = title.replace('\n','')
		#title = title.strip(' ')
		if 'الحلقة' in title and '/c/' not in url:
			episode = re.findall(' الحلقة [0-9]*',title,re.DOTALL)
			if episode:
				title = title.replace(episode[0],'')
		#title = unescapeHTML(title)
		if title not in allTitles:
			allTitles.append(title)
			if '/video/' in link:
				addLink(title,link,92,img)
			else:
				addDir(title,link,91,img)
	html_blocks = re.findall('pagination(.*?)</div>',html,re.DOTALL)
	if html_blocks:
		block = html_blocks[0]
		items = re.findall('<a href="(.*?)".*?>(.*?)<',block,re.DOTALL)
		for link,title in items:
			title = unescapeHTML(title)
			title = title.replace('الصفحة ','')
			addDir('صفحة '+title,link,91)
	xbmcplugin.endOfDirectory(addon_handle)

def PLAY(url):
	urlLIST = []
	html = openURL(url,'',headers,'','4HELAL-PLAY-1st')
	html_blocks = re.findall('links-panel(.*?)div',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('href="(.*?)"',block,re.DOTALL)
	for link in items:
		urlLIST.append(link)
	html_blocks = re.findall('nav-tabs(.*?)video-panel-more',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('ajax-file-id.*?value="(.*?)"',block,re.DOTALL)
	id = items[0]
	#xbmcgui.Dialog().ok('',id)
	items = re.findall('data-server="(.*?)".*?false;">(.*?)<',block,re.DOTALL)
	for link,title in items:
		url = 'http://www.4helal.tv/ajax.php?id='+id+'&ajax=true&server='+link
		link = openURL(url,'',headers,'','4HELAL-PLAY-2nd')
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
	new_search = search.replace(' ','%20')
	#xbmcgui.Dialog().ok(str(len(search)) , str(len(new_search)) )
	url = 'https://www.4helal.tv/search.php'
	headers = { 'User-Agent' : '' , 'Content-Type' : 'application/x-www-form-urlencoded' }
	payload = { 't' : new_search }
	data = urllib.urlencode(payload)
	html = openURL(url,data,headers,'','4HELAL-SEARCH-1st')
	if 'movies-items' in html: ITEMS('',html)
	else: xbmcgui.Dialog().ok('no results','لا توجد نتائج للبحث')


