# -*- coding: utf-8 -*-
from LIBRARY import *

script_name='RESOLVERS'

def RESOLVABLE(url):
	result = 0
	if 'akoam.net' in url and '?' not in url: result = 1
	elif 'rapidvideo' 	in url: result = 2
	elif 'mystream' 	in url: result = 3
	elif 'vidshare' 	in url: result = 4
	elif 'uqload' 		in url: result = 5
	elif 'vcstream' 	in url: result = 6
	elif 'vidoza' 		in url: result = 7
	elif 'watchvideo' 	in url: result = 8
	elif 'upbom' 		in url: result = 9
	elif 'liivideo' 	in url: result = 10
	elif 'vidhd' 		in url: result = 11
	elif 'intoupload' 	in url: result = 12
	elif 'estream'	 	in url: result = 13
	elif 'vev.io'	 	in url: result = 14
	elif 'youtu'	 	in url: result = 15
	elif 'catch.is'	 	in url: result = 16
	elif 'load.is'	 	in url: result = 17
	elif 'golink'	 	in url: result = 18
	elif 'go2ooo'		in url: result = 19
	elif 'vidbom'		in url: result = 20
	elif 'vidbob'		in url: result = 21
	elif 'uptostream'	in url: result = 22
	return result

def RESOLVE(url):
	videoURL = ''
	if 'akoam.net' in url and '?' not in url: videoURL = AKOAMNET(url)
	elif 'rapidvideo' 	in url: videoURL = RAPIDVIDEO(url)
	elif 'mystream' 	in url: videoURL = MYSTREAM(url)
	elif 'vidshare' 	in url: videoURL = VIDSHARE(url)
	elif 'uqload' 		in url: videoURL = UQLOAD(url)
	elif 'vcstream' 	in url: videoURL = VCSTREAM(url)
	elif 'vidoza' 		in url: videoURL = VIDOZA(url)
	elif 'watchvideo' 	in url: videoURL = WATCHVIDEO(url)
	elif 'upbom' 		in url: videoURL = UPBOM(url)
	elif 'liivideo' 	in url: videoURL = LIIVIDEO(url)
	elif 'vidhd' 		in url: videoURL = VIDHD(url)
	elif 'intoupload' 	in url: videoURL = INTOUPLOAD(url)
	elif 'estream'	 	in url: videoURL = ESTREAM(url)
	elif 'vev.io'	 	in url: videoURL = VEVIO(url)
	elif 'youtu'	 	in url: videoURL = YOUTUBE(url)
	elif 'catch.is'	 	in url: videoURL = CATCHIS(url)
	elif 'load.is'	 	in url: videoURL = LOADIS(url)
	elif 'golink'	 	in url: videoURL = GOLINK(url)
	elif 'go2ooo'		in url: videoURL = GO2OOO(url)
	elif 'vidbom'		in url: videoURL = VIDBOM(url)
	elif 'vidbob'		in url: videoURL = VIDBOB(url)
	elif 'uptostream'	in url: videoURL = UPTOSTREAM(url)
	return videoURL

def SERVERS(linkLIST):
	serversLIST = []
	urlLIST = []
	serversSTATUS = []
	serversDICT = {}
	linkLIST = set(linkLIST)
	for i in range(0,25):
		serversSTATUS.append('')
	for link in linkLIST:
		server = RESOLVABLE(link)
		if server>0:
			if server<10: serverNum = '0' + str(server)
			else: serverNum = str(server)
			serversDICT[serverNum+serversSTATUS[server]] = link
			if serversSTATUS[server]=='': serversSTATUS[server] = 'a'
			else: serversSTATUS[server] = chr(ord(serversSTATUS[server])+1)
	for i in sorted(serversDICT.keys()):
		serversLIST.append('سيرفر '+i)
		urlLIST.append(serversDICT[i])
	return serversLIST,urlLIST

def PLAY(linkLIST,script_name,play='yes'):
	serversLIST,urlLIST = SERVERS(linkLIST)
	selection = xbmcgui.Dialog().select('اختر السيرفر المناسب:', serversLIST)
	if selection == -1 : return
	url = urlLIST[selection]
	videoURL = RESOLVE(url)
	#xbmcgui.Dialog().ok(url,'')
	if play=='yes': PLAY_VIDEO(videoURL,script_name)
	return videoURL

