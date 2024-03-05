
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from  selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver import Keys

options = webdriver.ChromeOptions()
service_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
options.add_experimental_option("detach",True)
driver_obj = webdriver.Chrome(service=service_obj,options=options)
driver_obj.implicitly_wait(10)

# driver_obj.get("https://demo.nopcommerce.com/")
# driver_obj.maximize_window()
# reg_link = Keys.CONTROL + Keys.RETURN
# # driver_obj.find_element(By.LINK_TEXT,"Register").send_keys(reg_link)
# driver_obj.find_element(By.LINK_TEXT,"Register").send_keys(Keys.CONTROL + Keys.RETURN)

#New Tab -Selenium4 : Opens a new tab and switches to new tab

# driver_obj.get("https://demo.nopcommerce.com/")
# driver_obj.switch_to.new_window('tab')
# driver_obj.get("https://www.orangehrm.com/")

#New Window -Selenium4 : Opens a new browser window and switches to new window
driver_obj.get("https://demo.nopcommerce.com/")
driver_obj.switch_to.new_window('window')
driver_obj.get("https://www.orangehrm.com/")