
#-----------------Import stataments--------------------------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#------------------Object creations------------------------

service_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver_obj = webdriver.Chrome(service= service_obj, options=options)
#-----------------Waiting time 10 seconds for loading the window-----------
#------------- method to wait for elements to become available before throwing an exception------------
driver_obj.implicitly_wait(10)
#--------------------Get the url ---------------

driver_obj.get("https://demo.nopcommerce.com/register?returnUrl=%2F")

driver_obj.maximize_window()
#------------Conditional commands------------------
#is_displayed, is_enabled

# searchbox = driver_obj.find_element(By.XPATH,"//input[@id='small-searchterms']")
#
# print("Display Status: ", searchbox.is_displayed())
# print("Enable Status: ", searchbox.is_enabled())

#is_Selected - only for radio buttons &check boxes we can use
radio_Male = driver_obj.find_element(By.XPATH,"//input[@id = 'gender-male']")
radio_female = driver_obj.find_element(By.XPATH,"//input[@id = 'gender-female']")

print("Default radio Button Status")
print(radio_Male.is_selected())  #False
print(radio_female.is_selected()) #False

# radio_Male.click()  #Selected mail radio button
# print("After selecting male radio button")
# print(radio_Male.is_selected()) #True
# print(radio_female.is_selected()) #False
radio_female.click()
print("After selecting female radio button")
print(radio_Male.is_selected())
print(radio_female.is_selected())
# driver_obj.quit()