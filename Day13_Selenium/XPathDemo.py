#https://automationexercise.com/

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

driver_obj.get("https://demo.nopcommerce.com/")

#---------------Maximize the browser window after loading--------------
driver_obj.maximize_window()

#Absolute XPATH
#/html/body/div[6]/div[1]/div[2]/div[2]/form/input
#/html/body/div[6]/div[1]/div[2]/div[2]/form/button
# driver_obj.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[2]/div[2]/form/input").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
# driver_obj.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[2]/div[2]/form/button").click()

#Relative Xpath
#//*[@id="small-searchterms"]
#//*[@id="small-search-box-form"]/button
# driver_obj.find_element(By.XPATH,"//*[@id='small-searchterms']").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
# driver_obj.find_element(By.XPATH,"//*[@id='small-search-box-form']/button").click()
# Relative path using OR Option
# driver_obj.find_element(By.XPATH,"//*[@id='small-searchterms' or @name ='q']").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
# driver_obj.find_element(By.XPATH,"//*[@id='small-search-box-form']/button").click()

# Relative path using AND Option
driver_obj.find_element(By.XPATH,"//*[@id='small-searchterms' and @name ='q']").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
driver_obj.find_element(By.XPATH,"//*[@id='small-search-box-form']/button").click()

#Contain()

driver_obj.find_element(By.XPATH, "//*[contains(@id,'searchterms')]").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
driver_obj.find_element(By.XPATH,"//*[@id='small-search-box-form']/button").click()

