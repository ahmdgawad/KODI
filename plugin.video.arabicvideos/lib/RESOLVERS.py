# -*- coding: utf-8 -*-
from LIBRARY import *
from urlresolver import HostedMediaFile as urlresolver_HostedMediaFile

script_name='RESOLVERS'
doNOTresolveMElist = [ 'mystream','vimple','vidbom' ]

def MAIN(mode,url,text):
	if mode==160: PLAY_LINK(url,text)
	return

def PLAY(linkLIST,script_name):
	serversLIST,urlLIST = SERVERS(linkLIST,script_name)
	#xbmcgui.Dialog().ok('',str(urlLIST))
	#selection = xbmcgui.Dialog().select('اختر السيرفر المناسب:', serversLIST)
	#if selection == -1 : return ''
	if script_name=='HALACIMA': menu_name='[COLOR FFC89008]HLA [/COLOR]'
	elif script_name=='4HELAL': menu_name='[COLOR FFC89008]HEL [/COLOR]'
	elif script_name=='AKOAM': menu_name='[COLOR FFC89008]AKM [/COLOR]'
	elif script_name=='SHAHID4U': menu_name='[COLOR FFC89008]SHA [/COLOR]'
	size = len(urlLIST)
	for i in range(0,size):
		title = serversLIST[i]
		link = urlLIST[i]
		addLink(menu_name+title,link,160,'','','',script_name)
	xbmcplugin.endOfDirectory(addon_handle)
	return

def PLAY_LINK(url,script_name):
	title = xbmc.getInfoLabel( "ListItem.Label" )
	if 'مجهول' in title:
		from PROBLEMS import MAIN as PROBLEMS_MAIN
		PROBLEMS_MAIN(156)
		videoURL = ''
	else:
		videoURL = RESOLVE(url)
		if videoURL==[]:
			videoURL = ''
		else:
			videoURL = videoURL[0]
			PLAY_VIDEO(videoURL,script_name,'yes')
	#xbmcgui.Dialog().ok(str(videoURL),'')
	return videoURL

def CHECK(url):
	result = 'unknown'
	if   '1fichier'		in url: result = 'known'
	elif '4helal'		in url: result = 'known'
	elif 'allmyvideos'	in url: result = 'known'
	elif 'allvid'		in url: result = 'known'
	elif 'bestcima'		in url: result = 'known'
	elif 'cloudy.ec'	in url: result = 'known'
	elif 'dailymotion'	in url: result = 'known'
	elif 'downace'		in url: result = 'known'
	#elif 'estream'		in url: result = 'known'
	elif 'filerio'		in url: result = 'known'
	elif 'firedrive'	in url: result = 'known'
	elif 'flashx'		in url: result = 'known'
	elif 'govid'		in url: result = 'known'
	elif 'hqq'			in url: result = 'known'
	elif 'media4up'		in url: result = 'known'
	elif 'mystream'		in url: result = 'known'
	elif 'nitroflare'	in url: result = 'known'
	elif 'nowvideo'		in url: result = 'known'
	elif 'ok.ru'		in url: result = 'known'
	elif 'oload'		in url: result = 'known'
	elif 'openload'		in url: result = 'known'
	elif 'streamango'	in url: result = 'known'
	elif 'streamin'		in url: result = 'known'
	elif 'streammango'	in url: result = 'known'
	elif 'thevid.net'	in url: result = 'known'
	elif 'upload'		in url: result = 'known'
	elif 'uptobox'		in url: result = 'known'
	elif 'videobam'		in url: result = 'known'
	elif 'videorev'		in url: result = 'known'
	elif 'vidfast'		in url: result = 'known'
	elif 'vidgg'		in url: result = 'known'
	elif 'vidlox'		in url: result = 'known'
	elif 'vidzi'		in url: result = 'known'
	elif 'watchers'		in url: result = 'known'
	elif 'watchers.to'	in url: result = 'known'
	elif 'wintv.live'	in url: result = 'known'
	elif 'youwatch'		in url: result = 'known'
	elif 'vidto.me'		in url: result = 'known'
	elif 'archive'		in url: result = 'known'
	elif 'publicvideohost' in url: result = 'known'
	elif 'vidbom'		in url: result = 'known'
	else:
		link = 'http://emadmahdi.pythonanywhere.com/check?url=' + url
		result = openURL(link,'','','','RESOLVERS-CHECK-1st')
	return result

