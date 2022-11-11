# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Chrome()


driver.get("https://www.geeksforgeeks.org/")

# get element
element = driver.find_element(By.XPATH, "(//span[contains(text(),'Web Development')]) [1]")

# print value
print(element.is_enabled())
