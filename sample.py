import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.yahoo.com/")

# Find the search box

element = driver.find_element(By.NAME, "p")
element.send_keys("Selenium" + Keys.RETURN)
driver.close()
