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

# request 드라이버가 url 접속
url = 'https://www.melon.com/genre/song_list.htm?gnrCode=GN0100' # 멜론차트 페이지
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
request = requests.get(url, headers=header)
print(request)

# 셀레니움 드라이버가 url 접속
driver.get(url)
time.sleep(1)


genre = {'balad' : '//*[@id="conts"]/div[2]/ul/li[1]/a', 
         'dance' : '//*[@id="conts"]/div[2]/ul/li[2]/a', 
        #  'rapHiphop' : '//*[@id="conts"]/div[2]/ul/li[3]/a', 
        #  'RBsoul' : '//*[@id="conts"]/div[2]/ul/li[4]/a', 
        #  'indi': '//*[@id="conts"]/div[2]/ul/li[5]/a',
        # 'rockMetal': '//*[@id="conts"]/div[2]/ul/li[6]/a',
        # 'porkBlouse' : '//*[@id="conts"]/div[2]/ul/li[8]/a'
        }
data_title = []
data_artist = []

for g in genre.keys():

        driver.find_element(By.XPATH, genre.get(g)).click() # 하단 페이지 넘어가기 클릭
        # if(g == 'indi') :
        #         driver.find_element(By.XPATH, '//*[@id="conts"]/div[3]/ul/li[1]/a').click()
        driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div/div[5]/form/div/div/div/a[2]').click() # 인기버튼 클릭

        for _ in range(1):
                for i in range(1,2):
                        time.sleep(3)
                        driver.find_element(By.XPATH, '//*[@id="pageObjNavgation"]/div/span/a[{0}]'.format(i)).click() # 하단 페이지 넘어가기 클릭
                        soup = BeautifulSoup(driver.page_source)
                        div = soup.findAll('div', {'class' : 'service_list_song'})
                        
                        for i in div:
                                titles = i.findAll('div', {'class': 'rank01'})
                                artists = i.findAll('span', {'class' : 'checkEllipsis'})
                        
                        sub_title = []
                        sub_artist = []
                        for i in range(len(titles)):
                                sub_title.append(titles[i].text.strip())
                                sub_artist.append(artists[i].text.strip())
                                if(i == len(titles) - 1):
                                        data_title.append(sub_title)
                                        data_artist.append(sub_artist)
                                
                        
                
                # driver.find_element(By.XPATH, '//*[@id="pageObjNavgation"]/div/a').click()


print(data_title)
print(data_artist)






print("ok")
