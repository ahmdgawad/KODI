# -*- coding: utf-8 -*-
from LIBRARY import *

website0a = 'http://www.panet.co.il'
website0b = 'http://m.panet.co.il'
headers = { 'User-Agent' : '' }
script_name = 'PANET'

def MAIN(mode,url):
	if mode==30: MENU()
	elif mode==31: CATEGORIES(url)
	elif mode==32: ITEMS(url)
	elif mode==33: PLAY(url)
	elif mode==34: SEARCH(url)
	elif mode==35: CATEGORIES(url,'1')
	elif mode==36: CATEGORIES(url,'2')

def MENU():
	addDir('بحث عن افلام',website0a+'/search/result/title/movies',34,icon)
	addDir('بحث عن مسلسلات',website0a+'/search/result/title/series',34,icon)
	addDir('مسلسلات وبرامج',website0a+'/series/v1',31,icon)
	addDir('افلام مصنفة حسب النوع',website0a+'/movies',35,icon)
	addDir('افلام مصنفة حسب الممثل',website0a+'/movies',36,icon)
	addDir('احدث الافلام',website0a+'/movies',32,icon)
	addDir('مسرحيات',website0a+'/movies/genre/4/1',32,icon)
	xbmcplugin.endOfDirectory(addon_handle)

def CATEGORIES(url,select=''):
	info = url.split('/')
	type = info[3]
	#xbmcgui.Dialog().ok(type, url)
	if type=='series':
		html = openURL(url,'',headers,'','PANET-CATEGORIES-1st')
		html_blocks=re.findall('categoriesMenu(.*?)seriesForm',html,re.DOTALL)
		block= html_blocks[0]
		items=re.findall('href="(.*?)">(.*?)<',block,re.DOTALL)
		for link,name in items:
			url = website0a + link
			name = name.strip(' ')
			addDir(name,url,32,icon)
	if type=='movies':
		html = openURL(url,'',headers,'','PANET-CATEGORIES-2nd')
		if select=='1':
			html_blocks=re.findall('moviesGender(.*?)select',html,re.DOTALL)
			block = html_blocks[0]
			items=re.findall('option><option value="(.*?)">(.*?)<',block,re.DOTALL)
			for value,name in items:
				url = website0a + '/movies/genre/' + value
				addDir(name,url,32,icon)
		elif select=='2':
			html_blocks=re.findall('moviesActor(.*?)select',html,re.DOTALL)
			block = html_blocks[0]
			items=re.findall('option><option value="(.*?)">(.*?)<',block,re.DOTALL)
			for value,name in items:
				url = website0a + '/movies/actor/' + value
				addDir(name,url,32,icon)
	xbmcplugin.endOfDirectory(addon_handle)

def ITEMS(url):
	html = openURL(url,'',headers,'','PANET-ITEMS-1st')
	type = url.split('/')[3]
	if 'home' in url: type='episodes'
	if type=='series':
		html_blocks = re.findall('panet-thumbnails(.*?)panet-pagination',html,re.DOTALL)
		block = html_blocks[0]
		items = re.findall('href="(.*?)""><img src="(.*?)".*?h2>(.*?)<',block,re.DOTALL)
		for link,img,name in items:
			url = website0a + link 
			name = name.strip(' ')
			addDir(name,url,32,img)
	if type=='movies':
		html_blocks = re.findall('panet-mars-adv-panel.*?advBarMars(.+?)panet-pagination',html,re.DOTALL)
		block = html_blocks[0]
		items = re.findall('panet-thumbnail.*?href="(.*?)"><img src="(.*?)" alt="(.+?)"',block,re.DOTALL)
		for link,img,name in items:
			name = name.strip(' ')
			url = website0a + link
			addLink(name,url,33,img)
	if type=='episodes':
		page = url.split('/')[-1]
		#xbmcgui.Dialog().ok(url,'')
		if page=='1':
			html_blocks = re.findall('panet-mars-adv-panel(.+?)advBarMars',html,re.DOTALL)
			block = html_blocks[0]
			items = re.findall('panet-thumbnail.*?href="(.*?)"><img src="(.*?)".*?panet-title">(.*?)</div.*?panet-info">(.*?)</div',block,re.DOTALL)
			count = 0
			for link,img,episode,title in items:
				count += 1
				if count==10: break
				name = title + ' - ' + episode
				url = website0a + link
				addLink(name,url,33,img)
		html_blocks = re.findall('panet-mars-adv-panel.*?advBarMars(.+?)panet-pagination',html,re.DOTALL)
		block = html_blocks[0]
		items = re.findall('panet-thumbnail.*?href="(.*?)""><img src="(.*?)".*?panet-title"><h2>(.*?)</h2.*?panet-info"><h2>(.*?)</h2',block,re.DOTALL)
		for link,img,title,episode in items:
			episode = episode.strip(' ')
			title = title.strip(' ')
			name = title + ' - ' + episode
			url = website0a + link
			addLink(name,url,33,img)
	html_blocks = re.findall('glyphicon-chevron-right(.+?)data-revive-zoneid="4"',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('<li><a href="(.*?)">(.*?)<',block,re.DOTALL)
	for link,page in items:
		url = website0a + link 
		name = 'صفحة ' + page
		addDir(name,url,32,icon)
	xbmcplugin.endOfDirectory(addon_handle)

def PLAY(url):
	#xbmcgui.Dialog().ok(url,'')
	if 'series' in url:
		url = website0a + '/series/v1/seriesLink/' + url.split('/')[-1]
		html = openURL(url,'',headers,'','PANET-PLAY-1st')
		items = re.findall('url":"(.*?)"',html,re.DOTALL)
		url = items[0]
		url = url.replace('\/','/')
	else:
		html = openURL(url,'',headers,'','PANET-PLAY-2nd')
		items = re.findall('contentURL" content="(.*?)"',html,re.DOTALL)
		url = items[0]
	PLAY_VIDEO(url,script_name)

def SEARCH(url):
	search = KEYBOARD()
	if search == '': return
	new_search = search.replace(' ','-')
	type=url.split('/')[-1]
	data = 'query='+new_search+'&searchDomain='+type
	html = openURL(website0a+'/search',data,headers,'','PANET-SEARCH-1st')
	#xbmcgui.Dialog().ok(html, new_search)
	items=re.findall('title":"(.*?)".*?link":"(.*?)"',html,re.DOTALL)
	for title,link in items:
		url = website0a + link.replace('\/','/')
		#xbmcgui.Dialog().ok(title, url.split('/')[-1]   )
		if type=='movies': addLink(title,url,33,icon)
		else: addDir(title,url+'/1',32,icon)
	xbmcplugin.endOfDirectory(addon_handle)


