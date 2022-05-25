#!/usr/bin/env python3

# pip install selenium
# brew install chromedriver (or whatever's up on your system)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.common as c
import time

chrome_options = Options()
#  chrome_options.headless = True
#  chrome_options.add_argument("--window-size=2560,2560")

driver = webdriver.Chrome('chromedriver', options=chrome_options)

driver.get('http://[::]:8000/kb.html#/')

time.sleep(3)

#  root = driver.find_element(by=c.by.By.TAG_NAME, value='body')

# zoom in
#  driver.execute_script("document.body.style.zoom='400%'")

with open('layers.json', 'r') as f:
    driver.execute_script(f'angular.element(document.getElementsByTagName("body")).scope().deserializeAndRender({f.read()}, true)')
    driver.execute_script(r'angular.element(document.getElementsByTagName("body")).scope().$apply()')

time.sleep(2)

screenshot = driver.save_screenshot('my_screenshot.png')
driver.quit()


