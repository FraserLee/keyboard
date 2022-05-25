#!/usr/bin/env python3

# pip install selenium
# brew install chromedriver (or whatever's up on your system)

SCALE = 4.0

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.common as c
import time
import os

chrome_options = Options()
#  chrome_options.headless = True
#  chrome_options.add_argument("--window-size=2560,2560")

driver = webdriver.Chrome('chromedriver', options=chrome_options)

# print script directory
driver.get('file://' + os.path.dirname(os.path.realpath(__file__)) + '/kle/kb.html')

time.sleep(3)

kb_div = driver.find_element(by=c.by.By.ID, value='keyboard')
print(kb_div.size)

# zoom in
driver.execute_script(f'document.body.style.zoom = {SCALE};')

with open('layers.json', 'r') as f:
    driver.execute_script(f'angular.element(document.getElementsByTagName("body")).scope().deserializeAndRender({f.read()}, true)')
    driver.execute_script(r'angular.element(document.getElementsByTagName("body")).scope().$apply()')

time.sleep(2)

screenshot = driver.save_screenshot('my_screenshot.png')
driver.quit()


