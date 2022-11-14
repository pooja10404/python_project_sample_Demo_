import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
# For maximixe the cuurent window
driver.maximize_window()

# NAME finds element with name
username = driver.find_element(By.NAME, "username").send_keys("Admin")
password = driver.find_element(By.NAME, "password").send_keys("admin123")

# XPATH finds element with XPATH
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)
driver.close()

