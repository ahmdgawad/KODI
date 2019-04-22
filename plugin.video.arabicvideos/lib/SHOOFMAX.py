# -*- coding: utf-8 -*-
from LIBRARY import *

website0a = 'https://shoofmax.com'
website0b = 'https://static.shoofmax.com'
script_name = 'SHOOFMAX'
menu_name='[COLOR FFC89008]SHF [/COLOR]'

def MAIN(mode,url,text):
	if mode==50: MAIN_MENU()
	elif mode==51: TITLES(url)
	elif mode==52: EPISODES(url)
	elif mode==53: PLAY(url)
	elif mode==55: MOVIES_MENU()
	elif mode==56: SERIES_MENU()
	elif mode==57: FILTERS(url,1)
	elif mode==58: FILTERS(url,2)
	elif mode==59: SEARCH(text)
	return

def MAIN_MENU():
	addDir(menu_name+'بحث في الموقع','',59)
	addDir(menu_name+'المسلسلات','',56)
	addDir(menu_name+'الافلام','',55)
	xbmcplugin.endOfDirectory(addon_handle)
	return

def MOVIES_MENU():
	addDir(menu_name+'افلام رائجة',website0a+'/movie/1/popular',51)
	addDir(menu_name+'احدث الافلام',website0a+'/movie/1/latest',51)
	addDir(menu_name+'افلام كلاسيكية',website0a+'/movie/1/classic',51)
	addDir(menu_name+'اخر اضافات الافلام',website0a+'/movie/1/newest',51)
	addDir('=========================','',9999)
	addDir(menu_name+'اختيار افلام مرتبة بسنة الانتاج',website0a+'/movie/1/yop',57)
	addDir(menu_name+'اختيار افلام مرتبة بالافضل تقييم',website0a+'/movie/1/review',57)
	addDir(menu_name+'اختيار افلام مرتبة بالاكثر مشاهدة',website0a+'/movie/1/views',57)
	xbmcplugin.endOfDirectory(addon_handle)
	return

def SERIES_MENU():
	addDir(menu_name+'مسلسلات رائجة',website0a+'/series/1/popular',51)
	addDir(menu_name+'احدث المسلسلات',website0a+'/series/1/latest',51)
	addDir(menu_name+'مسلسلات كلاسيكية',website0a+'/series/1/classic',51)
	addDir(menu_name+'اخر اضافات المسلسلات',website0a+'/series/1/newest',51)
	addDir('=========================','',9999)
	addDir(menu_name+'اختيار مسلسلات مرتبة بسنة الانتاج',website0a+'/series/1/yop',57)
	addDir(menu_name+'اختيار مسلسلات مرتبة بالافضل تقييم',website0a+'/series/1/review',57)
	addDir(menu_name+'اختيار مسلسلات مرتبة بالاكثر مشاهدة',website0a+'/series/1/views',57)
	xbmcplugin.endOfDirectory(addon_handle)
	return

def TITLES(url):
	#xbmcgui.Dialog().ok(url,url)
	if '?' in url:
		parts = url.split('?')
		filter = '?' + urllib2.quote(parts[1],'=&:/')
		url = parts[0]
	else: filter = ''
	#xbmcgui.Dialog().ok(filter,'')
	info = url.split('/')
	sort = info[ len(info)-1 ]
	page = info[ len(info)-2 ]
	type = info[ len(info)-3 ]
	if sort in ['yop','review','views']:
		if type=='movie': type1='فيلم'
		elif type=='series': type1='مسلسل'
		url = website0a + '/filter-programs/' + quote(type1) + '/' + page + '/' + sort + filter
		html = openURL(url,'','','','SHOOFMAX-TITLES-1st')
		items = re.findall('"ref":(.*?),.*?"title":"(.*?)".+?"numep":(.*?),"res":"(.*?)"',html,re.DOTALL)
		count_items=0
		for id,title,episodes_number,img in items:
			count_items += 1
			img = website0b + '/img/program/' + img + '-2.jpg'
			link = website0a + '/program/' + id
			if type=='movie': addLink(menu_name+title,link,53,img)
			if type=='series': addDir(menu_name+'مسلسل '+title,link+'?ep='+episodes_number+'='+title+'='+img,52,img)
	else:
		if type=='movie': type1='movies'
		elif type=='series': type1='series'
		url = website0b + '/json/selected/' + sort + '-' + type1 + '-WW.json'
		html = openURL(url,'','','','SHOOFMAX-TITLES-2nd')
		items = re.findall('"ref":(.*?),"ep":(.*?),"base":"(.*?)","title":"(.*?)"',html,re.DOTALL)
		count_items=0
		for id,episodes_number,img,title in items:
			count_items += 1
			img = website0b + '/img/program/' + img + '-2.jpg'
			link = website0a + '/program/' + id
			if type=='movie': addLink(menu_name+title,link,53,img)
			if type=='series': addDir(menu_name+'مسلسل '+title,link+'?ep='+episodes_number+'='+title+'='+img,52,img)
	title='صفحة '
	if count_items==16:
		for count_page in range(1,13) :
			if not page==str(count_page):
				url = website0a+'/filter-programs/'+type+'/'+str(count_page)+'/'+sort + filter
				addDir(menu_name+title+str(count_page),url,51)
	xbmcplugin.endOfDirectory(addon_handle)
	return

