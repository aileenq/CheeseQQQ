# -*- coding: utf-8 -*-
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from playsound import playsound
from datetime import datetime


search_dates = ['2020-09-02','2020-09-05','2020-09-09','2020-09-12','2020-09-16','2020-09-19','2020-09-23','2020-09-26'] #你想要搜索的日期
base_url = 'https://www.google.com/flights?lite=0#flt=SFO.PVG.2020-11-25.SFOPVG0UA857;c:USD;e:1;a:UA;sd:1;t:b;tt:o;sp:2.USD.706410' #这个url可以替换成任何你想搜的航班


time_out_seconds = 3 # set the time to wait till web fully loaded
executable_path = '-----你的chromedriver存放路径-----' #例如 ‘/Users/zhangsan/Downloads/chromedriver’

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome('-----你的chromedriver存放路径-----', chrome_options=option) #例如 ‘/Users/zhangsan/Downloads/chromedriver’
driver.get(base_url)

found = False
for i in range(0,250): #刷250轮
	for my_date in search_dates:
		if found:
			break
		my_url = base_url.replace('2020-11-25', my_date) #前面的日期是你base_url里面的日期
		driver = webdriver.Chrome(executable_path=executable_path, chrome_options=option)
		driver.get(my_url)
		
		time.sleep(time_out_seconds)
		try:
			driver.find_element_by_class_name('gws-flights-results__error-message')
			print(datetime.now())
			print('UA857 SFO-PVG: no result on date: ' + my_date ) #设定没有搜到航班时的提示信息
			driver.quit()
			time.sleep(3)
			continue
		except:
			playsound('-----你的提示音文件路径-----') #播放提示音 文件路径例如‘/Users/zhangsan/Downloads/alert.mp3’
			print('❥△❥ flight search attempted on date ' +  my_date + ' flight found!❥△❥')
			print('  url:', my_url)
			found = True
			break
	
print("End of 250 rounds.")
playsound('-----你的结束提示音文件路径-----') #播放结束提示音 文件路径例如‘/Users/zhangsan/Downloads/end.mp3’
driver.quit()  
