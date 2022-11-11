import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# webdriver.Chrome() will initialize the chrome driver
driver = webdriver.Chrome()

# maximize_window() will maximize the window
driver.maximize_window()


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# wait implicitly
driver.implicitly_wait(10)

# ID finds element with id
userName = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
login = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")

# send_keys sends string in the field
userName.send_keys("Admin")
password.send_keys("admin123")

# click() will click on the element
login.click()

# time.sleep(5) is the Hard Wait
time.sleep(5)

# driver.close() will close the window
driver.close()
