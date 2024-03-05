import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
service_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
options.add_experimental_option("detach",True)
driver_obj = webdriver.Chrome(service=service_obj, options=options)
driver_obj.implicitly_wait(10)

driver_obj.get("https://demo.nopcommerce.com/")
driver_obj.maximize_window()

# driver_obj.save_screenshot("C:\\Users\\home\\PycharmProjects\\Selenium_Python\\Day23_Selenium\\homepage.png")
driver_obj.save_screenshot(os.getcwd() + "\\homepage.png")

# driver_obj.get_screenshot_as_file(os.getcwd() + "\\homepage.png")

# driver_obj.get_screenshot_as_base64() driver_obj.get_screenshot_as_png() #Save in binary format
driver_obj.quit()