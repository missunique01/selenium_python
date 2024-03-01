
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

driver_obj.get("https://rahulshettyacademy.com/AutomationPractice/")

driver_obj.maximize_window()

# dropdown_Elements = Select(driver_obj.find_element(By.XPATH,"//select[@id= 'dropdown-class-example']"))
# Obj created for Select Class
# select_obj = Select(dropdown_Elements)

#select the elements from the dropdown

# dropdown_Elements.select_by_visible_text("Option1")
# dropdown_Elements.select_by_value("2")
# dropdown_Elements.select_by_index(2)
#Capture all the elements

# alloptions = dropdown_Elements.options
#
# print("Total options available to select: ", len(alloptions))  #4

# for i in alloptions:
#     print(i.text) #Select Option1 Option2 Option3

#selecting the element in the web page without using built in function
# for i in alloptions:
#     if i.text == "Option1":
#         i.click()
#         break

#Printing options
all_Options = driver_obj.find_elements(By.XPATH,"//*[@id= 'dropdown-class-example']/option")

print(len(all_Options))