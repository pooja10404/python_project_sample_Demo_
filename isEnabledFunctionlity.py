# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Chrome()


driver.get("https://www.geeksforgeeks.org/")

# get element by xpath
element = driver.find_element(By.XPATH, "(//span[contains(text(),'Web Development')]) [1]")

# print element  is True or False
print(element.is_enabled())
