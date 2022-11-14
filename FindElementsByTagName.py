import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
driver.maximize_window()
time.sleep(5)
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
login = driver.find_element(By.XPATH, "//button[@type='submit']")
username.send_keys("Admin")
password.send_keys("admin123")
login.click()
driver.implicitly_wait(5)

country = driver.find_elements(By.TAG_NAME, "button")

for item in country:
    text = item.text
    print(text)

time.sleep(2)
driver.close()
