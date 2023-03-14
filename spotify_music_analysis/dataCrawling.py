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
url = 'https://www.melon.com/chart/index.htm' # 멜론차트 페이지
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
request = requests.get(url, headers=header)
print(request)

# 셀레니움 드라이버가 url 접속
driver.get(url)
time.sleep(1)

soup = BeautifulSoup(driver.page_source)
div = soup.findAll('div', {'class' : 'service_list_song'})
    
def getSong():
     song_data = []
     for i in div:
        songs = i.findAll('div', {'class': 'rank01'})
     for i in range(len(songs)):
          song_data.append(songs[i].text.strip())
     return song_data

def getSinger():
     singer_data = []
     for i in div:
        singers = i.findAll('span', {'class' : 'checkEllipsis'})
     for i in range(len(singers)):
          singer_data.append(singers[i].text.strip())
     return singer_data

def getAlbum():
    album_data = []
    for i in div:
        albums = i.findAll('div', {'class' : 'rank03'})
    for i in range(len(albums)):
        album_data.append(albums[i].text.strip())
    return album_data

def getSongInfo():
    genre_data = []
    lyrics_data = []
    for i in div:
         driver.find_element(By.XPATH, '//*[@id="lst50"]/td[5]/div').click()

# a = getSong()
# print(a)
# print(len(a))

# b = getSinger()
# print(b)
# print(len(b))

# c = getAlbum()
# print(c)
# print(len(c))