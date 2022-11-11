import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# webdriver.Chrome() will initialize the chrome driver
driver = webdriver.Chrome()

# maximize_window() will maximize the window
driver.maximize_window()

driver.get("https://onepagelove.com/tag/demo")

# wait implicitly
driver.implicitly_wait(20)

# CLASS_NAME finds element with CLASS_NAME
userName = driver.find_element(By.CLASS_NAME, "thumb-image")

# send_keys sends string in the field
time.sleep(5)
userName.click()
time.sleep(5)

# driver.close() will close the window
driver.close()
