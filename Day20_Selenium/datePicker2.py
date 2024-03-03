
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

driver_obj.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver_obj.maximize_window()


#Go to the Date Of Birth field & CLick
driver_obj.find_element(By.XPATH,"//p[@id='dob_field']//span").click()

datePicker_Month = Select(driver_obj.find_element(By.XPATH,"//select[@class='ui-datepicker-month']"))
datePicker_Month.select_by_visible_text("Dec")

datePicker_Year = Select(driver_obj.find_element(By.XPATH,"//select[@class='ui-datepicker-year']"))

datePicker_Year.select_by_visible_text("2022")

allDates = driver_obj.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for i in allDates:
    if i.text == "5":
        i.click()
        break

