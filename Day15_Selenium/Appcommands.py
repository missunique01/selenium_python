
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

driver_obj.get("https://opensource-demo.orangehrmlive.com/")

driver_obj.maximize_window()
#------------Using title command-------

print(driver_obj.title) #OrangeHRM

print(driver_obj.current_url)  #https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
#----------To check the source code of the page use below
print(driver_obj.page_source)

driver_obj.quit()