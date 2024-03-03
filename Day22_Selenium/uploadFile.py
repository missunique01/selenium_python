
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#Service Object Creation

options = webdriver.ChromeOptions()
service_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")

options.add_experimental_option("detach",True)
driver_obj = webdriver.Chrome(service= service_obj, options=options)

driver_obj.implicitly_wait(20)

#Go to application


driver_obj.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver_obj.maximize_window()

resume_uplpad = driver_obj.find_element(By.XPATH,"//input[@name='resume']").click()

driver_obj