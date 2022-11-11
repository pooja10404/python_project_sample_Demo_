import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)
user_name = driver.find_element(By.XPATH, "//input[@name='username'] ")
password = driver.find_element(By.XPATH, "//input[@name='password']")
button = driver.find_element(By.TAG_NAME, "button")
user_name.send_keys("Admin")
password.send_keys("admin123")
button.click()
time.sleep(5)
Admin = driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][1]")
time.sleep(5)
actions = ActionChains(driver)
actions.move_to_element(Admin).click().perform()
driver.close()
