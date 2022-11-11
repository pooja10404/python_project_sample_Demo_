# import webdriver
import time

from selenium import webdriver

# import Action chains
from selenium.webdriver.common.action_chains import ActionChains

# create webdriver object
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# get url
driver.get("https://www.geeksforgeeks.org/")

# get element

element = driver.find_element(By.LINK_TEXT, 'Courses')

# create action chain object
action = ActionChains(driver)

time.sleep(3)
# perform move_to_element operation
action.move_to_element(element).click().perform()
time.sleep(3)
