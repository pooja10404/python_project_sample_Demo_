import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/index.htm")
time.sleep(5)
b = driver.find_element(By.CSS_SELECTOR,"h1[class='mb-0 display-6 mb-4 mt-8']")
time.sleep(5)
# get text and print
print("Text is: " + b.text)
time.sleep(5)
driver.close()
