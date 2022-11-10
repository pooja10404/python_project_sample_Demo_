from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
location = "https://demoqa.com/alerts"
driver.get(location)

# Click on the "Alert" button to generate the Simple Alert
clickMeButton = driver.find_element(By.ID, 'confirmButton')
clickMeButton.click()
time.sleep(2)

# Switch the control to the Alert window
alertBox = driver.switch_to.alert
# To click on the ‘Cancel’ button of the alert. (Dismiss the alert)
alertBox.dismiss()

# close the driver
driver.close()
