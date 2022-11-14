from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException)

driver = webdriver.Chrome()
driver.get("http://somedomain/url_that_delays_loading")
driver.maximize_window()
ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=ignore_list)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div")))

driver.quit()