# -*- coding: utf-8 -*-
from LIBRARY import *
from urlresolver import HostedMediaFile as urlresolver_HostedMediaFile

script_name='RESOLVERS'
notResolvableLIST = [ 'mystream' ]

"""
def RESOLVABLE_OLD(url):
	result = 44
	if 'akoam.net' 		in url and '?' not in url: result = 1
	elif 'rapidvideo' 	in url: result = 2
	elif 'uptobox' 		in url: result = 3
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
	elif 'arabloads'	in url: result = 23
	elif 'top4top'		in url: result = 24
	elif 'zippyshare'	in url: result = 25
	elif 'gounlimited'	in url: result = 26
	elif 'thevideo'		in url: result = 27
	elif 'mp4upload'	in url: result = 28
	return result

def SERVERS_OLD(linkLIST,script_name=''):
	serversLIST = []
	urlLIST = []
	unknownLIST = ''
	serversSTATUS = []
	serversDICT = {}
	linkLIST = set(linkLIST)
	for i in range(0,44):
		serversSTATUS.append('')
	for link in linkLIST:
		server = RESOLVABLE(link)
		if server<10: serverNum = '0' + str(server)
		else: serverNum = str(server)
		#xbmcgui.Dialog().ok(link,serverNum)
		serversDICT[serverNum+serversSTATUS[server]] = link
		if serversSTATUS[server]=='': serversSTATUS[server] = 'a'
		else: serversSTATUS[server] = chr(ord(serversSTATUS[server])+1)
	sortedList = sorted(serversDICT.keys())
	for i in sortedList:
		if i[0:2]=='44':
			serversLIST.append('سيرفر مجهول ' + SERVERNAME(serversDICT[i]))
			if CHECK(serversDICT[i])=='unknown':
				unknownLIST += serversDICT[i]+'\\n'
		else: serversLIST.append('سيرفر ' + SERVERNAME(serversDICT[i]))
		urlLIST.append(serversDICT[i])
	lines = len(unknownLIST.split('\\n'))-1
	#xbmcgui.Dialog().ok(str(lines),'')
	if lines>0:
		message = '\\n'+unknownLIST
		subject = 'Unknown Resolvers = ' + str(lines)
		result = SEND_EMAIL(subject,message,'no','','FROM-RESOLVERS-'+script_name)
	return serversLIST,urlLIST
"""

def CHECK(link):
	url = 'http://emadmahdi.pythonanywhere.com/check?url='
	result = openURL(url+link,'','','','RESOLVERS-CHECK-1st')
	return result

def RESOLVABLE(url):
	result1 = ''
	result2 = ''
	if any(value in url for value in notResolvableLIST): return ''
	elif 'go.akoam.net'	in url and '?' not in url: result1 = 'akoam'
	elif 'go.akoam.net'	in url and '?estream' in url: result1 = 'estream'
	elif 'go.akoam.net'	in url and '?' in url: result2 = url.split('?')[1]
	elif 'rapidvideo' 	in url: result1 = 'rapidvideo'
	elif 'uptobox' 		in url: result1 = 'uptobox'
	elif 'vidshare' 	in url: result1 = 'vidshare'
	elif 'uqload' 		in url: result1 = 'uqload'
	elif 'vcstream' 	in url: result1 = 'vcstream'
	elif 'vidoza' 		in url: result1 = 'vidoza'
	elif 'watchvideo' 	in url: result1 = 'watchvideo'
	elif 'upbom' 		in url: result1 = 'upbom'
	elif 'liivideo' 	in url: result1 = 'liivideo'
	elif 'vidhd' 		in url: result1 = 'vidhd'
	elif 'intoupload' 	in url: result1 = 'intoupload'
	elif 'estream'	 	in url: result1 = 'estream'
	elif 'vev.io'	 	in url: result1 = 'vev'
	elif 'youtu'	 	in url: result1 = 'youtube'
	elif 'catch.is'	 	in url: result1 = 'catch'
	elif 'load.is'	 	in url: result1 = 'load'
	elif 'golink'	 	in url: result1 = 'golink'
	elif 'go2ooo'		in url: result1 = 'go2ooo'
	elif 'vidbom'		in url: result1 = 'vidbom'
	elif 'vidbob'		in url: result1 = 'vidbob'
	elif 'uptostream'	in url: result1 = 'uptostream'
	elif 'arabloads'	in url: result1 = 'arabloads'
	elif 'top4top'		in url: result1 = 'top4top'
	elif 'zippyshare'	in url: result1 = 'zippyshare'
	elif 'gounlimited'	in url: result1 = 'gounlimited'
	elif 'thevideo'		in url: result1 = 'thevideo'
	elif 'mp4upload'	in url: result1 = 'mp4upload'
	elif 'wintv.live'	in url: result1 = 'wintv.live'
	elif 'filerio'		in url: result1 = 'filerio'
	else:
		resolvable = urlresolver_HostedMediaFile(url).valid_url()
		if resolvable:
			result2 = url.split('//')[1].split('/')[0]
	if result1!='': result = '1. '+'سيرفر محلي ' + result1
	elif result2!='': result = '2. '+'سيرفر غريب ' + result2
	else: result = ''
	return result

