import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
# create webdriver object
driver = webdriver.Chrome()
# maximize window
driver.maximize_window()
driver.get("https://www.geeksforgeeks.org/")
time.sleep(5)
# get element by xpath
element = driver.find_element(By.XPATH, "(//span[contains(text(),'Courses')]) [1]")

# create action chain object
action = ActionChains(driver)
# click the Hold the Courses Link
action.click_and_hold(element)

# perform the operation
action.perform()
