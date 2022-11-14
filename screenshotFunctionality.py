from selenium import webdriver
from time import sleep

# webdriver.Chrome() will initialize the chrome driver
driver = webdriver.Chrome()

# maximize_window() will maximize the window
driver.maximize_window()

driver.get('https://www.python.org')
sleep(2)

# get_screenshot_as_file will screenshot of the page
driver.get_screenshot_as_file("screenshot.png")
driver.quit()
print("end...")