def RESOLVE(url):
	videoURL = ''
	if any(value in url for value in notResolvableLIST): return ''
	elif 'go.akoam.net'	in url: videoURL = AKOAMNET(url)
	elif 'rapidvideo' 	in url: videoURL = RAPIDVIDEO(url)
	elif 'uptobox' 		in url: videoURL = UPTOBOX(url)
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
	elif 'arabloads'	in url: videoURL = ARABLOADS(url)
	elif 'top4top'		in url: videoURL = TOP4TOP(url)
	elif 'zippyshare'	in url: videoURL = ZIPPYSHARE(url)
	elif 'gounlimited'	in url: videoURL = GOUNLIMITED(url)
	elif 'thevideo'		in url: videoURL = THEVIDEO(url)
	elif 'mp4upload'	in url: videoURL = MP4UPLOAD(url)
	elif 'wintv.live'	in url: videoURL = WINTVLIVE(url)
	elif 'filerio'		in url: videoURL = FILERIO(url)
	else:
		resolvable = urlresolver_HostedMediaFile(url).valid_url()
		if resolvable:
			videoURL = URLRESOLVER(url)
	return videoURL

def SERVERS(linkLIST,script_name=''):
	serversLIST = []
	urlLIST = []
	unknownLIST = []
	serversDICT = []
	message = '\\n'
	linkLIST = set(linkLIST)
	for link in linkLIST:
		server = RESOLVABLE(link)
		if server=='':
			serverNAME = '3. ' + 'سيرفر مجهول ' + link.split('//')[1].split('/')[0]
			if CHECK(link)=='unknown':
				unknownLIST.append(link)
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

def PLAY(linkLIST,script_name,play='yes'):
	serversLIST,urlLIST = SERVERS(linkLIST,script_name)
	selection = xbmcgui.Dialog().select('اختر السيرفر المناسب:', serversLIST)
	if selection == -1 : return ''
	url = urlLIST[selection]
	videoURL = RESOLVE(url)
	if videoURL=='':
		import PROBLEMS
		PROBLEMS.MAIN(1006)
	elif play=='yes': PLAY_VIDEO(videoURL,script_name)
	return videoURL

def	URLRESOLVER(url):
	link = 'Error'
	try: link = urlresolver_HostedMediaFile(url).resolve()
	except: xbmcgui.Dialog().notification('خطأ خارجي','الرابط ليس فيديو')
	return link

def RAPIDVIDEO(url):
	headers = { 'User-Agent' : '' }
	html = openURL(url,'',headers,'','RESOLVERS-RAPIDVIDEO-1st')
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
	return items[0]

