# -*- coding: utf-8 -*-
from LIBRARY import *
import urllib
import requests

website0a = 'http://shoofmax.com'
website0b = 'https://static.shoofmax.com'
website0c = 'https://shoofmax.com'

def MAIN(mode,url):
	if mode==50: MENU()
	elif mode==51: TITLES(url)
	elif mode==52: EPISODES(url)
	elif mode==53: PLAY(url)
	elif mode==54: SEARCH()

def MENU():
	#addDir('بحث في الموقع',website0a,54,icon)
	addDir('افلام بحسب السنة',website0a+'/movie/1/yop',51,icon)
	addDir('افلام بحسب التقييم',website0a+'/movie/1/review',51,icon)
	addDir('افلام بحسب المشاهدة',website0a+'/movie/1/views',51,icon)
	addDir('مسلسلات بحسب السنة',website0a+'/series/1/yop',51,icon)
	addDir('مسلسلات بحسب التقييم',website0a+'/series/1/review',51,icon)
	addDir('مسلسلات بحسب المشاهدة',website0a+'/series/1/views',51,icon)
	xbmcplugin.endOfDirectory(addon_handle)

def TITLES(url):
	info = url.split('/')
	sort = info[ len(info)-1 ]
	page = info[ len(info)-2 ]
	type = info[ len(info)-3 ]
	if type=='movie': type1='فيلم'
	if type=='series': type1='مسلسل'
	url = website0a+'/filter-programs/'+quote(type1)+'/'+page+'/'+sort
	html = openURL(url)
	items = re.findall('"ref":(.*?),.*?"title":"(.*?)".+?"numep":(.*?),"res":"(.*?)"',html,re.DOTALL)
	count_items=0
	for id,title,episodes_number,name in items:
		count_items += 1
		img = website0b + '/img/program/' + name + '-2.jpg'
		link = website0a + '/program/' + id
		if type=='movie': addLink(title,link,53,img)
		if type=='series': addDir(title,link+'?ep='+episodes_number+'='+title+'='+img,52,img)
	title='صفحة '
	if count_items==16:
		for count_page in range(1,13) :
			if not page==str(count_page):
				url = website0a+'/filter-programs/'+type+'/'+str(count_page)+'/'+sort
				addDir(title+str(count_page),url,51,icon)
	xbmcplugin.endOfDirectory(addon_handle)

def EPISODES(url):
	info = url.split('=')
	episodes_number = info[1]
	name = info[2]
	img = info[3]
	info = url.split('?')
	url = info[0]
	#name = xbmc.getInfoLabel( "ListItem.Title" )
	#img = xbmc.getInfoLabel( "ListItem.Thumb" )
	name1 = 'مسلسل '
	name2 = ' - الحلقة '
        for episode in range(int(episodes_number),0,-1):
		link = url + '?ep=' + str(episode)
		title = name1 + name + name2 + str(episode)
		addLink(title,link,53,img)
	xbmcplugin.endOfDirectory(addon_handle)

def PLAY(url):
	html = openURL(url)
	block = re.findall('intro_end(.*?)initialize',html,re.DOTALL)[0]
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
	html = openURL(multiple1)
	base = multiple1.replace('variant.m3u8','')
	items = re.findall('RESOLUTION=(.*?),.*?\n(.*?)u8',html,re.DOTALL)
        for quality,link in items:
		url = base + link + 'u8'
		count += 1
		items_url.append(url)
		items_name.append('Main server: m3u8 '+quality)
	count += 1
	html = openURL(multiple2)
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
	play_item = xbmcgui.ListItem(path=url)
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

	html = openURL(website0c)
	block = re.findall('name="_csrf" value="(.*?)">',html,re.DOTALL)
	csrf = block[0]

	url = website0c + '/search'
	url = "https://shoofmax.com/search"

	#headers = { 'Content-Type': 'application/x-www-form-urlencoded' }
	#payload = { '_csrf' : 'test' , '_csrf' : csrf }

	payload = '_csrf=' + csrf
	#payload = 'q=test&_csrf=' + csrf
	#headers = { 'content-type': 'application/x-www-form-urlencoded' }
	headers = {
	    'origin': "https://shoofmax.com",
	    'upgrade-insecure-requests': "1",
	    'dnt': "1",
	    'content-type': "application/x-www-form-urlencoded",
	    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
	    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
	    'referer': "https://shoofmax.com/",
	    'accept-encoding': "gzip, deflate, br",
	    'accept-language': "en-US,en;q=0.9,ar;q=0.8",
	    'cookie': "session=5ak_HSvwBq8_3vj0BugdPQ.GG6OU4k90qNPndLi51oyyAwzgJPiEIMxh8KJ7Bp39WT1_bOIrguhyyHQRX7psG6hY5l1YP1A2F4KB7DxwABdyp1g_r0JQBhCrB6xZtFDy80.1537480566514.86400000.eQdjvbMrOIYBLzTjXhPCNicnOc3UNBAYpEspiue7a4g; ybjg="
	    }
	#html = requests.request("POST", url, data=payload, headers=headers)

	payload = "{ '_csrf='"+ csrf+" }"
	data = urllib.urlencode(payload)
	html = openURL(url,data,headers)

	#headers = { "content-type": "application/x-www-form-urlencoded" }
	#payload = '{ _csrf :'+ csrf +'}'
	#html = requests.post(url, data=payload, headers=headers, auth='')

	xbmcgui.Dialog().ok(str(url),str(html))

	html_blocks = re.findall('general-body(.*?)search-bottom-padding',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('href="(.*?)".*?background-image: url\((.*?)\).*?<span>(.*?)</span>',block,re.DOTALL)
	for link,img,title in items:
		title = title.replace('\n','')
		link = website0a + link
		addDir(title,link,73,img)
	xbmcplugin.endOfDirectory(addon_handle)



