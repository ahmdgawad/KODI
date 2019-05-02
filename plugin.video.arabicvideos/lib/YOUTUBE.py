# -*- coding: utf-8 -*-
from LIBRARY import *

website0a = 'https://www.youtube.com'
script_name='YOUTUBE'
menu_name='[COLOR FFC89008]YUT [/COLOR]'

def MAIN(mode,text):
	yes = xbmcgui.Dialog().yesno('هل تريد الاستمرار ؟','هذا الاختيار سوف يخرجك من البرنامج','لأنه سوف يقوم بتشغيل برنامج يوتيوب')
	if yes:
		if mode==140: MENU()
		elif mode==149: SEARCH(text)
	return

def MENU():
	xbmc.executebuiltin('RunAddon(plugin.video.youtube)')
	return

def SEARCH(search=''):
	if search=='': search = KEYBOARD()
	if search == '': return
	search = search.replace(' ','%20')
	url = 'plugin://plugin.video.youtube/kodion/search/query/?q='+search
	xbmc.executebuiltin('ActivateWindow(Videos,'+url+',return)')
	return



