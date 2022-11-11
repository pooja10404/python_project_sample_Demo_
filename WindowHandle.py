import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()

#get method to launch the URL
driver.get("https://the-internet.herokuapp.com/windows")
time.sleep(5)

#to refresh the browser
driver.refresh()
#choose loactor by link test
link = driver.find_element(By.LINK_TEXT, "Click Here")
time.sleep(1.5)
link.click()

#prints the window handle in focus
time.sleep(5)
print(driver.current_window_handle)

#to fetch the first child window handle
change=driver.window_handles[1]

#to switch focus the first child window handle
time.sleep(2)
driver.switch_to.window(change)
print(driver.find_element(By.TAG_NAME("h3")))
#to close the browser
driver.quit()




