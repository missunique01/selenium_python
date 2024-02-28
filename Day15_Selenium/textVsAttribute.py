
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

driver_obj.get("https://demo.nopcommerce.com/login?returnUrl=%2F")

# email_box = driver_obj.find_element(By.XPATH,"//input[@id='Email']")
# email_box.clear()
# email_box.send_keys("abc123@gmail.com")
# print("Result of text: ", email_box.text)  #printed Nothing
# print("Result of get_attribute", email_box.get_attribute('value')) #abc123@gmail.com


button_element = driver_obj.find_element(By.XPATH,"//button[@class='button-1 login-button']")

print("Result of text: ", button_element.text) #LOG IN
print("Result of get attribute()", button_element.get_attribute('value')) #Return nothing
print("Result of get attribute()", button_element.get_attribute('type')) #Return submit


