import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
# For maximixe the cuurent window
driver.maximize_window()

# value of an attribute in an html document
username = driver.find_element(By.NAME,"username").get_attribute("name")
print("attribute  is: " +username)
time.sleep(5)
driver.close()

