import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
# Find the search box
driver.maximize_window()
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
login=driver.find_element(By.XPATH, "//button[@type='submit']")
username.send_keys("Admin")
password.send_keys("admin123")
login.click()
time.sleep(2)
driver.close()