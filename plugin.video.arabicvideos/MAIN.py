# -*- coding: utf-8 -*-
from lib.LIBRARY import *

def MAIN():
	website1 = 'موقع كل العرب'
	website2 = 'موقع قناة اي فيلم'
	website3 = 'موقع بانيت'
	website4 = 'موقع قناة المعارف'
	website5 = 'موقع شوف ماكس'
	website6 = 'موقع المنبر الفاطمي'
	website0a = '========================='
	website0f = '--------------------------------'
	website0g = 'ـProblems & Solutions       مشاكل وحلول'
	website0d = 'ـMessage to developer       رسالة الى المبرمج'
	addDir(website5,'',50)
	addDir(website3,'',30)
	addDir(website2,'',20)
	addDir(website6,'',60)
	addDir(website4,'',40)
	addDir(website1,'',10)
	addDir(website0a,'',9999)
	addDir(website0d,'',4)
	addDir(website0g,'',1111)
	xbmcplugin.endOfDirectory(addon_handle)

def problemsMENU():
	website0b = 'Problem:   Can\'t see Arabic Text'
	website0c = 'الفيديو لا يظهر في موقع كل العرب   :مشكلة'
	website0d = 'بعض الروابط لا تعمل   :مشكلة'
	addDir(website0b,'',2)
	addDir(website0c,'',3)
	addDir(website0d,'',5)
	xbmcplugin.endOfDirectory(addon_handle)
	


def get_params():
	param=[]
	paramstring=sys.argv[2]
	if len(paramstring)>=2:
		params=sys.argv[2]
		cleanedparams=params.replace('?','')
		if (params[len(params)-1]=='/'):
			params=params[0:len(params)-2]
		pairsofparams=cleanedparams.split('&')
		param={}
		for i in range(len(pairsofparams)):
			splitparams={}
			splitparams=pairsofparams[i].split('=')
			if (len(splitparams))==2:
				param[splitparams[0]]=splitparams[1]
	return param

url=''
mode=''
page=''
category=''
text=''
params=get_params()
try: mode=int(params["mode"])
except: pass
try: url=urllib2.unquote(params["url"])
except: pass
try: page=int(params["page"])
except: pass
try: category=params["category"]
except: pass
try: text=params["text"]
except: pass

if mode=='': MAIN()
if mode==1111: problemsMENU() 
if mode>=0 and mode<=9: from lib.PROGRAM2 import MAIN ; MAIN(mode,text)
if mode>=10 and mode<=19: from lib.ALARAB import MAIN ; MAIN(mode,url)
if mode>=20 and mode<=29: from lib.IFILM import MAIN ; MAIN(mode,url,page)
if mode>=30 and mode<=39: from lib.PANET import MAIN ; MAIN(mode,url)
if mode>=40 and mode<=49: from lib.ALMAAREF import MAIN ; MAIN(mode,url,category)
if mode>=50 and mode<=59: from lib.SHOOFMAX import MAIN ; MAIN(mode,url)
if mode>=60 and mode<=69: from lib.ALFATIMI import MAIN ; MAIN(mode,url,category)



