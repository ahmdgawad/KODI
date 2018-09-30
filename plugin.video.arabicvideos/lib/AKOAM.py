# -*- coding: utf-8 -*-
from LIBRARY import *

website0a = 'http://akoam.net'
headers = { 'User-Agent' : '' }
script_name='AKOAM'

def MAIN(mode,url):
	if mode==70: MENU()
	elif mode==71: CATEGORIES(url)
	elif mode==72: TITLES(url)
	elif mode==73: EPISODES(url)
	elif mode==74: PLAY(url)
	elif mode==75: SEARCH()

def MENU():
	addDir('بحث في الموقع',website0a,75)
	ignoreLIST = ['الألعاب','البرامج','الاجهزة اللوحية','الصور و الخلفيات']
	html = openURL(website0a,'',headers,'','AKOAM-MENU-1st')
	html_blocks = re.findall('big_parts_menu(.*?)main_partions',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('href="(.*?)".*?>(.*?)<',block,re.DOTALL)
	for link,title in items:
		#if any(value in link for value in ignoreLIST):
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
		addDir('الجميع',url,72)
		xbmcplugin.endOfDirectory(addon_handle)
	else: TITLES(url)

def TITLES(url):
	html = openURL(url,'',headers,'','AKOAM-TITLES-1st')
	html_blocks = re.findall('navigation(.*?)<script',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('subject_box.*?href="(.*?)".*?src="(.*?)".*?<h3>(.*?)<',block,re.DOTALL)
	for link,img,title in items:
		title = title.strip(' ')
		addDir(title,link,73,img)
	html_blocks = re.findall('pagination(.*?)</div',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('li>\n<a href=\'(.*?)\'>(.*?)<',block,re.DOTALL)
	for link,title in items:
		addDir('صفحة '+title,link,72,img)
	xbmcplugin.endOfDirectory(addon_handle)

def EPISODES(url):
	notvideosLIST = ['zip','rar','txt','pdf','htm','tar','iso']
	html = openURL(url,'',headers,'','AKOAM-EPISODES-1st')
	image = re.findall('class="main_img".*?src="(.*?)"',html,re.DOTALL)
	img = image[0]
	name = re.findall('class="sub_title".*?<h1>(.*?)</h1>',html,re.DOTALL)
	name = name[0].replace('\n','')
	html_blocks = re.findall('direct_link_box(.*?)ako-feedback',html,re.DOTALL)
	if not html_blocks:
		title = 'الرابط ليس فيديو'
		addLink(title,'',9999,img)
		xbmcplugin.endOfDirectory(addon_handle)
		return	
	block = html_blocks[0]
	items = re.findall('sub_epsiode_title">(.*?)</h2>.*?sub_file_title\'>(.*?)</span.*?href=\'(.*?)\'>',block,re.DOTALL)
	if items:
		for title,file,link in items:
			title = name + ' - ' + title.replace('\n','')
			if any(value in file for value in notvideosLIST):
				title = 'الرابط ليس فيديو'
				addLink(title,link,9999,img)
			else:
				addLink(title,link,74,img)
	else:
		title = 'رابط التشغيل'
		#title = name
		items = re.findall('sub_file_title\'>(.*?)</span>.*?href=\'(.*?)\'>',block,re.DOTALL)
		for file,link in items:
			if any(value in file for value in notvideosLIST):
				title = 'الرابط ليس فيديو'
				addLink(title,link,9999,img)
			else:
				addLink(title,link,74,img)
		if not items:
			title = 'الرابط ليس فيديو'
			addLink(title,'',9999,img)
	xbmcplugin.endOfDirectory(addon_handle)

def PLAY(url):
	id = url.split('/')[-1]
	url = 'http://load.is/link/read?hash=' + id
	html = openURL(url,'','','','AKOAM-PLAY-1st')
	items = re.findall('route":"(.*?)"',html,re.DOTALL)
	url = items[0].replace('\/','/')
	if 'catch.is' in url:
		#xbmcgui.Dialog().ok('catch.is',str(headers))
		id = url.split('%2F')[-1]
		url = 'http://catch.is/'+id
		payload = { 'op' : 'download2' , 'id' : id }
		headers['Content-Type'] = 'application/x-www-form-urlencoded'
		data = urllib.urlencode(payload)
		html = openURL(url,data,headers,'','AKOAM-PLAY-2nd')
		items = re.findall('direct_link.*?href="(.*?)"',html,re.DOTALL)
		url = items[0]
	else:
		#xbmcgui.Dialog().ok('load.is',str(headers))
		headers['X-Requested-With'] = 'XMLHttpRequest'
		headers['Referer'] = url
		html = openURL(url,'',headers,'','AKOAM-PLAY-3rd')
		items = re.findall('direct_link":"(.*?)"',html,re.DOTALL)
		url = items[0].replace('\/','/')
	PLAY_VIDEO(url,script_name)

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



