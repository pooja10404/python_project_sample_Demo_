from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com")
driver.find_element(By.LINK_TEXT, 'Frames').click()
driver.find_element(By.LINK_TEXT, 'Nested Frames').click()

# switch to frame with name
driver.switch_to.frame("frame-bottom")

# identify element and get text method
name = driver.find_element(By.XPATH, '//body').text
print("Test inside frame: " + name)

# move out of frame to parent page
driver.switch_to.default_content()

driver.quit()
