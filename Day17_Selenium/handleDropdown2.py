
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

driver_obj.get("https://testautomationpractice.blogspot.com/")

driver_obj.maximize_window()

dropdown_Elements = Select(driver_obj.find_element(By.XPATH,"//select[@id='country']"))
# Obj created for Select Class
# select_obj = Select(dropdown_Elements)

#select the elements from the dropdown

# dropdown_Elements.select_by_visible_text("France")
#Capture all the elements
# all_options = dropdown_Elements.options
# print("Total options in the dropdown list using options are: ", len(all_options))  #10

#printing all the elements in available in the dropdown list
# for i in all_options:
#     print(i.text)

#Selecting the elements in the web page without using built-in function means without using select_by_visible_text like tha
# for i in all_options:
#     if i.text == "France":
#         i.click()
#         break

#Printing all the options using find_elements without using for loop
all_options = driver_obj.find_elements(By.XPATH,"//*[@id='country']/option")

print(len(all_options))  #10



