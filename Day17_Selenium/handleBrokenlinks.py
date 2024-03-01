
#-----------------Import stataments--------------------------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
#------------------Object creations------------------------

service_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver_obj = webdriver.Chrome(service= service_obj, options=options)
#-----------------Waiting time 10 seconds for loading the window-----------
driver_obj.implicitly_wait(10)
#--------------------Get the url ---------------

driver_obj.get("https://phptravels.com/demo/")

driver_obj.maximize_window()

#Checking the broken links in the web page
allLinks = driver_obj.find_elements(By.XPATH,"//a")
count = 0

for i in allLinks:
    url = i.get_attribute('href')
    try:
        res = requests.head(url)
    except:
        None
    if res.status_code>=402:
        print(url,"is broken Link")
        count += 1
    else:
        print(url, "valid link")
print("Total number of broken links", count)

