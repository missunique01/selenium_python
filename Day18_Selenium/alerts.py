import time

#-----------------Import stataments--------------------------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import requests
#------------------Object creations------------------------

service_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver_obj = webdriver.Chrome(service= service_obj, options=options)
#-----------------Waiting time 10 seconds for loading the window-----------
driver_obj.implicitly_wait(10)
#--------------------Get the url ---------------

driver_obj.get("https://the-internet.herokuapp.com/javascript_alerts")

driver_obj.maximize_window()

#Opens the alert window
driver_obj.find_element(By.XPATH,"//button[@onclick = 'jsPrompt()']").click()

time.sleep(5)

alertwindow = driver_obj.switch_to.alert
print(alertwindow.text)
alertwindow.send_keys("Welcome")
# alertwindow.accept()  #closing alert window by clcking OK Button
alertwindow.dismiss()  #closing alert window by clcking cancel Button
