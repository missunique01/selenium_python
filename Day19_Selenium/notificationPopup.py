from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

#Service Object Creation

#ChromeOptions class is used for  to specify the browser
#will creat one object for this and pass this obj while creating driverobj along with service
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications") #used to disable the notification popup's
service_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")

options.add_experimental_option("detach",True)
driver_obj = webdriver.Chrome(service= service_obj, options=options)

driver_obj.implicitly_wait(10)

driver_obj.get("https://whatmylocation.com/")

driver_obj.maximize_window()