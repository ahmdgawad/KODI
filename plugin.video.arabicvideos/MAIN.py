# -*- coding: utf-8 -*-
from lib.LIBRARY import *

def MAIN():
	website4 = 'موقع قناة المعارف' + '   .9'
	website6 = 'موقع المنبر الفاطمي' + '   .8'
	website2 = 'موقع قناة اي فيلم' + '   .7'
	website7 = 'موقع اكوام' + '   .6'
	website5 = 'موقع شوف ماكس' + '   .5'
	website1 = 'موقع كل العرب' + '   .4'
	website3 = 'موقع بانيت' + '   .3'
	website8 = 'موقع هلا سيما' + '   .2'
	website9 = 'موقع هلال يوتيوب' + '   .1'
	website0a = '========================='
	website0b = 'ـProblems & Solutions    مشاكل وحلول' + '   .12'
	website0c = 'ـMessage to developer    رسالة الى المبرمج' + '   .11'
	website0d = 'ـ DMCA     قانون الألفية للملكية الرقمية' + '   .10'
	website0z = 'Testing'
	#addLink(website0z,'',9)
	addDir(website0b,'',1000)
	addDir(website0c,'',2)
	addDir(website0d,'',3)
	#addDir(website0a,'',9999)
	addDir(website4,'',40)
	addDir(website6,'',60)
	addDir(website2,'',20)
	addDir(website7,'',70)
	addDir(website5,'',50)
	addDir(website1,'',10)
	addDir(website3,'',30)
	addDir(website8,'',80)
	addDir(website9,'',90)
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
elif mode>=10 and mode<=19: from lib.ALARAB import MAIN ; MAIN(mode,url)
elif mode>=20 and mode<=29: from lib.IFILM import MAIN ; MAIN(mode,url,page)
elif mode>=30 and mode<=39: from lib.PANET import MAIN ; MAIN(mode,url)
elif mode>=40 and mode<=49: from lib.ALMAAREF import MAIN ; MAIN(mode,url,category)
elif mode>=50 and mode<=59: from lib.SHOOFMAX import MAIN ; MAIN(mode,url)
elif mode>=60 and mode<=69: from lib.ALFATIMI import MAIN ; MAIN(mode,url,category)
elif mode>=70 and mode<=79: from lib.AKOAM import MAIN ; MAIN(mode,url)
elif mode>=80 and mode<=89: from lib.HALACIMA import MAIN ; MAIN(mode,url,page)
elif mode>=90 and mode<=99: from lib._4HELAL import MAIN ; MAIN(mode,url)

elif mode>=0 and mode<=9: from lib.PROGRAM import MAIN ; MAIN(mode,text)
elif mode>=1000 and mode<=1009: from lib.PROBLEMS import MAIN ; MAIN(mode)



