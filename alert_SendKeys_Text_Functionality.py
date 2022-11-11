from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
location = "https://demoqa.com/alerts"
driver.get(location)

# Click on the "Alert" button to generate the Simple Alert
clickMeButton = driver.find_element(By.ID, 'promtButton')
clickMeButton.click()
time.sleep(4)

# Switch the control to the Alert window and send keys
try:
    alertBox = driver.switch_to.alert
    alertBox.send_keys('tester')
except:
    print(11111111111111)

# close the driver
driver.close()
