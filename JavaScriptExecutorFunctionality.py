import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
# webdriver.Chrome() It will initialize the chrome driver
driver = webdriver.Chrome()
# maximize_window() it maximize the window
driver.maximize_window()
driver.get("https://www.amazon.in/")
# LINK_TEXT will find element using LINK_TEXT
best_sellers = driver.find_element(By.LINK_TEXT, "Best Sellers")
# execute_script will click the element
driver.execute_script("arguments[0].click();", best_sellers)



