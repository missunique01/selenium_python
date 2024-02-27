# 1)Open the browser
# 2) Open URL - https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
# 3) enter username
# 4) enter password
# 5) Click on logging
# 6)Capture the title of home page
# 7) verify the home page -OrangeHRMD(Expected value)
# 8) Close the browser
import threading

#---------------------------------Write the program------------------------------------
#Import the necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Create a object for chrome class using webdriver and pass the driver .exe file path
service_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver_obj = webdriver.Chrome(service=service_obj, options=options)
driver_obj.implicitly_wait(10)
#Open the URL using the get() through driver object
driver_obj.get("https://opensource-demo.orangehrmlive.com")
driver_obj.find_element(By.NAME,"username").send_keys("Admin")
driver_obj.find_element(By.NAME,"password").send_keys("admin123")
driver_obj.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
# driver_obj.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
actual_title = driver_obj.title
expected_title = "OrangeHRM"
if actual_title == expected_title:
    print("Test case passed")
else:
    print("Test case failed")
driver_obj.close()