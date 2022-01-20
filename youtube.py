from selenium import webdriver
from bs4 import BeautifulSoup
import time

browser = webdriver.Chrome("./chromedriver")
url = "https://www.youtube.com/feed/explore"
browser.get(url)

html = browser.page_source
soup = BeautifulSoup(html, "html.parser")

print(soup)