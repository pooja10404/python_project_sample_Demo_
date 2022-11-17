
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
driver = webdriver.Chrome()
driver.maximize_window()
# launch the url
driver.get("https://jqueryui.com/datepicker/")
driver.implicitly_wait(5)
# switch to frame
l = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
driver.switch_to.frame(l)
# identify element inside frame
d = driver.find_element(By.ID, "datepicker")
date = datetime.datetime.today()
day = date.strftime("%d")
curTime = date.strftime("%H:%M:%S")
driver.implicitly_wait(5)
d.click()
driver.implicitly_wait(5)
# identify list of all dates
n = driver.find_elements(By.XPATH, "(//td[@data-handler='selectDay']/a)[index]")
driver.implicitly_wait(5)
x = driver.find_element(By.XPATH, "(//td[@data-handler='selectDay']/a)[index]".replace('index', str(day)))
driver.implicitly_wait(5)
x.click()
time.sleep(3)
# get selected date (for choosing today date)
s = d.get_attribute('value')
print("current date is : ")
print(s, curTime)
#for prevoius date of which date you choose
pre = datetime.datetime.today() + datetime.timedelta(days=-1)
print("previus date is:-")
print (pre)
#for nextday date of which date you choose
NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
print("next date  is:-")
print (NextDay_Date)

# browser quit
driver.quit()