def RESOLVABLE(url):
	url2 = url.lower()
	result1 = ''
	result2 = ''
	if   any(value in url2 for value in doNOTresolveMElist): return ''
	elif 'go.akoam.net'	in url2 and '?' not in url2: result1 = 'akoam'
	elif 'go.akoam.net'	in url2 and '?' in url2: result2 = url2.split('?')[1]
	elif 'arabloads'	in url2: result1 = 'arabloads'
	elif 'archive'		in url2: result1 = 'archive'
	elif 'catch.is'	 	in url2: result1 = 'catch'
	#elif 'estream'	 	in url2: result1 = 'estream'
	elif 'filerio'		in url2: result1 = 'filerio'
	elif 'go2ooo'		in url2: result1 = 'go2ooo'
	elif 'go2to'		in url2: result1 = 'go2to'
	elif 'gogoo'		in url2: result1 = 'gogoo'
	elif 'gocoo'		in url2: result1 = 'gocoo'
	elif 'golink'	 	in url2: result1 = 'golink'
	elif 'gounlimited'	in url2: result1 = 'gounlimited'
	elif 'govid'		in url2: result1 = 'govid'
	elif 'intoupload' 	in url2: result1 = 'intoupload'
	elif 'liivideo' 	in url2: result1 = 'liivideo'
	elif 'load.is'	 	in url2: result1 = 'load'
	elif 'mp4upload'	in url2: result1 = 'mp4upload'
	elif 'publicvideohost' in url2: result1 = 'publicvideohost'
	elif 'rapidvideo' 	in url2: result1 = 'rapidvideo'
	elif 'thevideo'		in url2: result1 = 'thevideo'
	elif 'top4top'		in url2: result1 = 'top4top'
	elif 'upbom' 		in url2: result1 = 'upbom'
	elif 'uptobox' 		in url2: result1 = 'uptobox'
	elif 'uptostream'	in url2: result1 = 'uptostream'
	elif 'uqload' 		in url2: result1 = 'uqload'
	elif 'vcstream' 	in url2: result1 = 'vcstream'
	elif 'vev.io'	 	in url2: result1 = 'vev'
	elif 'vidbob'		in url2: result1 = 'vidbob'
	elif 'playr.4helal'	in url2: result1 = 'helal'
	#elif 'vidbom'		in url2: result1 = 'vidbom'
	elif 'vidhd' 		in url2: result1 = 'vidhd'
	elif 'vidoza' 		in url2: result1 = 'vidoza'
	elif 'vidshare' 	in url2: result1 = 'vidshare'
	elif 'watchvideo' 	in url2: result1 = 'watchvideo'
	elif 'wintv.live'	in url2: result1 = 'wintv.live'
	elif 'youtu'	 	in url2: result1 = 'youtube'
	elif 'zippyshare'	in url2: result1 = 'zippyshare'
	else:
		resolvable = urlresolver_HostedMediaFile(url).valid_url()
		if resolvable:
			result2 = url.split('//')[1].split('/')[0]
	if result1 in ['akoam','helal']: result = ' سيرفر خاص ' + result1
	elif result1!='': result = ' سيرفر عام معروف ' + result1
	elif result2!='': result = 'سيرفر عام خارجي ' + result2
	else: result = ''
	return result

