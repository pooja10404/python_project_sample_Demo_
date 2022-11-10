from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
location = "https://demoqa.com/alerts"
driver.get(location)

# Click on the "Alert" button to generate the Simple Alert
clickMeButton = driver.find_element(By.ID, 'alertButton')
clickMeButton.click()
time.sleep(2)

# Switch the control to the Alert window and send keys
try:
    alertBox = driver.switch_to.alert
    # Retrieve the message on the Alert window
    message = alertBox.text
    print('message===' + message)
except:
    print('error')

# close the driver
driver.close()