def RAPIDVIDEO(url):
	headers = { 'User-Agent' : '' }
	html = openURL(url,'',headers,'','RESOLVERS-RAPIDVIDEO-1st')
	items = re.findall('poster=.*?src="(.*?)"',html,re.DOTALL)
	return items[0]

def MYSTREAM(url):
	headers = { 'User-Agent' : '' }
	html = openURL(url,'',headers,'','RESOLVERS-MYSTREAM-1st')
	items = re.findall('poster=.*?src="(.*?)"',html,re.DOTALL)
	return items[0]

def VIDSHARE(url):
	headers = { 'User-Agent' : '' }
	html = openURL(url,'',headers,'','RESOLVERS-VIDSHARE-1st')
	items = re.findall('file:"(.*?)"',html,re.DOTALL)
	return items[0]

def UQLOAD(url):
	headers = { 'User-Agent' : '' }
	html = openURL(url,'',headers,'','RESOLVERS-UQLOAD-1st')
	items = re.findall('sources: \["(.*?)"',html,re.DOTALL)
	#xbmcgui.Dialog().ok(url,items[0])
	return items[0]

def VCSTREAM(url):
	id = url.split('/')[-2]
	url = 'https://vcstream.to/player?fid=' + id
	headers = { 'User-Agent' : '' }
	html = openURL(url,'',headers,'','RESOLVERS-VCSTREAM-1st')
	html = html.replace('\\','')
	items = re.findall('file":"(.*?)"',html,re.DOTALL)
	#xbmcgui.Dialog().ok(items[0],items[0])
	return items[0]

def VIDOZA(url):
	url = url.replace('embed-','')
	html = openURL(url,'','','','RESOLVERS-VIDOZA-1st')
	items = re.findall('source src="(.*?)"',html,re.DOTALL)
	#xbmcgui.Dialog().ok(str(items),html)
	return items[0]

def WATCHVIDEO(url):
	url = url.replace('embed-','')
	html = openURL(url,'','','','RESOLVERS-WATCHVIDEO-1st')
	items = re.findall("Download start.*?download_video\('(.*?)','(.*?)','(.*?)'",html,re.DOTALL)
	for id,mode,hash in items:
		url = 'https://watchvideo.us/dl?op=download_orig&id='+id+'&mode='+mode+'&hash='+hash
		html = openURL(url,'','','','RESOLVERS-WATCHVIDEO-2nd')
	items = re.findall('direct link.*?href="(.*?)"',html,re.DOTALL)
	return items[0]

def UPBOM(url):
	id = url.split('/')[-2]
	headers = { 'User-Agent' : '' , 'Content-Type' : 'application/x-www-form-urlencoded' }
	payload = { 'id' : id , 'op' : 'download2' }
	data = urllib.urlencode(payload)
	html = openURL(url,data,headers,'','RESOLVERS-UPBOM-1st')
	items = re.findall('direct_link.*?href="(.*?)"',html,re.DOTALL)
	return items[0]

def LIIVIDEO(url):
	headers = { 'User-Agent' : '' }
	html = openURL(url,'',headers,'','RESOLVERS-LIIVIDEO-1st')
	items = re.findall('file:"(.*?)"',html,re.DOTALL)
	return items[0]

def VIDHD(url):
	html = openURL(url,'','','','RESOLVERS-LIIVIDEO-1st')
	items = re.findall('file:"(.*?)"',html,re.DOTALL)
	return items[0]

