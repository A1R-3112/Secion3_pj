import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'

pages = 1
url = f'https://search.shopping.naver.com/search/category/100005309?catId=50000153&origQuery&pagingIndex={pages}&pagingSize=40&productSet=total&query&sort=rel&timestamp=&viewType=list'

browser = webdriver.Chrome(executable_path = '/opt/homebrew/bin/chromedriver')
browser.get("http://python.org")
 
menus = browser.find_elements(By.CSS_SELECTOR, '#top>ul.menu>li')
 
pypi = None
for m in menus:
    if m.text == "PyPI":
        pypi = m
    print(m.text)

 
time.sleep(5) # 5초 대기
#browser.quit() # 브라우저 종료
>div.basicList_detail_box__OoXKt