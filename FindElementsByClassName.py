import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://phptravels.com/demo/")
driver.maximize_window()
time.sleep(5)
# Find the search box

country = driver.find_elements(By.CLASS_NAME, "jfHeader-menuList")

for item in country:
    text = item.text
    print(text)

time.sleep(2)
driver.close()