def RESOLVE(url):
	url2 = url.lower()
	videoURL = []
	if any(value in url2 for value in doNOTresolveMElist): return ''
	elif 'go.akoam.net'	in url2: videoURL = AKOAMNET(url)
	elif 'arabloads'	in url2: videoURL = ARABLOADS(url)
	elif 'archive'		in url2: videoURL = ARCHIVE(url)
	elif 'catch.is'	 	in url2: videoURL = CATCHIS(url)
	#elif 'estream'	 	in url2: videoURL = ESTREAM(url)
	elif 'filerio'		in url2: videoURL = FILERIO(url)
	elif 'go2ooo'		in url2: videoURL = GO2OOO(url)
	elif 'go2to'		in url2: videoURL = GO2TO(url)
	elif 'gogoo'		in url2: videoURL = GOGOO(url)
	elif 'gocoo'		in url2: videoURL = GOCOO(url)
	elif 'golink'	 	in url2: videoURL = GOLINK(url)
	elif 'gounlimited'	in url2: videoURL = GOUNLIMITED(url)
	elif 'govid'		in url2: videoURL = GOVID(url)
	elif 'intoupload' 	in url2: videoURL = INTOUPLOAD(url)
	elif 'liivideo' 	in url2: videoURL = LIIVIDEO(url)
	elif 'load.is'	 	in url2: videoURL = LOADIS(url)
	elif 'mp4upload'	in url2: videoURL = MP4UPLOAD(url)
	elif 'publicvideohost' in url2: videoURL = PUBLICVIDEOHOST(url)
	elif 'rapidvideo' 	in url2: videoURL = RAPIDVIDEO(url)
	elif 'thevideo'		in url2: videoURL = THEVIDEO(url)
	elif 'top4top'		in url2: videoURL = TOP4TOP(url)
	elif 'upbom' 		in url2: videoURL = UPBOM(url)
	elif 'uptobox' 		in url2: videoURL = UPTOBOX(url)
	elif 'uptostream'	in url2: videoURL = UPTOSTREAM(url)
	elif 'uqload' 		in url2: videoURL = UQLOAD(url)
	elif 'vcstream' 	in url2: videoURL = VCSTREAM(url)
	elif 'vev.io'	 	in url2: videoURL = VEVIO(url)
	elif 'playr.4helal'	in url2: videoURL = HELAL(url)
	elif 'vidbob'		in url2: videoURL = VIDBOB(url)
	#elif 'vidbom'		in url2: videoURL = VIDBOM(url)
	elif 'vidhd' 		in url2: videoURL = VIDHD(url)
	elif 'vidoza' 		in url2: videoURL = VIDOZA(url)
	elif 'vidshare' 	in url2: videoURL = VIDSHARE(url)
	elif 'watchvideo' 	in url2: videoURL = WATCHVIDEO(url)
	elif 'wintv.live'	in url2: videoURL = WINTVLIVE(url)
	elif 'youtu'	 	in url2: videoURL = YOUTUBE(url)
	elif 'zippyshare'	in url2: videoURL = ZIPPYSHARE(url)
	else:
		#xbmcgui.Dialog().ok(str(url),str(url2))
		resolvable = urlresolver_HostedMediaFile(url).valid_url()
		if resolvable:
			#xbmcgui.Dialog().ok(str(url),str(url2))
			videoURL = URLRESOLVER(url)
			#xbmcgui.Dialog().ok(str(videoURL),'')
	return videoURL

def SERVERS(linkLIST,script_name=''):
	serversLIST = []
	urlLIST = []
	unknownLIST = []
	serversDICT = []
	message = '\\n'
	linkLIST = set(linkLIST)
	for link in linkLIST:
		if link=='': continue
		link = link.rstrip('/')
		server = RESOLVABLE(link)
		if server=='':
			#xbmcgui.Dialog().ok(link,'')
			if 'akoam' in link and '?' in link:
				serverNAME = 'سيرفر عام مجهول ' + link.split('?')[1]
			else:
				serverNAME = 'سيرفر عام مجهول ' + link.split('//')[1].split('/')[0]
			#if CHECK(link)=='unknown': unknownLIST.append(link)
		else:
			serverNAME = server
		serversDICT.append( [link,serverNAME] )
	sortedDICT = sorted(serversDICT, reverse=False, key=lambda key: key[1])
	for i in range(0,len(sortedDICT)):
		urlLIST.append(sortedDICT[i][0])
		serversLIST.append(sortedDICT[i][1])
	lines = len(unknownLIST)
	if lines>0:
		for link in unknownLIST:
			message += link + '\\n'
		subject = 'Unknown Resolvers = ' + str(lines)
		result = SEND_EMAIL(subject,message,'no','','FROM-RESOLVERS-'+script_name)
	return serversLIST,urlLIST

