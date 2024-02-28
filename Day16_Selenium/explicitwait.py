import time

#-----------------Import stataments--------------------------
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#------------------Object creations------------------------

service_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver_obj = webdriver.Chrome(service= service_obj, options=options)
#-----------Create object for WebDriverwait class which will take 2 params one is driver obj and the time
# mywait = WebDriverWait(driver_obj,10)  #Explicit wait declaration
mywait = WebDriverWait(driver_obj,10, poll_frequency=2, ignored_exceptions= [NoSuchElementException,
                                                           ElementNotVisibleException,
                                                           ElementNotSelectableException,
                                                           Exception])
#--------------------Get the url ---------------

driver_obj.get("https://www.google.com")
driver_obj.maximize_window()
search_box = driver_obj.find_element(By.NAME,'q')
search_box.send_keys("Selenium")
search_box.submit()

#Usage of Explicit wait object
searchlink = mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
searchlink.click()

# driver_obj.find_element(By.XPATH,"//h3[text()='Selenium']").click()

driver_obj.quit()