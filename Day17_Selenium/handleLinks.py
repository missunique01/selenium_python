
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
driver_obj.implicitly_wait(10)
#--------------------Get the url ---------------

driver_obj.get("https://demo.nopcommerce.com/")

driver_obj.maximize_window()

# driver_obj.find_element(By.LINK_TEXT,"Digital downloads").click()
# driver_obj.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()

#FInd number of links in a page

#Approach1 using Tag_NAME
# no_of_links = driver_obj.find_elements(By.TAG_NAME,"a")
# print(len(no_of_links)) #90

#Approach2 Using XPATH
no_of_links = driver_obj.find_elements(By.XPATH,"//a")
print(len(no_of_links))  #90

#print all the link Names in the console window
for i in no_of_links:
    print(i.text)