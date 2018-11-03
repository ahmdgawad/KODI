# -*- coding: utf-8 -*-
from LIBRARY import *

website0a = 'https://shoofmax.com'
website0b = 'https://static.shoofmax.com'
script_name = 'SHOOFMAX'

def MAIN(mode,url):
	if mode==50: MAIN_MENU()
	elif mode==51: TITLES(url)
	elif mode==52: EPISODES(url)
	elif mode==53: PLAY(url)
	elif mode==54: SEARCH()
	elif mode==55: MOVIES_MENU()
	elif mode==56: SERIES_MENU()
	return

def MAIN_MENU():
	addDir('بحث في الموقع','',54)
	addDir('المسلسلات','',56)
	addDir('الافلام','',55)
	xbmcplugin.endOfDirectory(addon_handle)
	return

def MOVIES_MENU():
	addDir('احدث الافلام',website0a+'/movie/1/latest',51)
	addDir('افلام رائجة',website0a+'/movie/1/popular',51)
	addDir('اخر اضافات الافلام',website0a+'/movie/1/newest',51)
	addDir('افلام كلاسيكية',website0a+'/movie/1/classic',51)
	addDir('اجدد الافلام',website0a+'/movie/1/yop',51)
	addDir('الافلام الافضل تقييم',website0a+'/movie/1/review',51)
	addDir('الافلام الاكثر مشاهدة',website0a+'/movie/1/views',51)
	xbmcplugin.endOfDirectory(addon_handle)
	return

def SERIES_MENU():
	addDir('احدث المسلسلات',website0a+'/series/1/latest',51)
	addDir('مسلسلات رائجة',website0a+'/series/1/popular',51)
	addDir('اخر اضافات المسلسلات',website0a+'/series/1/newest',51)
	addDir('مسلسلات كلاسيكية',website0a+'/series/1/classic',51)
	addDir('اجدد المسلسلات',website0a+'/series/1/yop',51)
	addDir('المسلسلات الافضل تقييم',website0a+'/series/1/review',51)
	addDir('المسلسلات الاكثر مشاهدة',website0a+'/series/1/views',51)
	xbmcplugin.endOfDirectory(addon_handle)
	return
	
	
def TITLES(url):
	info = url.split('/')
	sort = info[ len(info)-1 ]
	page = info[ len(info)-2 ]
	type = info[ len(info)-3 ]
	if sort in ['yop','review','views']:
		if type=='movie': type1='فيلم'
		elif type=='series': type1='مسلسل'
		url = website0a + '/filter-programs/' + quote(type1) + '/' + page + '/' + sort
		html = openURL(url,'','','','SHOOFMAX-TITLES-1st')
		items = re.findall('"ref":(.*?),.*?"title":"(.*?)".+?"numep":(.*?),"res":"(.*?)"',html,re.DOTALL)
		count_items=0
		for id,title,episodes_number,img in items:
			count_items += 1
			img = website0b + '/img/program/' + img + '-2.jpg'
			link = website0a + '/program/' + id
			if type=='movie': addLink(title,link,53,img)
			if type=='series': addDir(title,link+'?ep='+episodes_number+'='+title+'='+img,52,img)
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
			if type=='movie': addLink(title,link,53,img)
			if type=='series': addDir(title,link+'?ep='+episodes_number+'='+title+'='+img,52,img)
	title='صفحة '
	if count_items==16:
		for count_page in range(1,13) :
			if not page==str(count_page):
				url = website0a+'/filter-programs/'+type+'/'+str(count_page)+'/'+sort
				addDir(title+str(count_page),url,51)
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
		addLink(title,link,53,img)
	xbmcplugin.endOfDirectory(addon_handle)
	return

def PLAY(url):
	html = openURL(url,'','','','SHOOFMAX-PLAY-1st')
	html_blocks = re.findall('intro_end(.*?)initialize',html,re.DOTALL)
	block = html_blocks[0]
	#file = open('/data/emad.html', 'w')
	#file.write(url)
	#file.write('\n\n\n')
	#file.write(block)
	#file.close()
	#xbmcgui.Dialog().ok(origin_link, backup_origin_link )
	origin_link = re.findall('var origin_link = "(.*?)"',block,re.DOTALL)[0]
	backup_origin_link = re.findall('var backup_origin_link = "(.*?)"',block,re.DOTALL)[0]
	links = re.findall('origin_link\+"(.*?)"',block,re.DOTALL)
	video1 = origin_link + links[0]
	video2 = backup_origin_link + links[1]
	multiple1 = origin_link + links[2]
	multiple2 = backup_origin_link + links[3]
	count = 0
	items_url = []
	items_name = []
	items_url.append(video1)
	items_name.append('Main server: mp4')
	items_url.append(video2)
	items_name.append('Backup server: mp4')
	html = openURL(multiple1,'','','','SHOOFMAX-PLAY-2nd')
	base = multiple1.replace('variant.m3u8','')
	items = re.findall('RESOLUTION=(.*?),.*?\n(.*?)u8',html,re.DOTALL)
        for quality,link in items:
		url = base + link + 'u8'
		count += 1
		items_url.append(url)
		items_name.append('Main server: m3u8 '+quality)
	count += 1
	html = openURL(multiple2,'','','','SHOOFMAX-PLAY-3rd')
	base = multiple2.replace('variant.m3u8','')
	items = re.findall('RESOLUTION=(.*?),.*?\n(.*?)u8',html,re.DOTALL)
        for quality,link in items:
		url = base + link + 'u8'
		count += 1
		items_url.append(url)
		items_name.append('Backup server: m3u8 '+quality)
	count += 1
	selection = xbmcgui.Dialog().select('Select Video Quality:', items_name)
	if selection == -1 : return
	url = items_url[selection]
	#url = mixARABIC(url)
	#xbmcgui.Dialog().ok(url,'' )
	PLAY_VIDEO(url,script_name)
	return

def SEARCH():
	search = KEYBOARD()
	if search == '': return
	new_search = search.replace(' ','%20')
	import requests
	response = requests.get(website0a, data='', headers='')
	html = response.text
	cookies = response.cookies.get_dict()
	cookie = cookies['session']
	block = re.findall('name="_csrf" value="(.*?)">',html,re.DOTALL)
	csrf = block[0]
	payload = '_csrf=' + csrf + '&q=' + quote(new_search)
	headers = { 'content-type':'application/x-www-form-urlencoded' , 'cookie':'session='+cookie }
	url = website0a + "/search"
	response = requests.post(url, data=payload, headers=headers)
	html = response.text
	html_blocks = re.findall('general-body(.*?)search-bottom-padding',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('href="(.*?)".*?background-image: url\((.*?)\).*?<span>(.*?)</span>',block,re.DOTALL)
	for link,img,title in items:
		title = title.replace('\n','')
		url = website0a + link
		if '/program/' in url:
			if '?ep=' in url:
				url = url.replace('?ep=1','?ep=0')
				url = url + '=' + quote(title.encode('utf8')) + '=' + img
				addDir('[[ '+title+' ]]',url,52,img)
			else:
				addLink(title,url,53,img)
	xbmcplugin.endOfDirectory(addon_handle)
	return



