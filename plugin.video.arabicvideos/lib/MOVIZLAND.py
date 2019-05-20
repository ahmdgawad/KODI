# -*- coding: utf-8 -*-
from LIBRARY import *

website0a = 'http://movizland.online'
website0b = 'http://m.movizland.online'
script_name='MOVIZLAND'
headers = { 'User-Agent' : '' }
menu_name='[COLOR FFC89008]MVZ [/COLOR]'

def MAIN(mode,url,text):
	if mode==180: MENU()
	elif mode==181: ITEMS(url,text)
	elif mode==182: PLAY(url)
	elif mode==183: EPISODES(url)
	elif mode==189: SEARCH(text)
	return

def MENU():
	addDir(menu_name+'بحث في الموقع','',189)
	addDir(menu_name+'بوكس اوفيس موفيز لاند',website0a,181,'','','box-office')
	addDir(menu_name+'أحدث الافلام',website0a,181,'','','latest-movies')
	addDir(menu_name+'تليفزيون موفيز لاند',website0a,181,'','','tv')
	addDir(menu_name+'الاكثر مشاهدة',website0a,181,'','','top-view')
	addDir(menu_name+'أقوى الافلام الحالية',website0a,181,'','','top-movies')
	html = openURL(website0a,'',headers,'','MOVIZLAND-MENU-1st')
	items = re.findall('<h2><a href="(.*?)".*?">(.*?)<',html,re.DOTALL)
	for link,title in items:
		addDir(menu_name+title,link,181)
	#xbmcgui.Dialog().ok(html,html)
	xbmcplugin.endOfDirectory(addon_handle)
	return

def ITEMS(url,type=''):
	html = openURL(url,'',headers,'','MOVIZLAND-ITEMS-1st')
	#xbmc.log(url, level=xbmc.LOGNOTICE)
	if type=='latest-movies':
		block = re.findall('class="titleSection">أحدث الأفلام</h1>(.*?)<h1',html,re.DOTALL)[0]
		items = re.findall('height="3[0-9]+" src="(.*?)".*?bottom-title.*?href="(.*?)".*?>(.*?)<',block,re.DOTALL)
	elif type=='box-office':
		block = re.findall('class="titleSection">بوكس اوفيس موفيز لاند</h1>(.*?)<h1',html,re.DOTALL)[0]
		items = re.findall('height="3[0-9]+" src="(.*?)".*?bottom-title.*?href="(.*?)".*?>(.*?)<',block,re.DOTALL)
	elif type=='tv':
		block = re.findall('class="titleSection">تليفزيون موفيز لاند</h1>(.*?)class="paging"',html,re.DOTALL)[0]
		items = re.findall('height="3[0-9]+" src="(.*?)".*?bottom-title.*?href="(.*?)".*?>(.*?)<',block,re.DOTALL)
	elif type=='top-view':
		block = re.findall('btn-1 btn-absoly(.*?)btn-2 btn-absoly',html,re.DOTALL)[0]
		items = re.findall('style="background-image:url\(\'(.*?)\'.*?href="(.*?)".*?bottom-title.*?>(.*?)<',block,re.DOTALL)
	elif type=='top-movies':
		block = re.findall('btn-2-overlay(.*?)<style>',html,re.DOTALL)[0]
		items = re.findall('style="background-image:url\(\'(.*?)\'.*?href="(.*?)".*?bottom-title.*?>(.*?)<',block,re.DOTALL)
	else:
		items = re.findall('height="3[0-9]+" src="(.*?)".*?bottom-title.*?href="(.*?)".*?>(.*?)<',html,re.DOTALL)
	allTitles = []
	itemLIST = ['فيلم','الحلقة','الحلقه','عرض','Raw','SmackDown','اعلان']
	for img,link,title in items:
		link = unquote(link)
		link = link.replace('?view=true','')
		title = unescapeHTML(title)
		title2 = re.findall('(.*?)(بجودة|بجوده)',title,re.DOTALL)
		if title2: title = title2[0][0]
		if 'الحلقة' in title or 'الحلقه' in title:
			episode = re.findall('(.*?) (الحلقة|الحلقه) [0-9]+',title,re.DOTALL)
			if episode:
				title = '[COLOR FFC89008]Mod [/COLOR]'+episode[0][0]
				if title not in allTitles:
					addDir(menu_name+title,link,183,img)
					allTitles.append(title)
		elif any(value in title for value in itemLIST) and 'اجزاء' not in title:
			addLink(menu_name+title,link,182,img)
		else:
			addDir(menu_name+title,link,183,img)
	if type=='':
		items = re.findall('\n<li><a href="(.*?)".*?>(.*?)<',html,re.DOTALL)
		for link,title in items:
			title = unescapeHTML(title)
			title = title.replace('الصفحة ','')
			if title!='':
				addDir(menu_name+'صفحة '+title,link,181)
	xbmcplugin.endOfDirectory(addon_handle)
	return

