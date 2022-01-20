from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs

import pandas as pd

url = 'https://www.istarbucks.co.kr/index.do'

driver = wb.Chrome('./chromedriver')
driver.get(url)

driver.find_element_by_class_name('gnb_nav02').click()

#자세히 보기 클릭
driver.find_element_by_class_name('menu_drink_btn01').click()

#영양정보 보기 클릭
driver.find_element_by_class_name('a2').click()

#BeautifulSoup으로 웹 페이지 해석
soup = bs(driver.page_source,'html')

#항목타이틀, 모든 음료정보 수집
drink_cols = soup.select('table.coffeeInfo.mb60 th',limit=7)
drink_infos = soup.select('table.coffeeInfo.mb60 td')

col_list = []
for i in drink_cols:
    col_list.append(i.text)

info_list = []
for i in drink_infos:
    info_list.append(i.text)


import numpy as np
info_array = np.array(info_list).reshape(-1,7)
info_array

driver.close()
df = pd.DataFrame(info_array, columns=col_list)
df.set_index('메뉴')
df.to_excel("starbuks_menu.xlsx")