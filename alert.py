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
time.sleep(1)

# Switch the control to the Alert window
alertBox = driver.switch_to.alert
# accept the alert
alertBox.accept()

# close the driver
driver.close()
