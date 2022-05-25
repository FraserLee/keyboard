#!/usr/bin/env python3

# pip install selenium
# brew install chromedriver (or whatever's up on your system)

SCALE = 4.0

import os
import sys
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.common as c


# gate usage
if len(sys.argv) == 1:
    print("Usage: capture.py [filename] [optional: scale]")
    sys.exit(1)

filename = sys.argv[1]
if len(sys.argv) == 3:
    SCALE = float(sys.argv[2])

# set up the browser
chrome_options = Options()
chrome_options.headless = True
chrome_options.add_argument("--window-size=4000,4000")

# open a gutted KLE
driver = webdriver.Chrome('chromedriver', options=chrome_options)
driver.get('file://' + os.path.dirname(os.path.realpath(__file__)) + '/kle/kb.html')

# open file into KLE, force a refresh
with open('layers.json', 'r') as f:
    driver.execute_script(
        f'angular.element(document.getElementsByTagName("body")).scope().\
            deserializeAndRender({f.read()}, true)'
    )
    driver.execute_script(
        r'angular.element(document.getElementsByTagName("body")).scope().$apply()'
    )

size = driver.find_element(by=c.by.By.ID, value='keyboard-bg').size
print(size)

# zoom in
driver.execute_script(f'document.body.style.zoom = {SCALE};')

# resize the window, and capture the keyboard
driver.set_window_size(int(size['width'] * SCALE), int(size['height'] * SCALE))

filename = filename.split("/")[-1].split(".")[0] + ".png"
print(f'saving to \'{filename}\'')

screenshot = driver.save_screenshot(filename)

driver.quit()

