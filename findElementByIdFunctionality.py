import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# webdriver.Chrome() will initialize the chrome driver
driver = webdriver.Chrome()

# maximize_window() will maximize the window
driver.maximize_window()


driver.get("https://demoqa.com/text-box/")

# wait implicitly
driver.implicitly_wait(10)

# ID finds element with id
userName = driver.find_element(By.ID, "userName")
email = driver.find_element(By.ID, "userEmail")
submit = driver.find_element(By.ID, "submit")
currentAddress = driver.find_element(By.ID, "currentAddress")
permanentAddress = driver.find_element(By.ID, "permanentAddress")

# send_keys sends string in the field
userName.send_keys("DemoUser")
email.send_keys("demouser@gmail.com")
currentAddress.send_keys("currentAddress")
permanentAddress.send_keys("permanentAddress")

# click() will click on the element
submit.click()

# time.sleep(5) is the Hard Wait
time.sleep(5)

# driver.close() will close the window
driver.close()