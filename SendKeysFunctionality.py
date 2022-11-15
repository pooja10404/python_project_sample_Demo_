import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# webdriver.Chrome() It will initialize the chrome driver
driver = webdriver.Chrome()
# maximize_window() it maximize the window
driver.maximize_window()
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
time.sleep(5)
# CSS_SELECTOR will find element using css_selector
element = driver.find_element(By.CSS_SELECTOR, "input#Email")
# CSS_SELECTOR will find version  using css_selector
password = driver.find_element(By.CSS_SELECTOR, "input#Password")
# get  button by xpath
button = driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]")
# it will clear the element
element.clear()
# it will clear the password
password.clear()
# send_keys will send string in field
element.send_keys("admin@yourstore.com")
# send_keys will send string in password field
password.send_keys("admin")
time.sleep(5)
# it will click the button
button.click()
# close driver
driver.close()

