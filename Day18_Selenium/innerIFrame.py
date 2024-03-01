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

driver_obj.get("https://demo.automationtesting.in/Frames.html")

driver_obj.maximize_window()

driver_obj.find_element(By.XPATH,"//li[@class = 'active']//a[@class='analystic']").click()

outerframe = driver_obj.find_element(By.XPATH,"//*[@id='Multiple']/iframe")

driver_obj.switch_to.frame(outerframe)

innerframe = driver_obj.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver_obj.switch_to.frame(innerframe)

driver_obj.find_element(By.XPATH,"//input[@type='text']").send_keys("Welcome")


driver_obj.switch_to.parent_frame() #To Switch to the parent frame
#//div[@class = 'container iframes-page-container']