def	URLRESOLVER(url):
	try: link = urlresolver_HostedMediaFile(url).resolve()
	except: link = False
	if link==False:
		xbmcgui.Dialog().notification('خطأ خارجي','مشكلة في الرابط الاصلي')
		return ['Error']
	return [ link.rstrip('/') ]

def AKOAMNET(link):
	from requests import request as requests_request
	response = requests_request('GET', link, headers='', data='', allow_redirects=False)
	url = response.headers['Location']
	#xbmcgui.Dialog().ok(str(url),'')
	url = GOLINK(url)
	try: url = url[0]
	except:
		url = RESOLVE(url)
		url = url[0]
	if 'catch.is' in url:
		id = url.split('%2F')[-1]
		url = 'http://catch.is/'+id
		url = CATCHIS(url)
		url = url[0]
	else:
		url = url.replace('akoam.net','rmdan.tv')
		url2 = url
		#xbmcgui.Dialog().ok(str(url),'')
		headers = { 'User-Agent':'' , 'X-Requested-With':'XMLHttpRequest' , 'Referer':url }
		response = requests_request('POST', url2, headers=headers, data='', allow_redirects=False)
		html = response.text
		#xbmcgui.Dialog().ok(url2,str(len(html)))
		items = re.findall('direct_link":"(.*?)"',html,re.DOTALL|re.IGNORECASE)
		if not items:
			items = re.findall('<iframe.*?src="(.*?)"',html,re.DOTALL|re.IGNORECASE)
			if not items:
				items = re.findall('<embed.*?src="(.*?)"',html,re.DOTALL|re.IGNORECASE)
		url = items[0].replace('\/','/')
		url = url.rstrip('/')
		if 'http' not in url: url = 'http:' + url
		#xbmcgui.Dialog().ok(str(url),str(link))
		if '?' in link:
			url = RESOLVE(url)
			try: url = url[0]
			except: url = ''
		url1 = url
		#hash_data = re.findall('hash_data":"(.*?)"',html,re.DOTALL|re.IGNORECASE)[0]
		#response = requests_request('GET', url2, headers='', data='', allow_redirects=False)
		#html = response.text
		#watch_title = re.findall('<h1>(.*?)</h1>',html,re.DOTALL|re.IGNORECASE)[0]
		#splits = url2.split('/')
		#server = '/'.join(splits[0:3])
		#url3 = server + '/watching/'+hash_data+'/'+watch_title
		#xbmcgui.Dialog().ok(url1,url3)
	return [ url1.rstrip('/') ]

def RAPIDVIDEO(url):
	headers = { 'User-Agent' : '' }
	html = openURL(url,'',headers,'','RESOLVERS-RAPIDVIDEO-1st')
	#xbmcgui.Dialog().ok(url,html)
	items = re.findall('poster=.*?src="(.*?)"',html,re.DOTALL)
	return [ items[0].rstrip('/') ]

def VIDSHARE(url):
	headers = { 'User-Agent' : '' }
	html = openURL(url,'',headers,'','RESOLVERS-VIDSHARE-1st')
	items = re.findall('file:"(.*?)"',html,re.DOTALL)
	return [ items[0].rstrip('/') ]

