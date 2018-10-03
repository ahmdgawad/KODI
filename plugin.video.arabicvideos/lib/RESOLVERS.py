# -*- coding: utf-8 -*-
from LIBRARY import *

script_name='RESOLVERS'

def SERVERS(urlLIST):
	serverLIST = []
	for i in range(0,220):
		serverLIST.append('')
	for url in urlLIST:
		if   'vidbom' 		in url 	and serverLIST[1]=='': 	serverLIST[1] = url
		elif 'rapidvideo' 	in url 	and serverLIST[2]=='': 	serverLIST[2] = url
		elif 'mystream' 	in url 	and serverLIST[3]=='': 	serverLIST[3] = url
		elif 'vidshare' 	in url 	and serverLIST[4]=='': 	serverLIST[4] = url
		elif 'uqload' 		in url 	and serverLIST[5]=='': 	serverLIST[5] = url
		elif 'vcstream' 	in url 	and serverLIST[6]=='': 	serverLIST[6] = url
		elif 'vidoza' 		in url 	and serverLIST[7]=='': 	serverLIST[7] = url
		elif 'watchvideo' 	in url 	and serverLIST[8]=='': 	serverLIST[8] = url
		elif 'upbom' 		in url 	and serverLIST[9]=='': 	serverLIST[9] = url
		elif 'liivideo' 	in url 	and serverLIST[10]=='': serverLIST[10] = url
		elif 'vidhd' 		in url 	and serverLIST[11]=='': serverLIST[11] = url
		elif 'intoupload' 	in url 	and serverLIST[12]=='': serverLIST[12] = url
		elif 'estream'	 	in url 	and serverLIST[13]=='': serverLIST[13] = url
		elif 'vev.io'	 	in url 	and serverLIST[14]=='': serverLIST[14] = url

		elif 'vidbom' 		in url 	and serverLIST[101]=='': serverLIST[101] = url
		elif 'rapidvideo' 	in url 	and serverLIST[102]=='': serverLIST[102] = url
		elif 'mystream' 	in url 	and serverLIST[103]=='': serverLIST[103] = url
		elif 'vidshare' 	in url 	and serverLIST[104]=='': serverLIST[104] = url
		elif 'uqload' 		in url 	and serverLIST[105]=='': serverLIST[105] = url
		elif 'vcstream' 	in url 	and serverLIST[106]=='': serverLIST[106] = url
		elif 'vidoza' 		in url 	and serverLIST[107]=='': serverLIST[107] = url
		elif 'watchvideo' 	in url 	and serverLIST[108]=='': serverLIST[108] = url
		elif 'upbom' 		in url 	and serverLIST[109]=='': serverLIST[109] = url
		elif 'liivideo' 	in url 	and serverLIST[110]=='': serverLIST[110] = url
		elif 'vidhd' 		in url 	and serverLIST[111]=='': serverLIST[111] = url
		elif 'intoupload' 	in url 	and serverLIST[112]=='': serverLIST[112] = url
		elif 'estream'	 	in url 	and serverLIST[113]=='': serverLIST[113] = url
		elif 'vev.io'	 	in url 	and serverLIST[114]=='': serverLIST[114] = url

		elif 'vidbom' 		in url 	and serverLIST[201]=='': serverLIST[201] = url
		elif 'rapidvideo' 	in url 	and serverLIST[202]=='': serverLIST[202] = url
		elif 'mystream' 	in url 	and serverLIST[203]=='': serverLIST[203] = url
		elif 'vidshare' 	in url 	and serverLIST[204]=='': serverLIST[204] = url
		elif 'uqload' 		in url 	and serverLIST[205]=='': serverLIST[205] = url
		elif 'vcstream' 	in url 	and serverLIST[206]=='': serverLIST[206] = url
		elif 'vidoza' 		in url 	and serverLIST[207]=='': serverLIST[207] = url
		elif 'watchvideo' 	in url 	and serverLIST[208]=='': serverLIST[208] = url
		elif 'upbom' 		in url 	and serverLIST[209]=='': serverLIST[209] = url
		elif 'liivideo' 	in url 	and serverLIST[210]=='': serverLIST[210] = url
		elif 'vidhd' 		in url 	and serverLIST[211]=='': serverLIST[211] = url
		elif 'intoupload' 	in url 	and serverLIST[212]=='': serverLIST[212] = url
		elif 'estream'	 	in url 	and serverLIST[213]=='': serverLIST[213] = url
		elif 'vev.io'	 	in url 	and serverLIST[214]=='': serverLIST[214] = url
	return serverLIST

def VIDEO_URL(url):
	videoURL = ''
	if   'vidbom' 		in url: videoURL = VIDBOM(url)
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
	return videoURL

def VIDBOM(url):
	html = openURL(url,'','','','RESOLVERS-VIDBOM-1st')
	items = re.findall('file:"(.*?)"',html,re.DOTALL)
	return items[0]

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
	url = 'http://vcstream.to/player?fid=' + id
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



