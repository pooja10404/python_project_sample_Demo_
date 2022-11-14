import time

from selenium import webdriver

# Import Select class
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

# Using chrome driver
driver = webdriver.Chrome()
driver.maximize_window()
# Web page url
driver.get("https://demo.guru99.com/test/newtours/register.php")

# Find Xpath of element
element = driver.find_element(By.XPATH, "//select[@name='country']")
drop = Select(element)

# Select by Value
drop.select_by_value("ANGUILLA")

driver.close()