# -*- coding: utf-8 -*-
from LIBRARY import *

website0a = 'http://shahid4u.me'
script_name='SHAHID4U'
headers = { 'User-Agent' : '' }

def MAIN(mode,url):
	if mode==110: MENU()
	elif mode==111: ITEMS(url)
	elif mode==112: PLAY(url)
	elif mode==113: SEARCH()
	return

def MENU():
	addDir('بحث في الموقع','',113)
	addDir('المضاف حديثا',website0a,111)
	html = openURL(website0a,'',headers,'','SHAHID4U-MENU-1st')
	html_blocks = re.findall('menu-master(.*?)header>',html,re.DOTALL)
	#xbmcgui.Dialog().ok(html,html)
	block = html_blocks[0]
	items = re.findall('href="(.*?)">(.*?)<',block,re.DOTALL)
	ignoreLIST = ['مسلسلات انمي','الرئيسية']
	for link,title in items:
		title = title.strip(' ')
		if not any(value in title for value in ignoreLIST):
			addDir(title,link,111)
	xbmcplugin.endOfDirectory(addon_handle)
	return

def ITEMS(url):
	dirLIST = ['/category/series','/category/ramadan','?s=',quote('/category/برامج-تلفزيونية').lower()]
	if any(value in url for value in dirLIST):
		directory = True
	else:
		directory = False
	html = openURL(url,'',headers,'','SHAHID4U-ITEMS-1st')
	html_blocks = re.findall('class="blocksFilms"(.*?)<div class="header ">',html,re.DOTALL)
	if not html_blocks:
		html_blocks = re.findall('class="cats da_Sa"(.*?)<div class="header ">',html,re.DOTALL)
	if not html_blocks:
		PLAY(url)
		return
	block = html_blocks[0]
	items = re.findall('src="(.*?)".*?movief"><a href="(.*?)">(.*?)<',block,re.DOTALL)
	allTitles = []
	itemLIST = ['الحلقة','فيلم','اغنية','كليب','اعلان']
	#xbmcgui.Dialog().ok(quote('/category/برامج-تلفزيونية'),'')
	for img,link,title in items:
		link = unquote(link)
		#title = title.replace('\n','')
		#title = title.strip(' ')
		if directory is True:
			episode = re.findall(' الحلقة [0-9]*',title,re.DOTALL)
			if episode:
				title = title.replace(episode[0],'')
				title = title.replace(' والاخيرة','')
		if any(value in title for value in itemLIST):
			directory = False
		title = unescapeHTML(title)
		if title not in allTitles:
			allTitles.append(title)
			if directory is True:
				addDir(title,link,111,img)
			else:
				addLink(title,link,112,img)
	html_blocks = re.findall('class="pagination(.*?)</div>',html,re.DOTALL)
	if html_blocks:
		block = html_blocks[0]
		items = re.findall('<li><a href=["\'](.*?)["\'].*?>(.*?)<',block,re.DOTALL)
		for link,title in items:
			title = unescapeHTML(title)
			title = title.replace('الصفحة ','')
			addDir('صفحة '+title,link,111)
	xbmcplugin.endOfDirectory(addon_handle)
	return

def PLAY(url):
	linkLIST = []
	urlLIST = []
	html = openURL(url,'',headers,'','SHAHID4U-PLAY-1st')
	html_blocks = re.findall('class="servers2(.*?)</div>',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('href="(.*?)"',block,re.DOTALL)
	for link in items:
		linkLIST.append(link)
	url = url + '?watch=1'
	html = openURL(url,'',headers,'','SHAHID4U-PLAY-2nd')
	#xbmcgui.Dialog().ok(html,html)
	html_blocks = re.findall('li.server"(.*?)id="DataServers',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('url: \'(.*?)\'.*?data: \'(.*?)\'',block,re.DOTALL)
	url = items[0][0]+'?'+items[0][1]
	items = re.findall('server\((.*?)\)',block,re.DOTALL)
	for server in items:
		#html = openURL(url+server,'',headers,'','SHAHID4U-PLAY-3rd')
		urlLIST.append(url+server)
	count = len(urlLIST)
	import concurrent.futures
	with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
		responcesDICT = dict( (executor.submit(openURL, urlLIST[i], '', headers,'','SHAHID4U-PLAY-3rd'), i) for i in range(0,count) )
	for response in concurrent.futures.as_completed(responcesDICT):
		html = response.result()
		#html = html.replace('SRC=','src=')
		links = re.findall('src="(.*?)"',html,re.DOTALL)
		linkLIST.append(links[0])
	from RESOLVERS import PLAY as RESOLVERS_PLAY
	RESOLVERS_PLAY(linkLIST,script_name,'yes')
	return

def SEARCH():
	search = KEYBOARD()
	if search == '': return
	search = search.replace(' ','+')
	url = website0a + '/?s=' + search
	ITEMS(url)
	return



