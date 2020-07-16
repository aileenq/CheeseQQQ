# -*- coding: utf-8 -*-
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from playsound import playsound
from datetime import datetime


search_dates = ['2020-09-02','2020-09-05','2020-09-09','2020-09-12','2020-09-16','2020-09-19','2020-09-23','2020-09-26'] #你想要搜索的日期
base_url = 'https://www.google.com/flights?lite=0#flt=SFO.PVG.2020-11-25.SFOPVG0UA857;c:USD;e:1;a:UA;sd:1;t:b;tt:o;sp:2.USD.706410' #这里可以替换成任何你想搜的航班的google flight url


time_out_seconds = 3 # set the time to wait till web fully loaded
executable_path = '/Users/zhangsan/Downloads/FlightCrawler/chromedriver' #请把zhangsan替换成你自己mac的用户名

option = webdriver.ChromeOptions()
option.add_argument('headless') 
driver = webdriver.Chrome('/Users/zhangsan/Downloads/FlightCrawler/chromedriver', chrome_options=option) #请把zhangsan改成你自己mac的用户名
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
			print('UA857 SFO-PVG: no result on date: ' + my_date ) #没有搜到航班的提示信息
			driver.quit()
			time.sleep(3)
			continue
		except:
			playsound('/Users/zhangsan/Downloads/FlightCrawler/found.mp3') #播放发现航班的提示音
			print('❥△❥ flight search attempted on date ' +  my_date + ' flight found!❥△❥')
			print('  url:', my_url)
			found = True
			break
	
print("End of 250 rounds.")
playsound('/Users/zhangsan/Downloads/FlightCrawler/end.mp3') #播放结束提示音
driver.quit()  
