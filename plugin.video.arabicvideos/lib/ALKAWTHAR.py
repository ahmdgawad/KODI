# -*- coding: utf-8 -*-
from LIBRARY import *

website0a = 'http://www.alkawthartv.com'
script_name = 'ALKAWTHAR'

def MAIN(mode,url,page):
	if mode==130: MENU()
	#elif mode==131: TITLES(url)
	elif mode==132: CATEGORIES(url)
	elif mode==133: EPISODES(url,page)
	elif mode==134: PLAY(url)
	elif mode==135: LIVE()
	elif mode==136: SEARCH(page)
	return

def MENU():
	addLink('البث الحي لقناة الكوثر','',135,'','','no')
	addDir('بحث في الموقع','',136,icon,1)
	addDir('المسلسلات',website0a+'/category/543',132,icon,1)
	addDir('الافلام',website0a+'/category/628',132,icon,1)
	addDir('برامج الصغار والشباب',website0a+'/category/517',132,icon,1)
	addDir('ابرز البرامج',website0a+'/category/1763',132,icon,1)
	addDir('المحاضرات',website0a+'/category/943',132,icon,1)
	addDir('عاشوراء',website0a+'/category/1353',132,icon,1)
	addDir('البرامج الاجتماعية',website0a+'/category/501',132,icon,1)
	addDir('البرامج الدينية',website0a+'/category/509',132,icon,1)
	addDir('البرامج الوثائقية',website0a+'/category/553',132,icon,1)
	addDir('البرامج السياسية',website0a+'/category/545',132,icon,1)
	addDir('كتب',website0a+'/category/291',132,icon,1)
	addDir('تعلم الفارسية',website0a+'/category/88',132,icon,1)
	addDir('ارشيف البرامج',website0a+'/category/1279',132,icon,1)
	"""
	html = openURL(website0a,'','','','ALKAWTHAR-MENU-1st')
	html_blocks=re.findall('dropdown-menu(.*?)dropdown-toggle',html,re.DOTALL)
	block = html_blocks[1]
	items=re.findall('href="(.*?)">(.*?)<',block,re.DOTALL)
	for link,title in items:
		title = title.strip(' ')
		typeLIST = ['/religious','/social','/political']
		if any(value in link for value in typeLIST):
			title = 'البرامج ' + title
		url = website0a + link
		if '/category' in url:
			addDir(title,url,132,icon,1)
		elif '/conductor' not in url:
			addDir(title,url,131,icon,1)
	"""
	xbmcplugin.endOfDirectory(addon_handle)
	return

"""
def TITLES(url):
	typeLIST = ['/religious','/social','/political','/films','/series']
	html = openURL(url,'','','','ALKAWTHAR-TITLES-1st')
	html_blocks = re.findall('titlebar(.*?)titlebar',html,re.DOTALL)
	block = html_blocks[0]
	if any(value in url for value in typeLIST):
		items = re.findall("src='(.*?)'.*?href='(.*?)'.*?>(.*?)<",block,re.DOTALL)
		for img,link,title in items:
			title = title.strip(' ')
			link = website0a + link
			addDir(title,link,133,img,1)
	elif '/docs' in url:
		items = re.findall("src='(.*?)'.*?<h2>(.*?)</h2>.*?href='(.*?)'",block,re.DOTALL)
		for img,title,link in items:
			title = title.strip(' ')
			link = website0a + link
			addDir(title,link,133,img,1)
	xbmcplugin.endOfDirectory(addon_handle)
	return
"""

def CATEGORIES(url):
	category = url.split('/')[-1]
	html = openURL(url,'','','','ALKAWTHAR-CATEGORIES-1st')
	html_blocks = re.findall('parentcat(.*?)</div>',html,re.DOTALL)
	if not html_blocks:
		EPISODES(url,1)
		return
	block = html_blocks[0]
	items = re.findall("href='(.*?)'.*?>(.*?)<",block,re.DOTALL)
	for link,title in items:
		#categoryNew = url.split('/')[-1]
		#if category==categoryNew: continue
		title = title.strip(' ')
		link = website0a + link
		addDir(title,link,132,icon,1)
	xbmcplugin.endOfDirectory(addon_handle)
	return

