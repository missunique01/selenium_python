

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

driver_obj.get("https://www.hyrtutorials.com/p/frames-practice.html")

driver_obj.maximize_window()

#Switch to frame 1 and perfomd the action
driver_obj.switch_to.frame("frm1")
driver_obj.find_element(By.XPATH,"//li[@class='hub-home']").click()

#go back to main page
driver_obj.switch_to.default_content()

#Switch to frame 2 and perfomd the action
driver_obj.switch_to.frame("frm2")
driver_obj.find_element(By.XPATH,"//div[@class ='post-head']")

#go back to main page
driver_obj.switch_to.default_content()

#Switch to frame 3 and perfomd the action
driver_obj.switch_to.frame("frm3")
driver_obj.find_element(By.XPATH,"//a[@class = 'facebook']").click()
