import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
# create webdriver object
driver = webdriver.Chrome()
# maximize window
driver.maximize_window()
driver.get("https://www.geeksforgeeks.org/")
# get element
element = driver.find_element(By.XPATH, "(//span[contains(text(),'Courses')]) [1]")
# create action chain object
action = ActionChains(driver)
# click the course link
action.click(element)
# release the course link
action.release(element)
# perform the operation
action.perform()
