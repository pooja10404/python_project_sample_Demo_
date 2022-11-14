import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(0.5)
driver.get("https://www.tutorialspoint.com/index.htm")


time.sleep(5)
b = driver.find_element(By.XPATH, "(//a[@class='nav-link'])[2]").click()
#perform click with execute_script method
driver.execute_script("arguments[0].click();", b)
time.sleep(5)
print("Page title after click: " + driver.title)