def UQLOAD(url):
	headers = { 'User-Agent' : '' }
	html = openURL(url,'',headers,'','RESOLVERS-UQLOAD-1st')
	items = re.findall('sources: \["(.*?)"',html,re.DOTALL)
	#xbmcgui.Dialog().ok(url,items[0])
	return [ items[0].rstrip('/') ]

def VCSTREAM(url):
	id = url.split('/')[-2]
	url = 'https://vcstream.to/player?fid=' + id
	headers = { 'User-Agent' : '' }
	html = openURL(url,'',headers,'','RESOLVERS-VCSTREAM-1st')
	html = html.replace('\\','')
	items = re.findall('file":"(.*?)"',html,re.DOTALL)
	#xbmcgui.Dialog().ok(items[0],items[0])
	return [ items[0].rstrip('/') ]

def VIDOZA(url):
	url = url.replace('embed-','')
	html = openURL(url,'','','','RESOLVERS-VIDOZA-1st')
	items = re.findall('source src="(.*?)"',html,re.DOTALL)
	#xbmcgui.Dialog().ok(str(items),html)
	return [ items[0].rstrip('/') ]

def WATCHVIDEO(url):
	url = url.replace('embed-','')
	html = openURL(url,'','','','RESOLVERS-WATCHVIDEO-1st')
	items = re.findall("Download start.*?download_video\('(.*?)','(.*?)','(.*?)'",html,re.DOTALL)
	for id,mode,hash in items:
		url = 'https://watchvideo.us/dl?op=download_orig&id='+id+'&mode='+mode+'&hash='+hash
		html = openURL(url,'','','','RESOLVERS-WATCHVIDEO-2nd')
	items = re.findall('direct link.*?href="(.*?)"',html,re.DOTALL)
	return [ items[0].rstrip('/') ]

def UPBOM(url):
	id = url.split('/')[-2]
	headers = { 'User-Agent' : '' , 'Content-Type' : 'application/x-www-form-urlencoded' }
	payload = { 'id' : id , 'op' : 'download2' }
	data = urllib.urlencode(payload)
	html = openURL(url,data,headers,'','RESOLVERS-UPBOM-1st')
	#xbmc.log(html, level=xbmc.LOGNOTICE)
	items = re.findall('direct_link.*?href="(.*?)"',html,re.DOTALL)
	return [ items[0].rstrip('/') ]

def LIIVIDEO(url):
	headers = { 'User-Agent' : '' }
	html = openURL(url,'',headers,'','RESOLVERS-LIIVIDEO-1st')
	items = re.findall('file:"(.*?)"',html,re.DOTALL)
	return [ items[0].rstrip('/') ]

def VIDHD(url):
	html = openURL(url,'','','','RESOLVERS-LIIVIDEO-1st')
	items = re.findall('file:"(.*?)"',html,re.DOTALL)
	return [ items[0].rstrip('/') ]

def INTOUPLOAD(url):
	headers = { 'User-Agent' : '' }
	html = openURL(url,'',headers,'','RESOLVERS-INTOUPLOAD-1st')
	html_blocks = re.findall('POST.*?(.*?)clearfix',html,re.DOTALL)
	block = html_blocks[0]
	items = re.findall('op" value="(.*?)".*?id" value="(.*?)".*?rand" value="(.*?)".*?left:(.*?)px;.*?&#(.*?);.*?left:(.*?)px;.*?&#(.*?);.*?left:(.*?)px;.*?&#(.*?);.*?left:(.*?)px;.*?&#(.*?);',block,re.DOTALL)
	for op,id,rand,pos1,num1,pos2,num2,pos3,num3,pos4,num4 in items:
		a=1
	captcha = { int(pos1):chr(int(num1)) , int(pos2):chr(int(num2)) , int(pos3):chr(int(num3)) , int(pos4):chr(int(num4)) }
	code = ''
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
	return [ items[0].rstrip('/') ]

def ESTREAM(url):
	#url = url.replace('embed-','')
	html = openURL(url,'','','','RESOLVERS-ESTREAM-1st')
	items = re.findall('video preload.*?src=.*?src="(.*?)"',html,re.DOTALL)
	#xbmcgui.Dialog().ok(items[0],items[0])
	return [ items[0].rstrip('/') ]

