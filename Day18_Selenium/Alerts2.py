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

driver_obj.get("https://mypage.rediff.com/login")

driver_obj.maximize_window()
driver_obj.find_element(By.XPATH,"//input[@type = 'submit']").click()  #Login Button
alertobj = driver_obj.switch_to.alert

time.sleep(5)
alertobj.accept()