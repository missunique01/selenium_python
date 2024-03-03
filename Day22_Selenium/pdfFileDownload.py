

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
location = os.getcwd() #This will give the current working directory


def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    #Service Object Creation
    service_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
    #adding prefered location for downloadin the file using dictionaries
    # preferences = {"download.default_directory" : "C:/Users/home/PycharmProjects/Selenium_Python/Day22_Selenium"}
    preferences = {"download.default_directory": os.getcwd()}
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", preferences)
    driver_obj = webdriver.Chrome(service= service_obj, options=options)
    return driver_obj

#Edge Browser setup
def Edge_setup():
    from selenium.webdriver.edge.service import Service
    #Service Object Creation
    service_obj = Service("C:\Drivers\msedgedriver.exe")

    #adding prefered location for downloadin the file using dictionaries
    # preferences = {"download.default_directory":"C:/Users/home/PycharmProjects/Selenium_Python/Day22_Selenium"}
    preferences = {"download.default_directory": location}
    options = webdriver.EdgeOptions()
    options.add_experimental_option("prefs", preferences)
    driver_obj = webdriver.Edge(service= service_obj, options=options)
    return driver_obj
driver_obj = chrome_setup()

driver_obj.implicitly_wait(10)
driver_obj.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver_obj.maximize_window()
#This will downloaded in the chrome default location
driver_obj.find_element(By.XPATH,"//table[@id='table-files']//tbody/tr[1]//td[5]/a").click()