def EPISODES(url,page):
	#xbmcgui.Dialog().ok(url, str(page))
	html = openURL(url,'','','','ALKAWTHAR-EPISODES-1st')
	items = re.findall('totalpagecount=[\'"](.*?)[\'"]',html,re.DOTALL)
	if items[0]=='':
		xbmcgui.Dialog().ok('فرع فارغ','لا يوجد حاليا ملفات فيديو في هذا الفرع')
		return
	totalpages = int(items[0])
	name = xbmc.getInfoLabel('ListItem.Label')
	#xbmcgui.Dialog().ok(name, str(''))
	if '/category/' in url:
		category = url.split('/')[-1]
		url2 = website0a + '/category/' + category + '/' + str(page)
		html = openURL(url2,'','','','ALKAWTHAR-EPISODES-3rd')
		html_blocks = re.findall('currentpagenumber(.*?)javascript',html,re.DOTALL)
		block = html_blocks[0]
		items = re.findall('src="(.*?)".*?full(.*?)>.*?href="(.*?)".*?>(.*?)<',block,re.DOTALL)
		for img,type,link,title in items:
			if 'video' not in type: continue
			if 'مسلسل' in title and 'حلقة' not in title: continue
			title = title.replace('\r\n','')
			title = title.strip(' ')
			if 'مسلسل' in name and 'حلقة' in title and 'مسلسل' not in title:
				title = name + ' - ' + title
			link = website0a + link
			if category=='628':
				addDir(title,link,133,img,1)
			else:
				addLink(title,link,134,img)
	elif '/episode/' in url:
		html_blocks = re.findall('playlist(.*?)col-md-12',html,re.DOTALL)
		if html_blocks:
			block = html_blocks[0]
			items = re.findall("video-track-text.*?loadVideo\('(.*?)','(.*?)'.*?>(.*?)<",block,re.DOTALL)
			for link,img,title in items:
				title = title.strip(' ')
				addLink(title,link,134,img)
		elif '/category/628' in html:
				title = 'ملف التشغيل - ' + name
				addLink(title,url,134)
		else:
			items = re.findall('id="Categories.*?href=\'(.*?)\'',html,re.DOTALL)
			category = items[0].split('/')[-1]
			url = website0a + '/category/' + category
			CATEGORIES(url)
			return
		totalpages = 0
		"""
			episodeID = url.split('/')[-1]
			items = re.findall('id="Categories.*?href=\'(.*?)\'',html,re.DOTALL)
			category = items[0].split('/')[-1]
			url2 = website0a + '/ajax/category/' + category + '/' + str(page)
			html = openURL(url2,'','','','ALKAWTHAR-EPISODES-2nd')
			items = re.findall('src="(.*?)".*?href="(.*?)"> <h5>(.*?)<',html,re.DOTALL)
			for img,link,title in items:
				link = website0a + link
				episodeIDnew = link.split('/')[-1]
				if episodeIDnew==episodeID: continue
				title = title.strip(' ')
				addLink(title,link,134,img)
		"""
	title = 'صفحة '
	for i in range(1,1+totalpages):
		if page!=i:
			addDir(title+str(i),url,133,icon,i)
	xbmcplugin.endOfDirectory(addon_handle)
	return

def PLAY(url):
	#xbmcgui.Dialog().ok(url, '')
	if '/news/' in url or '/episode/' in url:
		html = openURL(url,'','','','ALKAWTHAR-PLAY-1st')
		items = re.findall("mobilevideopath.*?value='(.*?)'",html,re.DOTALL)
		url = items[0]
	PLAY_VIDEO(url,script_name,'yes')
	return

def LIVE():
	html = openURL(website0a+'/live','','','','ALKAWTHAR-LIVE-1st')
	items = re.findall('file: "(.*?)"',html,re.DOTALL)
	url = items[0]
	PLAY_VIDEO(url,script_name,'no')
	return

def SEARCH(page):
	search = KEYBOARD()
	if search == '': return
	new_search = search.replace(' ','+')
	url = 'https://www.google.ca/search?q=site:alkawthartv.com+'+new_search+'&start='+str((page-1)*10)
	headers = { 'User-Agent' : '' }
	html = openURL(url,'',headers,'','ALKAWTHAR-SEARCH-1st')
	items = re.findall('rtl" href="/url\?q=(.*?)&.*?>(.*?)</a></h3>',html,re.DOTALL)
	for link,title in items:
		title = title.replace('<b>','').replace('</b>','')
		title = title.replace('\xab','').replace('\xbb','')
		#xbmcgui.Dialog().ok(title, title)
		#xbmc.log('EMAD1 '+title+' 1EMAD',level=xbmc.LOGNOTICE)
		title = unescapeHTML(title)
		if '/category/' in link:	# or '/program/' in link:
			vars = link.split('/')
			category = vars[4]
			url = website0a + '/category/' + category
			if len(vars)>5:
				page1 = vars[5]
				addDir(title,url,133,'',page1)
			else:
				addDir(title,url,132)
		elif '/episode/' in link:
			addDir(title,link,133,'',1)
		#else:
		#	addDir(title,url,132)
	name = 'صفحة '
	for i in range(1,8):
		if i==page: continue
		title = name + ' ' + str(i)
		addDir(title,'',136,icon,i)
	xbmcplugin.endOfDirectory(addon_handle)
	return