def VEVIO(url):
	id = url.split('/')[-1]
	url = 'https://vev.io/api/serve/video/' + id
	headers = { 'User-Agent' : '' }
	data = '{}'
	html = openURL(url,data,headers,'','RESOLVERS-VEVIO-1st')
	items = re.findall('":"(.*?)"',html,re.DOTALL)
	#xbmcgui.Dialog().ok(url,str(items))
	return [ items[0].rstrip('/') ]

def YOUTUBE(url):
	id = url.split('/')[-1]
	youtubeID = id.split('?')[0]
	url = 'plugin://plugin.video.youtube/play/?video_id='+youtubeID
	return [ url.rstrip('/') ]

def GOLINK(url):
	#id = url.split('/')[-1]
	#url = 'http://golink.to/link/read?hash=' + id
	import requests
	response = requests.request('GET', url, data='', headers='')
	html = response.text
	cookies = response.cookies.get_dict()
	cookie = cookies['golink']
	cookie = unquote(escapeUNICODE(cookie))
	items = re.findall('route":"(.*?)"',cookie,re.DOTALL)
	url = items[0].replace('\/','/')
	url = escapeUNICODE(url)
	return [ url.rstrip('/') ]

def GO2OOO(url):
	url = GOLINK(url)
	url = url[0]
	return [ url.rstrip('/') ]

def GO2TO(url):
	url = GOLINK(url)
	url = url[0]
	return [ url.rstrip('/') ]

def GOGOO(url):
	url = GOLINK(url)
	url = url[0]
	return [ url.rstrip('/') ]

def GOCOO(url):
	url = GOLINK(url)
	url = url[0]
	return [ url.rstrip('/') ]

def LOADIS(url):
	#id = url.split('/')[-1]
	#url = 'http://load.is/link/read?hash=' + id
	#html = openURL(url,'','','','RESOLVERS-LOADIS-1st')
	#items = re.findall('route":"(.*?)"',html,re.DOTALL)
	#url = items[0].replace('\/','/')
	url = GOLINK(url)
	url = url[0]
	return [ url.rstrip('/') ]

def CATCHIS(url):
	id = url.split('/')[-1]
	payload = { 'op' : 'download2' , 'id' : id }
	headers = { 'User-Agent' : '' , 'Content-Type' : 'application/x-www-form-urlencoded' }
	data = urllib.urlencode(payload)
	html = openURL(url,data,headers,'','RESOLVERS-CATCH-1st')
	items = re.findall('direct_link.*?href="(.*?)"',html,re.DOTALL)
	return [ items[0].rstrip('/') ]

def VIDBOM_PROBLEM(url):
	html = openURL(url,'','','','RESOLVERS-VIDBOM-1st')
	xbmc.sleep(1500)
	items = re.findall('file: "(.*?)"',html,re.DOTALL)
	slidesURL = items[0].rstrip('/')
	html2 = openURL(slidesURL,'','','','RESOLVERS-VIDBOM-2nd')
	xbmc.sleep(1500)
	items = re.findall('file:"(.*?)"',html,re.DOTALL)
	return [ items[0].rstrip('/') ]

def HELAL(url):
	headers = { 'User-Agent' : '' }
	#url = url.replace('http:','https:')
	html = openURL(url,'',headers,'','RESOLVERS-VIDBOB-1st')
	items = re.findall('file:"(.*?)"',html,re.DOTALL)
	#xbmcgui.Dialog().ok(items[0].rstrip('/'),'')
	url = items[0].replace('https:','http:')
	return [ url.rstrip('/') ]

def VIDBOB(url):
	headers = { 'User-Agent' : '' }
	#url = url.replace('http:','https:')
	html = openURL(url,'',headers,'','RESOLVERS-VIDBOB-1st')
	items = re.findall('file:"(.*?)"',html,re.DOTALL)
	#xbmcgui.Dialog().ok(items[0].rstrip('/'),'')
	url = items[0].replace('https:','http:')
	return [ url.rstrip('/') ]

