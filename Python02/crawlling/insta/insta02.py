# -*- coding:utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://www.instagram.com/explore/tags/' + input('search keyword : ')
driver = webdriver.Chrome('C:/test/chromedriver.exe')
driver.implicitly_wait(3) # 3초 기다리겠습니다
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

# email = driver.find_element_by_css_selector('.f0n8F > input').send_keys('duflalrjdi@nate.com')

# img_list = soup.find_all('div', {'class':'KL4Bh'})
# print(img_list)
img_list = soup.find_all('img')
for m in img_list : 
    print(m.get('src'))
