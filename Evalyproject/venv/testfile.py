from selenium import webdriver
from time import sleep
import pyperclip,pyautogui

driver = webdriver.Chrome()
#Window maximization
driver.maximize_window()
driver.get('http://desk.zol.com.cn/showpic/1920x1200_777_13.html')

 #  Move to the specified location, right click
pyautogui.rightClick(x=1000, y=500)

 # V
pyautogui.typewrite(['V'])

 #Copy address and file name
pic_dir = 'E:\\ROSI\\35.jpg'
pyperclip.copy(pic_dir)

 #Wait for the window to open, so as not to conflict with the command, the paste fails, and tried it many times before it has 0.8.
sleep(0.8)
 #
pyautogui.hotkey('ctrlleft','V')
 #  can also be pasted
# pyautogui.keyDown('ctrl')
# pyautogui.press('v')
# pyautogui.keyUp('ctrl')

 #
pyautogui.press('enter')