def UPTOSTREAM(url):
	headers = { 'User-Agent' : '' }
	html = openURL(url,'',headers,'','RESOLVERS-UPTOSTREAM-1st')
	items = re.findall('src":"(.*?)"',html,re.DOTALL)
	url = items[0].replace('\/','/')
	#xbmcgui.Dialog().ok('load.is',url)
	return [ url.rstrip('/') ]

def ARABLOADS(url):
	html = openURL(url,'','','','RESOLVERS-ARABLOADS-1st')
	items = re.findall('color="red">(.*?)<',html,re.DOTALL)
	return [ items[0].rstrip('/') ]

def TOP4TOP(url):
	return [ url.rstrip('/') ]

def ZIPPYSHARE(url):
	#xbmcgui.Dialog().ok(url,'')
	server = url.split('/')
	basename = '/'.join(server[0:3])
	html = openURL(url,'','','','RESOLVERS-ZIPPYSHARE-1st')
	items = re.findall('dlbutton\'\).href = "(.*?)" \+ \((.*?) \% (.*?) \+ (.*?) \% (.*?)\) \+ "(.*?)"',html,re.DOTALL)
	var1,var2,var3,var4,var5,var6 = items[0]
	var = int(var2) % int(var3) + int(var4) % int(var5)
	url = basename + var1 + str(var) + var6
	#xbmcgui.Dialog().ok(url,str(var))
	return [ url.rstrip('/') ]

def GOUNLIMITED_PROBLEM(url):
	url = url.replace('embed-','')
	headers = { 'User-Agent' : '' }
	html = openURL(url,'',headers,'','RESOLVERS-GOUNLIMITED-1st')
	items = re.findall('data(.*?)hide.*?embed(.*?)hash',html,re.DOTALL)
	id = items[0][0].replace('|','')
	hash = items[0][1].split('|')
	newhash = ''
	for i in reversed(hash):
		newhash += i + '-'
	newhash = newhash.strip('-')
	#url = 'https://gounlimited.to/dl?op=view&file_code='+id+'&hash='+newhash+'&embed=&adb=1'
	#html = openURL(url,'',headers,'','RESOLVERS-GOUNLIMITED-1st')

	from requests import request as requests_request
	url = "https://gounlimited.to/dl"
	querystring = { "op":"view","file_code":"o1yo2xwdmk0l","hash":newhash,"embed":"","adb":"1" }
	headers = {
		'accept': "*/*",
		'dnt': "1",
		'x-requested-with': "XMLHttpRequest",
		'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
		'referer': "https://gounlimited.to/o1yo2xwdmk0l.html",
		'accept-encoding': "gzip, deflate, br",
		'accept-language': "en-US,en;q=0.9,ar;q=0.8"
		}
	html = requests_request('GET', url, headers=headers, params=querystring)

	items = re.findall('video="" src="(.*?)"',html.text,re.DOTALL)
	#xbmcgui.Dialog().ok(str(html.content),str(len(html.content)))
	return [ items[0].rstrip('/') ]

def GOUNLIMITED(url):
	headers = { 'User-Agent' : '' }
	html = openURL(url,'',headers,'','RESOLVERS-GOUNLIMITED-1st')
	items = re.findall('preload\|mp4\|(.*?)\|sources\|Player',html,re.DOTALL)
	url = 'https://shuwaikh.gounlimited.to/'+items[0]+'/v.mp4'
	return [ url.rstrip('/') ]

