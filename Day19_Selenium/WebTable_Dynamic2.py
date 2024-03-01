
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

driver_obj.get("https://practice.expandtesting.com/dynamic-table")
driver_obj.minimize_window()

#total no of rows in a table
noOfRows = driver_obj.find_elements(By.XPATH,"//table[@class='table table-striped']/tbody/tr")
print("Total no of rows in a table", len(noOfRows))

for r in range(1,len(noOfRows)+1):
    CPU_VALUES = driver_obj.find_element(By.XPATH,"//table[@class='table table-striped']/tbody/tr["+str(r)+"]/td[4]").text
    print(CPU_VALUES)
    Actual_CPU_Value = driver_obj.find_element(By.XPATH,"//p[@id='chrome-cpu']").text
    if CPU_VALUES == Actual_CPU_Value:
        print("CPU Value is matching")
    else:
        print("Not matching")