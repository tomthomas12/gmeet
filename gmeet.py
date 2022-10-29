import pyautogui
import time
from datetime import date
from datetime import datetime
import os
dt = datetime.now()

def join(id):
	time.sleep(1)
	pyautogui.press('win', interval=0.5)
	time.sleep(1)
	pyautogui.typewrite('chrome', interval=0.5)
	time.sleep(1)
	pyautogui.press('enter', interval=0.5)
	time.sleep(2)
	pyautogui.typewrite('https://meet.google.com/?authser=0', interval=0.3)
	time.sleep(1)
	pyautogui.press('enter', interval=0.5)
	time.sleep(2)
	pyautogui.click(250, 520)
	time.sleep(1)
	pyautogui.typewrite(id, interval=0.2)
	time.sleep(1)
	pyautogui.press('enter', interval=0.2)
	time.sleep(9)
	pyautogui.click(400, 570)
	time.sleep(2)
	pyautogui.click(500, 570)
	time.sleep(2)
	pyautogui.click(990, 420)
	print("Asked to join")
	time.sleep(3)
	os.system("taskkill /im chrome.exe /f")
while True:
	if(dt.isoweekday()==6):
		#if(dt.strftime("%H:%M")=="15:58"):
			join("xrf-tciy-bsr")
			#continue
			break #just for now
		#go on adding your meeting ids per per date and time

