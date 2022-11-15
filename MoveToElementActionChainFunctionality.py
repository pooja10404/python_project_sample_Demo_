import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# maximize the window
driver.maximize_window()
time.sleep(5)
# get user_name by xpath
user_name = driver.find_element(By.XPATH, "//input[@name='username'] ")
# get password by xpath
password = driver.find_element(By.XPATH, "//input[@name='password']")
# get button by TagName
button = driver.find_element(By.TAG_NAME, "button")
# send_keys send the user_name
user_name.send_keys("Admin")
# send_keys send the Password
password.send_keys("admin123")
# button click login button
button.click()
time.sleep(5)
# get Admin By xpath
Admin = driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][1]")
time.sleep(5)
# create action chain object
actions = ActionChains(driver)
# move to element at Admin and click the Admin
actions.move_to_element(Admin).click().perform()
# close the driver
driver.close()
