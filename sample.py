from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('http://www.yahoo.com')

# Find the search box
elem = driver.find_element(By.NAME, 'p')
# Types seleniumhq and RETURN/ENTER
elem.send_keys('seleniumhq' + Keys.RETURN)

driver.quit()