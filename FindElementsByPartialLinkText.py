from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#Getting the instance of the web driver
driver = webdriver.Chrome()

#Providing the website URL
driver.get("https://www.educative.io/")

driver.maximize_window()
time.sleep(2)

#Using LINK_TEXT

#Using PARTIAL_LINK_TEXT
Link = driver.find_elements(By.PARTIAL_LINK_TEXT, 'dev')
for item in Link:
    text = item.text
    print(text)


driver.close()