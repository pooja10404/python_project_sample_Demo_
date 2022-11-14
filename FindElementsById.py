from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser= webdriver.Chrome()
browser.get("https://wiki.ubuntu.com")
browser.maximize_window()
time.sleep(3)

element = browser.find_elements(By.ID,"//id")
for item in element:
    text = item.text
    print(text)

time.sleep(3)
browser.close()