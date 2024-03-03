
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

#Service Object Creation

options = webdriver.ChromeOptions()
service_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")

options.add_experimental_option("detach",True)
driver_obj = webdriver.Chrome(service= service_obj, options=options)

driver_obj.implicitly_wait(10)

driver_obj.get("https://jqueryui.com/datepicker/")
driver_obj.maximize_window()

#Go to iframe
# iframe_element = driver_obj.find_element(By.XPATH,"//iframe[@class='demo-frame']")
# driver_obj.switch_to.window(iframe_element)

#If we have only single frame we can use this
driver_obj.switch_to.frame(0)

#MM/DD/YYYY -Date Format
#Passing the Date
# driver_obj.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("05/30/2022")

#Logic2

year = "2021"
date = "5"
month = "October"

driver_obj.find_element(By.XPATH,"//input[@id='datepicker']").click()

#Capture the Current month & year on  the screen
#Then compare with the expected month & year

while True:
    month_xpath = driver_obj.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    year_xpath =  driver_obj.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if month_xpath==month and year_xpath == year:
        break
    else:
        #Moving Forward
        # driver_obj.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click() #Next arrow
        #Moving Backward
        driver_obj.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click()

#Selecting date Logic
dates = driver_obj.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for i in dates:
    if i.text == date:
        i.click()
        break



