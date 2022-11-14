import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains

# create webdriver object
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.geeksforgeeks.org/")
# get element
element = driver.find_element(By.CSS_SELECTOR, "input#gcse-search-input")

# get size od element
print(element.size)