def EPISODES(url):
	info = url.split('=')
	episodes_number = info[1]
	name = unquote(info[2])
	img = info[3]
	info = url.split('?')
	url = info[0]
	if episodes_number=='0':
		html = openURL(url,'','','','SHOOFMAX-SEARCH-1st')
		html_blocks = re.findall('<select(.*?)</select>',html,re.DOTALL)
		block = html_blocks[0]
		items = re.findall('option value="(.*?)"',block,re.DOTALL)
		episodes_number = items[-1]
		#xbmcgui.Dialog().ok(episodes_number,'')
	#name = xbmc.getInfoLabel( "ListItem.Title" )
	#img = xbmc.getInfoLabel( "ListItem.Thumb" )
	name1 = 'مسلسل '
	name2 = ' - الحلقة '
        for episode in range(int(episodes_number),0,-1):
		link = url + '?ep=' + str(episode)
		title = name1 + name + name2 + str(episode)
		addLink(menu_name+title,link,53,img)
	xbmcplugin.endOfDirectory(addon_handle)
	return

def PLAY(url):
	html = openURL(url,'','','','SHOOFMAX-PLAY-1st')
	html_blocks = re.findall('intro_end(.*?)initialize',html,re.DOTALL)
	block = html_blocks[0]
	items_url = []
	items_name = []
	multiples = []
	origin_link = re.findall('var origin_link = "(.*?)"',block,re.DOTALL)[0]
	backup_origin_link = re.findall('var backup_origin_link = "(.*?)"',block,re.DOTALL)[0]
	links = re.findall('mp4:.*?_link.*?\t(.*?)_link\+"(.*?)"',block,re.DOTALL)
	links += re.findall('mp4:.*?\t(.*?)_link\+"(.*?)"',block,re.DOTALL)
	for server,link in links:
		filename = link.split('/')[-1]
		filename = filename.replace('fallback','')
		filename = filename.replace('.mp4','')
		filename = filename.replace('-','')
		if 'backup' in server:
			server = 'backup server'
			url = backup_origin_link + link
		else:
			server = 'main server'
			url = origin_link + link
		items_url.append(url)
		items_name.append('mp4: '+server+' '+filename)
	links = re.findall('hls: (.*?)_link\+"(.*?)"',block,re.DOTALL)
	for server,link in links:
		if 'backup' in server:
			server = 'backup server'
			url = backup_origin_link + link
		else:
			server = 'main server'
			url = origin_link + link
		html = openURL(url,'','','','SHOOFMAX-PLAY-2nd')
		items = re.findall('RESOLUTION=(.*?),.*?\n(.*?)m3u8',html,re.DOTALL)
		for quality,link in items:
			url2 = url.replace('variant.m3u8','') + link + 'm3u8'
			items_url.append(url2)
			items_name.append('m3u8: '+server+' '+quality)
	selection = xbmcgui.Dialog().select('Select Video Quality:', items_name)
	if selection == -1 : return
	url = items_url[selection]
	#url = mixARABIC(url)
	PLAY_VIDEO(url,script_name)
	return

def FILTERS(url,type):
	#xbmcgui.Dialog().ok(url,url)
	if 'series' in url: url2 = website0a + '/genre/مسلسل'
	else: url2 = website0a + '/genre/فيلم'
	url2 = quote(url2)
	html = openURL(url2,'','','','SHOOFMAX-FILTERS-1st')
	#xbmcgui.Dialog().ok(url,html)
	if type==1: html_blocks = re.findall('subgenre(.*?)div',html,re.DOTALL)
	elif type==2: html_blocks = re.findall('country(.*?)div',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('option value="(.*?)">(.*?)</option',block,re.DOTALL)
	if type==1:
		for subgenre,title in reversed(items):
			addDir(menu_name+title,url+'?subgenre='+subgenre,58)
	elif type==2:
		parts = url.split('?')
		url = parts[0]
		subgenre = parts[1]
		for country,title in reversed(items):
			addDir(menu_name+title,url+'?country='+country+'&'+subgenre,51)
	xbmcplugin.endOfDirectory(addon_handle)
	return

def SEARCH(search=''):
	if search=='': search = KEYBOARD()
	if search == '': return
	#xbmcgui.Dialog().ok(search,search)
	new_search = search.replace(' ','%20')
	from requests import request as requests_request
	response = requests_request('GET', website0a, data='', headers='')
	html = response.text
	cookies = response.cookies.get_dict()
	cookie = cookies['session']
	block = re.findall('name="_csrf" value="(.*?)">',html,re.DOTALL)
	csrf = block[0]
	payload = '_csrf=' + csrf + '&q=' + quote(new_search)
	headers = { 'content-type':'application/x-www-form-urlencoded' , 'cookie':'session='+cookie }
	url = website0a + "/search"
	response = requests_request('POST', url, data=payload, headers=headers)
	html = response.text
	html_blocks = re.findall('general-body(.*?)search-bottom-padding',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('href="(.*?)".*?background-image: url\((.*?)\).*?<span>(.*?)</span>',block,re.DOTALL)
	if items:
		for link,img,title in items:
			title = title.replace('\n','')
			url = website0a + link
			if '/program/' in url:
				if '?ep=' in url:
					url = url.replace('?ep=1','?ep=0')
					url = url + '=' + quote(title.encode('utf8')) + '=' + img
					addDir(menu_name+'مسلسل '+title,url,52,img)
				else:
					addLink(menu_name+'فيلم '+title,url,53,img)
		xbmcplugin.endOfDirectory(addon_handle)
	else: xbmcgui.Dialog().ok('no results','لا توجد نتائج للبحث')
	return


