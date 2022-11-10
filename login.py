import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
time.sleep(5)
element = driver.find_element(By.CSS_SELECTOR, "input#Email")
version = driver.find_element(By.CSS_SELECTOR, "input#Password")
button = driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]")
element.clear()
version.clear()
element.send_keys("admin@yourstore.com")
version.send_keys("admin")
time.sleep(5)
button.click()
driver.close()

