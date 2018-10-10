# -*- coding: utf-8 -*-
from LIBRARY import *

website0a = 'https://vod.alarab.com'
website0b = 'https://vod.alarab.com/view-1/افلام-عربية'
website0c = 'http://tv.alarab.com'
website0d = 'http://tv1.alarab.com'
website0e = 'http://vod.alarab.com/index.php'
script_name = 'ALARAB'

def MAIN(mode,url):
	if mode==10: MENU()
	elif mode==11: ITEMS(url)
	elif mode==12: PLAY(url)
	elif mode==13: SEARCH()
	elif mode==14: LATEST()
	#elif mode==15: RAMADAN('?year=2018')

def MENU():
	addDir('بحث في الموقع','',13,icon)
	addDir('مسلسلات جديدة','',14,icon)
	#addDir('مسلسلات رمضان','',15,icon)
	html = openURL(website0b,'','','','ALARAB-MENU-1st')
	html_blocks=re.findall('footer_sec(.*?)social-network',html,re.DOTALL)
	block=html_blocks[0]
	#xbmcgui.Dialog().ok(str(len(html)), str(len(block)) )
	items=re.findall('href="(.*?)".*?>(.*?)<',block,re.DOTALL)
	for url,name in items:
		addDir(name,url,11,icon)
	xbmcplugin.endOfDirectory(addon_handle)

def LATEST():
	html = openURL(website0b,'','','','ALARAB-LATEST-1st')
	html_blocks=re.findall('right_content.*?heading-top(.*?)heading-top',html,re.DOTALL)
	block = html_blocks[0]
	items=re.findall('href="(.*?)".*?src="(.*?)" alt="(.*?)"',block,re.DOTALL)
	for link,img,name in items:
		url = website0a + link
		addDir(name,url,11,img)
	xbmcplugin.endOfDirectory(addon_handle)

def ITEMS(url):
	#xbmcgui.Dialog().ok(url,'')
	html = openURL(url,'','','','ALARAB-ITEMS-1st')
	html_blocks = re.findall('heading-list(.*?)right_content',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('video-box.*?href="(.*?)".*?src="(.*?)" alt="(.*?)"',block,re.DOTALL)
	for link,img,name in items:
		url = website0a + link
		if 'series' in link:
			addDir(name,url,11,img)
		else:
			addLink(name,url,12,img)
	items = re.findall('tsc_3d_button red.*?href="(.*?)" title="(.*?)"',block,re.DOTALL)
	for link,page in items:
		url = website0a + link
		addDir(page,url,11,icon)
	xbmcplugin.endOfDirectory(addon_handle)

def PLAY(url):
	id = re.findall('com/v(.*?)-',url,re.DOTALL)[0]
	url2 = 'https://alarabplayers.alarab.com/?vid='+id
	html = openURL(url,'','','','ALARAB-PLAY-1st')
	html += openURL(url2,'','','','ALARAB-PLAY-2nd')
	#xbmcgui.Dialog().ok(url,'')
	html_blocks = re.findall('playerInstance.setup(.*?)primary',html,re.DOTALL)
	block = html_blocks[0]
	try: block += html_blocks[1]
	except: pass
	count = 0
	items_url = []
	items_name = []
	items = re.findall('file: "(.*?)mp4".*?label: "(.*?)"',block,re.DOTALL)
	for file,label in reversed(items):
		count += 1
		items_url.append(file+'mp4')
		items_name.append(label)
	items = re.findall('file:".*?youtu.*?=(.*?)"',block,re.DOTALL)
	for youtubeID in items:
		url = 'plugin://plugin.video.youtube/play/?video_id='+youtubeID
		count += 1
		items_url.append(url)
		items_name.append('From youtube')
	url = website0a + '/download.php?file='+id
	html = openURL(url,'','','','ALARAB-PLAY-3rd')
	items = re.findall('</h2>.*?href="(.*?)mp4"',html,re.DOTALL)
	if items:
		url = items[0] + 'mp4'
		count += 1
		items_url.append(url)
		items_name.append('From download')
	if count == 0:
		xbmcgui.Dialog().ok('No video file found','لا يوجد ملف فيديو')
		return
	elif count == 1:
		selection = 0
		url = items_url[selection]
	elif count > 1:
		new_items_url = []
		new_items_name = []
		for i in range(0,len(items_url),+1):
			if items_url[i] not in new_items_url:
				new_items_url.append(items_url[i])
				new_items_name.append(items_name[i])
		selection = xbmcgui.Dialog().select('Select Video Link:', new_items_name)
		if selection == -1 : return
		url = new_items_url[selection]
	PLAY_VIDEO(url,script_name)

def SEARCH():
	search = KEYBOARD()
	if search == '': return
	new_search = search.replace(' ','%20')
	searchlink = website0a + "/q/" + new_search
	#xbmcgui.Dialog().ok('',searchlink)
	ITEMS(searchlink)
"""
def RAMADAN(url):
	year = url.split('?year=')[1]
	#xbmcgui.Dialog().ok(url,year)
	html = openURL(website0b,'','','','ALARAB-RAMADAN-1st')
	html_blocks=re.findall('</a> </div></div>(.*?)ramadanseriesTOP',html,re.DOTALL)
	block = html_blocks[0]
	items=re.findall('href="(.*?)".*?>(.*?)<',block,re.DOTALL)
	for link,name in items:
		name = name.strip(' ')
		url = website0a + link.replace('2018',year)
		addDir(name,url,11)
	xbmcplugin.endOfDirectory(addon_handle)

def RAMADAN_YEARS_MENU():
	for year in range(2018,2000,-1):
		url = '?year=' + str(year)
		addDir(str(year),url,16)
	xbmcplugin.endOfDirectory(addon_handle)
"""
