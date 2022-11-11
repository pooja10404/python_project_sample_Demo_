import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#to load the chrome driver
driver = webdriver.Chrome()
# to maximize the browser window
driver.maximize_window()
#Explicit wait for 5 seconds
time.sleep(2)
#get the url
driver.get("https://www.tutorialspoint.com/index.htm")
driver.refresh()
driver.find_element(By.LINK_TEXT,"Company")
print("hello")
#to close the browser
driver.quit()


