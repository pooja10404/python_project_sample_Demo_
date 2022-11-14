import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
# create webdriver object
driver = webdriver.Chrome()
# maximize window
driver.maximize_window()
driver.get("https://www.geeksforgeeks.org/")
# get element by xpath
element = driver.find_element(By.XPATH, "(//span[contains(text(),'Courses')]) [1]")

# create action chain object
action = ActionChains(driver)

# Right Click on Course Link
action.context_click(on_element=element).perform()

# perform the operation
# action.perform()
