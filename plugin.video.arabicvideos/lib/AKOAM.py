# -*- coding: utf-8 -*-
from LIBRARY import *

website0a = 'http://akoam.net'
headers={ 'User-Agent' : '' }

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
	html = openURL(website0a,'',headers)
	html_blocks = re.findall('big_parts_menu(.*?)main_partions',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('href="(.*?)".*?>(.*?)<',block,re.DOTALL)
	for link,title in items:
		#if any(value in link for value in ignoreLIST):
		if title not in ignoreLIST:
			addDir(title,link,71)
	xbmcplugin.endOfDirectory(addon_handle)

def CATEGORIES(url):
	html = openURL(url,'',headers)
	html_blocks = re.findall('sect_parts(.*?)</div>',html,re.DOTALL)
	if html_blocks:
		block = html_blocks[0]
		items = re.findall('href="(.*?)".*?>(.*?)<',block,re.DOTALL)
		for link,title in items:
			addDir(title,link,72)
		addDir('الجميع',url,72)
		xbmcplugin.endOfDirectory(addon_handle)
	else: TITLES(url)

def TITLES(url):
	html = openURL(url,'',headers)
	html_blocks = re.findall('navigation(.*?)<script',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('subject_box.*?href="(.*?)".*?src="(.*?)".*?<h3>(.*?)<',block,re.DOTALL)
	for link,img,title in items:
		addDir(title,link,73,img)
	html_blocks = re.findall('pagination(.*?)</div',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('li>\n<a href=\'(.*?)\'>(.*?)<',block,re.DOTALL)
	for link,title in items:
		addDir(title,link,72,img)
	xbmcplugin.endOfDirectory(addon_handle)

def EPISODES(url):
	notvideosLIST = ['zip','rar','txt','pdf','htm','tar','iso']
	html = openURL(url,'',headers)
	image = re.findall('class="main_img" src="(.*?)"',html,re.DOTALL)
	img = image[0]
	html_blocks = re.findall('direct_link_box(.*?)ako-feedback',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('sub_epsiode_title">(.*?)</h2>.*?sub_file_title\'>(.*?)</span.*?href=\'(.*?)\'>',block,re.DOTALL)
	if items:
		for title,file,link in items:
			title = title.replace('\n','')
			if any(value in file for value in notvideosLIST):
				title = 'الملف ليس فيديو'
				addLink(title,link,9999,img)
			else:
				addLink(title,link,74,img)
	else:
		items = re.findall('sub_file_title\'>(.*?)</span>.*?href=\'(.*?)\'>',block,re.DOTALL)
		title = 'رابط التشغيل'
		for file,link in items:
			if any(value in file for value in notvideosLIST):
				title = 'الملف ليس فيديو'
				addLink(title,link,9999,img)
			else:
				addLink(title,link,74,img)
	xbmcplugin.endOfDirectory(addon_handle)

def PLAY(url):
	id = url.split('/')[3]
	url = 'http://load.is/link/read?hash=' + id
	html = openURL(url)
	items = re.findall('route":"(.*?)"',html,re.DOTALL)
	url = items[0].replace('\/','/')
	headers['X-Requested-With'] = 'XMLHttpRequest'
	headers['Referer'] = url
	##xbmcgui.Dialog().ok(url , str(headers))
	html = openURL(url,'',headers)
	items = re.findall('direct_link":"(.*?)"',html,re.DOTALL)
	url = items[0].replace('\/','/')
	play_item = xbmcgui.ListItem(path=url)
	play_item.setProperty('IsPlayable', 'true')
	xbmcplugin.setResolvedUrl(addon_handle, True, play_item)

def SEARCH():
	search =''
	keyboard = xbmc.Keyboard(search, 'Search')
	keyboard.doModal()
	if keyboard.isConfirmed(): search = keyboard.getText()
	if len(search)<2:
		xbmcgui.Dialog().ok('غير مقبول. اعد المحاولة.','Not acceptable. Try again.')
		return
	search = search.replace(' ','%20')
	new_search = mixARABIC(search)
	url = website0a + '/search/' + new_search
	html = openURL(url,'',headers)
	html_blocks = re.findall('akoam_result(.*?)<script',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('href="(.*?)".*?background-image: url\((.*?)\).*?<h1>(.*?)</h1>',block,re.DOTALL)
	for link,img,title in items:
		title = title.replace('\n','')
		addDir(title,link,73,img)
	xbmcplugin.endOfDirectory(addon_handle)



