# -*- coding: utf-8 -*-
from LIBRARY import *

def MAIN(mode):
        if mode==1000:
        	addDir('Problem:   Can\'t see Arabic Text or Letters','',1001)
       		addDir('في موقع كل العرب - الفيديو لا يعمل   :مشكلة','',1002)
        	addDir('بعض الروابط لا تعمل   :مشكلة','',1003)
        	addDir('لا توجد مواقع مخصصة للافلام والمسلسلات الاجنبية   :مشكلة','',1004)
        	addDir('بعض الروابط بطيئة   :مشكلة','',1005)
        	addDir('لماذا يوجد سيرفرات مجهولة او سيئة   :مشكلة','',1006)
        	xbmcplugin.endOfDirectory(addon_handle)

	elif mode==1001:
		message1 = '1.   If you can\'t see Arabic Letters then go to "Kodi Interface Settings" and change the font to "Arial"'
		message2 = '2.   If you can\'t see "Arial" in kodi skin fonts then go to "Kodi Interface Settings" and change your skin to another skin that accepts "Arial" font'
		xbmcgui.Dialog().ok('Arabic Problem',message1)
		xbmcgui.Dialog().ok('Font Problem',message2)

	elif mode==1002:
		message1 = 'هذا الموقع بحاجة الى ربط مشفر حاول تنزيل شهادة التشفير (SSL Certificate) على كودي أو استخدم اصدار اخر لكودي  مثل اصدار 17.6'
		xbmcgui.Dialog().ok('المواقع المشفرة',message1)
		message2 = 'شهادة التشفير هي ملف يحتوي على شفرة خاصة او تواقيع خاصة لشركات معروفة وله تاريخ صلاحية ونفاذ والغرض منه هو تبادل المعلومات بطريقة مشفرة يصعب اختراقها وفهمها'
		xbmcgui.Dialog().ok('شهادة التشفير - SSL Certificate',message2)

	elif mode==1003:
		yes = xbmcgui.Dialog().yesno('روابط لا تعمل','غالبا السبب هو من الموقع الاصلي المغذي للبرنامج وللتأكد تستطيع اخبار المبرمج بجميع التفاصيل فهل تريد اخبار المبرمج الان ؟')	
		if yes: 
			import PROGRAM
			PROGRAM.MAIN(2)

	elif mode==1004:
		message = 'السبب هو ان هذا البرنامج مخصص فقط للغة العربية ولكن مع هذا وبالصدفة يوجد فيه مواقع فيها افلام ومسلسلات مترجمة او مدبلجة الى اللغة العربية والى لغات اخرى ولا يوجد سبب للتكرار'
		xbmcgui.Dialog().ok('مواقع اجنبية',message)

	elif mode==1005:
		message = 'الروابط البطيئة لا علاقة لها بالبرنامج وغالبا السبب هو من الموقع الاصلي المغذي للبرنامج'
		xbmcgui.Dialog().ok('روابط بطيئة',message)

	elif mode==1006:
		message = 'هي سيرفرات لا يستطيع البرنامج استخدامها بسبب كونها محمية من المصدر او بحاجة الى اشتراك رسمي او جديدة او لا يعرفها البرنامج'
		xbmcgui.Dialog().ok('سيرفرات سيئة او مجهولة',message)

	return
		

