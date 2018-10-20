# -*- coding: utf-8 -*-
from lib.LIBRARY import *

def MAIN():
	#addLink('Testing','',9)
	addDir('ـMessage to developer    رسالة الى المبرمج'+'   .14','',2)
	addDir('ـ DMCA     قانون الألفية للملكية الرقمية'+'   .13','',3)
	addDir('ـProblems & Solutions    مشاكل وحلول'+'   .12','',1000)
	addDir('قنوات تلفزونية'+'   .11','',100)
	#addDir('=========================','',9999)
	addDir('موقع قناة المعارف'+'   .10','',40)
	addDir('موقع المنبر الفاطمي'+'   .9','',60)
	addDir('موقع قناة اي فيلم'+'   .8','',20)
	addDir('موقع شوف ماكس'+'   .7','',50)
	addDir('موقع اكوام'+'   .6','',70)
	addDir('موقع هلا سيما'+'   .5','',80)
	addDir('موقع هلال يوتيوب'+'   .4','',90)
	addDir('موقع شاهد فوريو'+'   .3','',110)
	addDir('موقع كل العرب'+'   .2','',10)
	addDir('موقع بانيت'+'   .1','',30)
	xbmcplugin.endOfDirectory(addon_handle)
	return

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
elif mode>=100 and mode<=109: from lib.TV1 import MAIN ; MAIN(mode,url)
elif mode>=110 and mode<=119: from lib.SHAHID4U import MAIN ; MAIN(mode,url)

elif mode>=0 and mode<=9: from lib.PROGRAM import MAIN ; MAIN(mode,text)
elif mode>=1000 and mode<=1009: from lib.PROBLEMS import MAIN ; MAIN(mode)



