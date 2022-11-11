# import webdriver
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains

# create webdriver object
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.geeksforgeeks.org/")

# get source element
source_element = driver.find_element(By.XPATH, "(//span[contains(text(),'Courses')]) [1]")

# get target element
target_element = driver.find_element(By.XPATH, "(//span[contains(text(),'Web Development')]) [1]")

# create action chain object
action = ActionChains(driver)

# drag and drop the item
action.drag_and_drop(source_element, target_element)

# perform the operation
action.perform()
