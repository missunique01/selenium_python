import time

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
#This will automatically decrease the synchronization problem
#This is applicable for all commands
driver_obj.implicitly_wait(10)
#--------------------Get the url ---------------

driver_obj.get("https://www.google.com")
driver_obj.maximize_window()
search_box = driver_obj.find_element(By.NAME,'q')
search_box.send_keys("Selenium")
search_box.submit()

# time.sleep(5)
driver_obj.find_element(By.XPATH,"//h3[text()='Selenium']").click()

driver_obj.quit()