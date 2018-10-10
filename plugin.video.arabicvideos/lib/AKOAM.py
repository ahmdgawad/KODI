# -*- coding: utf-8 -*-
from LIBRARY import *

website0a = 'https://akoam.net'
headers = { 'User-Agent' : '' }
script_name='AKOAM'

def MAIN(mode,url):
	if mode==70: MENU()
	elif mode==71: CATEGORIES(url)
	elif mode==72: TITLES(url,1)
	elif mode==73: EPISODES(url)
	elif mode==74: PLAY(url)
	elif mode==75: SEARCH()
	elif mode==76: TITLES(url,2)

def MENU():
	addDir('بحث في الموقع','',75)
	addDir('المميزة',website0a,76)
	ignoreLIST = ['الكتب و الابحاث','الكورسات التعليمية','الألعاب','البرامج','الاجهزة اللوحية','الصور و الخلفيات']
	html = openURL(website0a,'',headers,'','AKOAM-MENU-1st')
	html_blocks = re.findall('big_parts_menu(.*?)main_partions',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('href="(.*?)".*?>(.*?)<',block,re.DOTALL)
	for link,title in items:
		if title not in ignoreLIST:
			addDir(title,link,71)
	xbmcplugin.endOfDirectory(addon_handle)

def CATEGORIES(url):
	html = openURL(url,'',headers,'','AKOAM-CATEGORIES-1st')
	html_blocks = re.findall('sect_parts(.*?)</div>',html,re.DOTALL)
	if html_blocks:
		block = html_blocks[0]
		items = re.findall('href="(.*?)".*?>(.*?)<',block,re.DOTALL)
		for link,title in items:
			title = title.strip(' ')
			addDir(title,link,72)
		addDir('جميع الفروع',url,72)
		xbmcplugin.endOfDirectory(addon_handle)
	else: TITLES(url,1)

def TITLES(url,type):
	html = openURL(url,'',headers,'','AKOAM-TITLES-1st')
	if type==1:
		html_blocks = re.findall('navigation(.*?)<script',html,re.DOTALL)
	elif type==2:
		html_blocks = re.findall('section_title featured_title(.*?)subjects-crousel',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('subject_box.*?href="(.*?)".*?src="(.*?)".*?<h3>(.*?)<',block,re.DOTALL)
	for link,img,title in items:
		title = title.strip(' ')
		title = unescapeHTML(title)
		addDir(title,link,73,img)
	html_blocks = re.findall('pagination(.*?)</div',html,re.DOTALL)
	if html_blocks:
		block = html_blocks[0]
		items = re.findall('li>\n<a href=\'(.*?)\'>(.*?)<',block,re.DOTALL)
		for link,title in items:
			addDir('صفحة '+title,link,72,img)
	xbmcplugin.endOfDirectory(addon_handle)

def EPISODES(url):
	notvideosLIST = ['zip','rar','txt','pdf','htm','tar','iso','html']
	html = openURL(url,'',headers,'','AKOAM-EPISODES-1st')
	image = re.findall('class="main_img".*?src="(.*?)"',html,re.DOTALL)
	img = image[0]
	html_blocks = re.findall('ad-300-250.*?ad-300-250(.*?)ako-feedback',html,re.DOTALL)
	block = html_blocks[0]
	if 'sub_epsiode_title' in block:
		name = re.findall('class="sub_title".*?<h1>(.*?)</h1>',html,re.DOTALL)
		name = name[0].replace('\n','') + ' - '
		items = re.findall('sub_epsiode_title">(.*?)</h2>.*?sub_file_title\'>(.*?) - <i>',block,re.DOTALL)
	else:
		name = ''
		files = re.findall('sub_file_title\'>(.*?) - <i>',block,re.DOTALL)
		items = [ ('رابط التشغيل',files[0]) ]
	count = 0
	for title,file in items:
		filetype = file.split('.')[-1]
		if any(value in filetype for value in notvideosLIST):
			addLink('الرابط ليس فيديو','',9999,img)
		else:
			count += 1
			title = name + title.replace('\n','')
			link = url + '?ep='+str(count)
			addLink(title,link,74,img)
	xbmcplugin.endOfDirectory(addon_handle)

def PLAY(url):
	var = url.split('?ep=')
	url = var[0]
	episode = int(var[1])
	#xbmcgui.Dialog().ok(url,'')
	html = openURL(url,'',headers,'','AKOAM-EPISODES-1st')
	html_blocks = re.findall('ad-300-250.*?ad-300-250(.*?)ako-feedback',html,re.DOTALL)
	html_block = html_blocks[0].replace('\'direct_link_box\'','"direct_link_box epsoide_box"')
	html_block = html_block + 'direct_link_box'
	blocks = re.findall('epsoide_box(.*?)direct_link_box',html_block,re.DOTALL)
	block = blocks[episode-1]
	linkLIST = []
	serversDICT = { '1430052371':'ok.ru' , '1477487601':'estream' , '1505328404':'streammango' , '1423080015':'flashx' , '1458117295':'openload' }
	items = re.findall('download_btn\' target=\'_blank\' href=\'(.*?)\'',block,re.DOTALL)
	for link in items:
		linkLIST.append(link)
	items = re.findall('background-image: url\((.*?)\).*?href=\'(.*?)\'',block,re.DOTALL)
	for serverIMG,link in items:
		serverIMG = serverIMG.split('/')[-1]
		serverIMG = serverIMG.split('.')[0]
		linkLIST.append(link+'?'+serversDICT[serverIMG])
	from RESOLVERS import PLAY as RESOLVERS_PLAY
	url = RESOLVERS_PLAY(linkLIST,script_name,'no')
	vidoeURL = RESOLVE_AKOAM(url)
	PLAY_VIDEO(vidoeURL,script_name)

def SEARCH():
	search = KEYBOARD()
	if search == '': return
	new_search = search.replace(' ','%20')
	#xbmcgui.Dialog().ok(str(len(search)) , str(len(new_search)) )
	url = website0a + '/search/' + new_search
	html = openURL(url,'',headers,'','AKOAM-SEARCH-1st')
	html_blocks = re.findall('akoam_result(.*?)<script',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('href="(.*?)".*?background-image: url\((.*?)\).*?<h1>(.*?)</h1>',block,re.DOTALL)
	for link,img,title in items:
		title = title.replace('\n','')
		title = unescapeHTML(title)
		addDir(title,link,73,img)
	xbmcplugin.endOfDirectory(addon_handle)

def RESOLVE_AKOAM(url):
	id = url.split('/')[-1]
	from RESOLVERS import RESOLVE as RESOLVERS_RESOLVE
	url = 'http://load.is/' + id
	url = RESOLVERS_RESOLVE(url)
	if 'catch.is' in url:
		id = url.split('%2F')[-1]
		url = 'http://catch.is/'+id
		url = RESOLVERS_RESOLVE(url)
	else:
		headers['X-Requested-With'] = 'XMLHttpRequest'
		headers['Referer'] = url
		html = openURL(url,'',headers,'','AKOAM-PLAY-3rd')
		items1 = re.findall('<IFRAME SRC="(.*?)"',html,re.DOTALL)
		items2 = re.findall('<iframe src="(.*?)"',html,re.DOTALL)
	if items1:
		url = items1[0].replace('\/','/')
	elif items2:
		url = items2[0].replace('\/','/')
	else:
		items = re.findall('direct_link":"(.*?)"',html,re.DOTALL)
		url = items[0].replace('\/','/')
	return url