def ESTREAM(url):
	html = openURL(url,'','','','RESOLVERS-ESTREAM-1st')
	items = re.findall('video preload.*?src=.*?src="(.*?)"',html,re.DOTALL)
	#xbmcgui.Dialog().ok(str(items),html)
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
	html = openURL(url,'','','','RESOLVERS-LOADIS-1st')
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
	html = openURL(url,'','','','RESOLVERS-GO2OOO-1st')
	items = re.findall('route":"(.*?)"',html,re.DOTALL)
	url = items[0].replace('\/','/')
	#xbmcgui.Dialog().ok('load.is',url)
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

def ARABLOADS(url):
	html = openURL(url,'','','','RESOLVERS-ARABLOADS-1st')
	items = re.findall('color="red">(.*?)<',html,re.DOTALL)
	return url

def TOP4TOP(url):
	return url

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
	return url

def GOUNLIMITED_TEST(url):
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

	import requests
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
	html = requests.request("GET", url, headers=headers, params=querystring)

	items = re.findall('video="" src="(.*?)"',html.text,re.DOTALL)
	#xbmcgui.Dialog().ok(str(html.content),str(len(html.content)))
	return items[0]

def GOUNLIMITED(url):
	headers = { 'User-Agent' : '' }
	html = openURL(url,'',headers,'','RESOLVERS-GOUNLIMITED-1st')
	items = re.findall('preload\|mp4\|(.*?)\|sources\|Player',html,re.DOTALL)
	url = 'https://shuwaikh.gounlimited.to/'+items[0]+'/v.mp4'
	return url

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
	return items[0]

def THEVIDEO(url):
	url = url.replace('embed-','')
	html = openURL(url,'','','','RESOLVERS-THEVIDEO-1st')
	items = re.findall('direct link" value="(.*?)"',html,re.DOTALL)
	link = items[0]
	url = VEVIO(link)
	#xbmcgui.Dialog().ok(str(items),html)
	return url

def MP4UPLOAD(url):
	url = url.replace('embed-','')
	url = url.replace('.html','')
	id = url.split('/')[-1]
	headers = { 'Content-Type' : 'application/x-www-form-urlencoded' }
	payload = { "id":id , "op":"download2" }
	import requests
	request = requests.post(url, headers=headers, data=payload, allow_redirects=False)
	return request.headers['Location']

def WINTVLIVE(url):
	html = openURL(url,'','','','RESOLVERS-WINTVLIVE-1st')
	items = re.findall('mp4: \[\'(.*?)\'',html,re.DOTALL)
	link = items[0]
	return link

def AKOAMNET(link):
	#xbmcgui.Dialog().ok(link,link)
	id = link.split('/')[-1].split('?')[0]
	url = 'http://load.is/' + id
	url = LOADIS(url)
	if 'catch.is' in url:
		id = url.split('%2F')[-1]
		url = 'http://catch.is/'+id
		url = CATCHIS(url)
	else:
		headers = { 'User-Agent':'' , 'X-Requested-With':'XMLHttpRequest' , 'Referer':url }
		html = openURL(url,'',headers,'','AKOAM-RESOLVE_AKOAM-1st')
		items = re.findall('<IFRAME.*?SRC="(.*?)"',html,re.DOTALL)
		if not items: 
			items = re.findall('<iframe.*?src="(.*?)"',html,re.DOTALL)
			if not items:
				items = re.findall('direct_link":"(.*?)"',html,re.DOTALL)
		url = items[0].replace('\/','/')
		if 'http' not in url: url = 'http:' + url
		#xbmcgui.Dialog().ok(url,url)
		if '?' in link: url = RESOLVE(url)
	return url

def	FILERIO(url):
	id = url.split('/')[-1]
	headers = { 'Content-Type' : 'application/x-www-form-urlencoded' }
	payload = { 'id':id , 'op':'download2' }
	data = urllib.urlencode(payload)
	html = openURL(url,data,headers,'','RESOLVERS-FILERIO-2nd')
	items = re.findall('direct_link.*?href="(.*?)"',html,re.DOTALL)
	return items[0]