def UPTOBOX(url):
	headers = { 'User-Agent' : '' }
	html = openURL(url,'',headers,'','RESOLVERS-UPTOBOX-1st')
	#xbmcgui.Dialog().ok(url,html)
	items = re.findall('waitingToken\' value=\'(.*?)\'',html,re.DOTALL)
	if items:
		token = items[0]
		headers = { 'User-Agent' : '' , 'Content-Type' : 'application/x-www-form-urlencoded' }
		payload = { 'waitingToken' : token }
		data = urllib.urlencode(payload)
		progress = xbmcgui.DialogProgress()
		progress.create('Waiting 35 seconds ...')
		for i in range(0,35):
			progress.update(i*100/35,str(35-i))
			xbmc.sleep(1000)
			if progress.iscanceled(): return
		progress.close()
		html = openURL(url,data,headers,'','RESOLVERS-UPTOBOX-2nd')
		#xbmcgui.Dialog().ok(str(html),html)
		#file = open('S:\emad3.html', 'w')
		#file.write(token)
		#file.write('\n\n\n')
		#file.write(html)
		#file.close()
	items = re.findall('comparison-table.*?<a href="(.*?)"',html,re.DOTALL)
	return [ items[0].rstrip('/') ]

def THEVIDEO(url):
	url = url.replace('embed-','')
	html = openURL(url,'','','','RESOLVERS-THEVIDEO-1st')
	items = re.findall('direct link" value="(.*?)"',html,re.DOTALL)
	link = items[0].rstrip('/')
	url = VEVIO(link)
	url = url[0]
	#xbmcgui.Dialog().ok(str(items),html)
	return [ url.rstrip('/') ]

def MP4UPLOAD(url):
	url = url.replace('embed-','')
	url = url.replace('.html','')
	id = url.split('/')[-1]
	headers = { 'Content-Type' : 'application/x-www-form-urlencoded' }
	payload = { "id":id , "op":"download2" }
	from requests import request as requests_request
	request = requests_request('POST', url, headers=headers, data=payload, allow_redirects=False)
	url = request.headers['Location']
	return [ url.rstrip('/') ]

def WINTVLIVE(url):
	html = openURL(url,'','','','RESOLVERS-WINTVLIVE-1st')
	items = re.findall('mp4: \[\'(.*?)\'',html,re.DOTALL)
	return [ items[0].rstrip('/') ]

def	FILERIO(url):
	#xbmc.log(url, level=xbmc.LOGNOTICE)
	id = url.split('/')[-1]
	headers = { 'Content-Type' : 'application/x-www-form-urlencoded' }
	payload = { 'id':id , 'op':'download2' }
	data = urllib.urlencode(payload)
	html = openURL(url,data,headers,'','RESOLVERS-FILERIO-2nd')
	#xbmc.log(html, level=xbmc.LOGNOTICE)
	items = re.findall('direct_link.*?href="(.*?)"',html,re.DOTALL)
	return [ items[0].rstrip('/') ]

def GOVID(url):
	html = openURL(url,'','','','RESOLVERS-GOVID-1st')
	items = re.findall('file:"(.*?)"',html,re.DOTALL)
	return [ items[0].rstrip('/') ]

def VIMPLE_PROBLEM(link):
	id = link.split('id=')[1]
	headers = { 'User-Agent' : '' }
	url = 'http://player.vimple.ru/iframe/' + id
	html = openURL(url,'',headers,'','RESOLVERS-VIMPLE-1st')
	items = re.findall('true,"url":"(.*?)"',html,re.DOTALL)
	url = items[0].replace('\/','/')
	return [ url.rstrip('/') ]

def ARCHIVE(url):
	html = openURL(url,'','','','RESOLVERS-ARCHIVE-1st')
	items = re.findall('source src="(.*?)"',html,re.DOTALL)
	#logging.warning('https://archive.org' + items[0])
	url = 'https://archive.org' + items[0]
	return [ url.rstrip('/') ]

def PUBLICVIDEOHOST(url):
	html = openURL(url,'','','','RESOLVERS-PUBLICVIDEOHOST-1st')
	items = re.findall('file: "(.*?)"',html,re.DOTALL)
	#xbmcgui.Dialog().ok(str(items),html)
	return [ items[0].rstrip('/') ]











