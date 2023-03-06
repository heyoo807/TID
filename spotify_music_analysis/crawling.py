import selenium
from selenium import webdriver as wd
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests
from itertools import repeat
from selenium.webdriver.common.by import By

# 크롬드라이버 열기
driver = wd.Chrome('C:\chromedriver') # 크롬드라이버 경로
driver.maximize_window() # 크롬창 크기 최대

# 드라이버가 해당 url 접속
url = 'https://www.melon.com/genre/song_list.htm?gnrCode=GN0100' # 멜론차트 페이지
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
request = requests.get(url, headers=header)
print(request)

# 셀레니움 클릭
driver.get(url)
time.sleep(1)

driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div/div[5]/form/div/div/div/a[2]').click() # 인기버튼 클릭




for j in range(1,10):
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="pageObjNavgation"]/div/span/a[{0}]'.format(j)).click() # 인기버튼 클릭
        soup = BeautifulSoup(driver.page_source)
        soup.select('div.service_list_song')
        titles = soup.findAll('div', {'class': 'rank01'})

        for i in range(len(titles)):
           print(titles[i].text.strip())



print("ok")
