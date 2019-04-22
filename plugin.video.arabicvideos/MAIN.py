# -*- coding: utf-8 -*-
from lib.LIBRARY import *

def MAIN():
	#addLink(menu_name+'Testing - watched enabled','',9,'','','yes')
	#addLink(menu_name+'Testing - watched disabled','',9,'','','no')

	addDir('بحث في جميع مواقع البرنامج'+'   .1','',6)
	addDir('=========================','',9999)

	addDir('[COLOR FFC89008]مواقع سيرفرات خاصة - قليلة المشاكل[/COLOR]','',5)
	addDir('[COLOR FFC89008]SHF [/COLOR]'+'موقع شوف ماكس (مشفر)'+'   .2','',50)
	addDir('[COLOR FFC89008]EGB [/COLOR]'+'موقع ايجي بيست (مشفر)'+'   .3','',120)
	addDir('[COLOR FFC89008]KLA  [/COLOR]'+'موقع كل العرب (مشفر)'+'   .4','',10)
	addDir('[COLOR FFC89008]PNT [/COLOR]'+'موقع بانيت'+'   .5','',30)
	addDir('[COLOR FFC89008]IFL   [/COLOR]'+'موقع قناة اي فيلم'+'   .6','',20)
	addDir('[COLOR FFC89008]KWT [/COLOR]'+'موقع قناة الكوثر'+'   .7','',130)
	addDir('[COLOR FFC89008]MRF [/COLOR]'+'موقع قناة المعارف'+'   .8','',40)
	addDir('[COLOR FFC89008]FTM [/COLOR]'+'موقع المنبر الفاطمي'+'   .9','',60)
	addDir('=========================','',9999)

	addDir('[COLOR FFC89008]مواقع سيرفرات خاصة وعامة - كثيرة المشاكل[/COLOR]','',5)
	addDir('[COLOR FFC89008]TV1   [/COLOR]'+'قنوات تلفزونية'+'   .10','',100)
	addDir('[COLOR FFC89008]AKM [/COLOR]'+'موقع اكوام (مشفر)'+'   .11','',70)
	addDir('[COLOR FFC89008]HEL [/COLOR]'+'موقع هلال يوتيوب (مشفر)'+'   .12','',90)
	addDir('=========================','',9999)

	addDir('[COLOR FFC89008]مواقع سيرفرات عامة - كثيرة المشاكل[/COLOR]','',5)
	addDir('[COLOR FFC89008]SHA [/COLOR]'+'موقع شاهد فوريو'+'   .13','',110)
	addDir('[COLOR FFC89008]HLA [/COLOR]'+'موقع هلا سيما (مشفر)'+'   .14','',80)
	addDir('=========================','',9999)

	addDir('ـProblems & Solutions    مشاكل وحلول'+'   .15','',1000)
	addDir('ـMessage to developer    رسالة الى المبرمج'+'   .16','',2)
	addDir('ـ DMCA     قانون الألفية للملكية الرقمية'+'   .17','',3)
	addLink('فحص المواقع المشفرة'+'   .18','',4)

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
try: text=urllib2.unquote(params["text"])
except: pass

if mode=='': MAIN()
elif mode>=0 and mode<=9: from lib.PROGRAM import MAIN ; MAIN(mode,text)
elif mode>=10 and mode<=19: from lib.ALARAB import MAIN ; MAIN(mode,url,text)
elif mode>=20 and mode<=29: from lib.IFILM import MAIN ; MAIN(mode,url,page,text)
elif mode>=30 and mode<=39: from lib.PANET import MAIN ; MAIN(mode,url,text)
elif mode>=40 and mode<=49: from lib.ALMAAREF import MAIN ; MAIN(mode,url,category,text)
elif mode>=50 and mode<=59: from lib.SHOOFMAX import MAIN ; MAIN(mode,url,text)
elif mode>=60 and mode<=69: from lib.ALFATIMI import MAIN ; MAIN(mode,url,category,text)
elif mode>=70 and mode<=79: from lib.AKOAM import MAIN ; MAIN(mode,url,text)
elif mode>=80 and mode<=89: from lib.HALACIMA import MAIN ; MAIN(mode,url,page,text)
elif mode>=90 and mode<=99: from lib.HELAL import MAIN ; MAIN(mode,url,text)
elif mode>=100 and mode<=109: from lib.TV1 import MAIN ; MAIN(mode,url)
elif mode>=110 and mode<=119: from lib.SHAHID4U import MAIN ; MAIN(mode,url,text)
elif mode>=120 and mode<=129: from lib.EGYBEST import MAIN ; MAIN(mode,url,page,text)
elif mode>=130 and mode<=139: from lib.ALKAWTHAR import MAIN ; MAIN(mode,url,page,text)

elif mode>=1000 and mode<=1009: from lib.PROBLEMS import MAIN ; MAIN(mode)