def INTOUPLOAD(url):
	headers = { 'User-Agent' : '' }
	html = openURL(url,'',headers,'','RESOLVERS-INTOUPLOAD-1st')
	html_blocks = re.findall('POST.*?(.*?)clearfix',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('op" value="(.*?)".*?id" value="(.*?)".*?rand" value="(.*?)".*?left:(.*?)px;.*?&#(.*?);.*?left:(.*?)px;.*?&#(.*?);.*?left:(.*?)px;.*?&#(.*?);.*?left:(.*?)px;.*?&#(.*?);',block,re.DOTALL)
	code = ''
	for op,id,rand,pos1,num1,pos2,num2,pos3,num3,pos4,num4 in items:
		a=1
	captcha = { int(pos1):chr(int(num1)) , int(pos2):chr(int(num2)) , int(pos3):chr(int(num3)) , int(pos4):chr(int(num4)) }
	for char in sorted(captcha):
		code += captcha[char]
	#xbmcgui.Dialog().ok(code,str(captcha))
	headers = { 'User-Agent' : '' , 'Content-Type' : 'application/x-www-form-urlencoded' }
	payload = { 'id':id , 'op':op , 'code':code , 'rand':rand }
	data = urllib.urlencode(payload)
	progress = xbmcgui.DialogProgress()
	progress.create('Waiting 15 seconds ...')
	for i in range(0,15):
		progress.update(i*100/15,str(15-i))
		xbmc.sleep(1000)
		if progress.iscanceled(): return
	progress.close()
	html = openURL(url,data,headers,'','RESOLVERS-INTOUPLOAD-2nd')
	items = re.findall('target_type.*?href="(.*?)"',html,re.DOTALL)
	return items[0]

def ESTREAM(url):
	html = openURL(url,'','','','RESOLVERS-ESTREAM-1st')
	items = re.findall('video preload.*?src=.*?src="(.*?)"',html,re.DOTALL)
	return items[0]

def VEVIO(url):
	id = url.split('/')[-1]
	url = 'https://vev.io/api/serve/video/' + id
	headers = { 'User-Agent' : '' }
	data = '{}'
	html = openURL(url,data,headers,'','RESOLVERS-VEVIO-1st')
	#xbmcgui.Dialog().ok(url,html)
	items = re.findall('http(.*?)"',html,re.DOTALL)
	return 'http'+items[0]

def YOUTUBE(url):
	id = url.split('/')[-1]
	youtubeID = id.split('?')[0]
	url = 'plugin://plugin.video.youtube/play/?video_id='+youtubeID
	return url

def CATCHIS(url):
	id = url.split('/')[-1]
	payload = { 'op' : 'download2' , 'id' : id }
	headers = { 'User-Agent' : '' , 'Content-Type' : 'application/x-www-form-urlencoded' }
	data = urllib.urlencode(payload)
	html = openURL(url,data,headers,'','RESOLVERS-CATCH-1st')
	items = re.findall('direct_link.*?href="(.*?)"',html,re.DOTALL)
	return items[0]

def LOADIS(url):
	id = url.split('/')[-1]
	url = 'http://load.is/link/read?hash=' + id
	html = openURL(url,'','','','RESOLVERS-LOAD-1st')
	items = re.findall('route":"(.*?)"',html,re.DOTALL)
	url = items[0].replace('\/','/')
	#xbmcgui.Dialog().ok('load.is',str(url))
	return url

def GOLINK(url):
	id = url.split('/')[-1]
	url = 'http://golink.to/link/read?hash=' + id
	html = openURL(url,'','','','RESOLVERS-GOLINK-1st')
	items = re.findall('route":"(.*?)"',html,re.DOTALL)
	url = items[0].replace('\/','/')
	#xbmcgui.Dialog().ok('load.is',str(url))
	return url

def GO2OOO(url):
	id = url.split('/')[-1]
	url = 'http://load.is/link/read?hash=' + id
	html = openURL(url,'','','','RESOLVERS-LOAD-1st')
	items = re.findall('route":"(.*?)"',html,re.DOTALL)
	url = items[0].replace('\/','/')
	#xbmcgui.Dialog().ok('load.is',url)
	return url

def AKOAMNET(url):
	return url

def VIDBOM(url):
	html = openURL(url,'','','','RESOLVERS-VIDBOM-1st')
	xbmc.sleep(1500)
	items = re.findall('file: "(.*?)"',html,re.DOTALL)
	slides = items[0]
	html2 = openURL(slides,'','','','RESOLVERS-VIDBOM-2nd')
	xbmc.sleep(1500)
	items = re.findall('file:"(.*?)"',html,re.DOTALL)
	url = items[0]
	return url

def VIDBOB(url):
	headers = { 'User-Agent' : '' }
	url = url.replace('https:','http:')
	html = openURL(url,'',headers,'','RESOLVERS-VIDBOB-1st')
	items = re.findall('file:"(.*?)"',html,re.DOTALL)
	return items[0]

def UPTOSTREAM(url):
	headers = { 'User-Agent' : '' }
	html = openURL(url,'',headers,'','RESOLVERS-UPTOSTREAM-1st')
	items = re.findall('src":"(.*?)"',html,re.DOTALL)
	url = items[0].replace('\/','/')
	#xbmcgui.Dialog().ok('load.is',url)
	return url