def EPISODES(url):
	html = openURL(url,'',headers,'','MOVIZLAND-EPISODES-1st')
	block = re.findall('<title>(.*?)</title>.*?height="([0-9]+)" src="(.*?)"',html,re.DOTALL)
	title = block[0][0]
	img = block[0][2]
	name = re.findall('(.*?) (الحلقة|الحلقه) [0-9]+',title,re.DOTALL)
	if name: name = name[0][0]
	else: name = title
	items = []
	html_blocks = re.findall('class="episodesNumbers"(.*?)</div>',html,re.DOTALL)
	if html_blocks:
		#xbmcgui.Dialog().ok(url,str(html_blocks))
		block = html_blocks[0]
		items = re.findall('href="(.*?)"',block,re.DOTALL)
		for link in items:
			link = unquote(link)
			title = re.findall('(الحلقة|الحلقه)-([0-9]+)',link.split('/')[-2],re.DOTALL)
			if not title:
				title = re.findall('()-([0-9]+)',link.split('/')[-2],re.DOTALL)
			if title: title = ' ' + title[0][1]
			else: title = ''
			title = name + ' - ' + 'الحلقة' + title
			title = unescapeHTML(title)
			addLink(menu_name+title,link,182,img)
	if not items:
		title = unescapeHTML(title)
		title2 = re.findall('(.*?)(بجودة|بجوده)',title,re.DOTALL)
		if title2: title = title2[0][0]
		addLink(menu_name+title,url,182,img)
	xbmcplugin.endOfDirectory(addon_handle)
	return

def PLAY(url):
	import xbmcaddon
	settings = xbmcaddon.Addon(id=addon_id)
	previous_url = settings.getSetting('previous.url')
	if url==previous_url:
		linkLIST = settings.getSetting('previous.linkLIST')
		linkLIST = linkLIST[1:-1].replace('&apos;','').replace(' ','').replace("'",'')
		linkLIST = linkLIST.split(',')
		#xbmcgui.Dialog().ok(url,str(linkLIST))
	else:
		linkLIST = []
		# main_watch_link
		html = openURL(url,'',headers,'','MOVIZLAND-PLAY-2nd')
		link = re.findall('font-size: 25px;" href="(.*?)"',html,re.DOTALL)[0]
		if 'http://moshahda.online/' in link:
			main_watch_link = link
			linkLIST.append(main_watch_link+'?name=Main')
		elif 'http://vb.movizland.online/' in link:
			html = openURL(link,'',headers,'','MOVIZLAND-PLAY-3rd')
			#xbmc.log(html, level=xbmc.LOGNOTICE)
			items = re.findall('href="(http://moshahda.online/.*?.html)".*?>([^<>]+)<',html,re.DOTALL)
			if len(items)==1:
				main_watch_link = items[0][0]
				items = re.findall('>([\n\w]+[ \w]*)(|</font></font></font>)<br /> .*?<a rel="nofollow" href="(http://e5tsar.*?)"',html,re.DOTALL)
				for title,dummy,link in items:
					title = title.replace('\n','')
					link = link + '?name=' + title
					linkLIST.append(link)
			else:
				titleLIST2 = []
				linkLIST2 = []
				for link,title in items:
					title = title.decode('windows-1256')
					titleLIST2.append(title)
					linkLIST2.append(link)
				selection = xbmcgui.Dialog().select('اختر الملف المناسب:', titleLIST2)
				if selection == -1 : return ''
				main_watch_link = linkLIST2[selection]
			linkLIST.append(main_watch_link+'?name=Main')
		else: main_watch_link = ''
		# mobile_watch_link
		url2 = url.replace(website0a,website0b)
		html = openURL(url2,'',headers,'','MOVIZLAND-PLAY-1st')
		id2 = re.findall('margin-bottom: 10px;" href=".*?-(.*?)-.*?.html',html,re.DOTALL)
		if id2:
			if id2[0]!='':
				mobile_watch_link = 'http://moshahda.online/' + id2[0] + '.html'
				if main_watch_link!=mobile_watch_link and main_watch_link!='':
					linkLIST.append(mobile_watch_link+'?name=Mobile')
		settings.setSetting('previous.url',url)
		settings.setSetting('previous.linkLIST',str(linkLIST))
	if len(linkLIST)==0:
		xbmcgui.Dialog().ok('مشكلة','غير قادر على ايجاد ملف الفيديو المناسب')
	else:
		#selection = xbmcgui.Dialog().select('اختر الفلتر المناسب:', linkLIST)
		#if selection == -1 : return ''
		from RESOLVERS import PLAY as RESOLVERS_PLAY
		RESOLVERS_PLAY(linkLIST,script_name)
	return ''

def SEARCH(search):
	if search=='': search = KEYBOARD()
	if search == '': return
	search = search.replace(' ','+')
	html = openURL(website0a,'',headers,'','MOVIZLAND-SEARCH-1st')
	items = re.findall('<option value="(.*?)">(.*?)</option>',html,re.DOTALL)
	categoryLIST = [ '' ]
	filterLIST = [ 'الكل وبدون فلتر' ]
	for category,title in items:
		categoryLIST.append(category)
		filterLIST.append(title)
	selection = xbmcgui.Dialog().select('اختر الفلتر المناسب:', filterLIST)
	if selection == -1 : return
	category = categoryLIST[selection]
	url = website0a + '/?s='+search+'&mcat='+category
	#xbmcgui.Dialog().ok(url,url)
	ITEMS(url)
	return

