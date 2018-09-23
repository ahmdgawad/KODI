# -*- coding: utf-8 -*-
from LIBRARY import *

def MAIN(mode):
        if mode==1000:
        	website0b = 'Problem:   Can\'t see Arabic Text'
        	website0c = 'في موقع كل العرب - الفيديو لا يعمل   :مشكلة'
        	website0d = 'بعض الروابط لا تعمل   :مشكلة'
        	website0e = 'اين مواقع الافلام والمسلسلات الاجنبية   :سؤال'
        	addDir(website0b,'',1001)
       		addDir(website0c,'',1002)
        	addDir(website0d,'',1003)
        	addDir(website0e,'',1004)
        	xbmcplugin.endOfDirectory(addon_handle)

	elif mode==1001:
		message1 = '1.   If you can\'t see Arabic Letters then go to "Kodi Interface Settings" and change the font to "Arial"'
		message2 = '2.   If you can\'t see "Arial" in kodi skin fonts then go to "Kodi Interface Settings" and change your skin to another skin that accepts "Arial" font'
		xbmcgui.Dialog().ok('Arabic Problem',message1)
		xbmcgui.Dialog().ok('Font Problem',message2)

	elif mode==1002:
		message1 = 'هذا الموقع بحاجة الى ربط مشفر حاول تنزيل شهادة التشفير على كودي او استخدم اصدار اخر لكودي  مثل اصدار 17.6'
		xbmcgui.Dialog().ok('المواقع المشفرة',message1)

	elif mode==1003:
		yes = xbmcgui.Dialog().yesno('الحل هو اخبار المبرمج بالتفاصيل','هل تريد اخبار المبرمج الان ؟')	
		if yes: MAIN(4,'')

	elif mode==1004:
		message = 'البرنامج مخصص للغة العربية ومع هذا وبالصدفة يوجد فيه مواقع فيها افلام ومسلسلات مترجمة او مدبلجة الى اللغة العربية والى لغات اخرى'
		xbmcgui.Dialog().ok('مواقع اجنبية',message)

