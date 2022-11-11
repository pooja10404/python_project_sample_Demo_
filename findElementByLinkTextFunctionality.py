import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# webdriver.Chrome() will initialize the chrome driver
driver = webdriver.Chrome()

# maximize_window() will maximize the window
driver.maximize_window()

driver.get("https://abstracta.us/blog/software-testing/best-demo-websites-for-practicing-different-types-of-software-tests/")

# wait implicitly
driver.implicitly_wait(10)

# identify element with linkText
addEmployee = driver.find_element(By.LINK_TEXT, 'About Us')

# time.sleep(5) is the Hard Wait
time.sleep(10)

addEmployee.click()
time.sleep(10)

# driver.close() will close the window
driver.close()


