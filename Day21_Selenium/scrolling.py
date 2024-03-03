import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

#Service Object Creation

options = webdriver.ChromeOptions()
service_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")

options.add_experimental_option("detach",True)
driver_obj = webdriver.Chrome(service= service_obj, options=options)

driver_obj.implicitly_wait(20)

#Go to application


driver_obj.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver_obj.maximize_window()

time.sleep(10)

#1 Scroll down the page till some pixel number

# driver_obj.execute_script("window.scrollBy(0,3000)", "")
# value = driver_obj.execute_script("return window.pageYOffset;")
# print("No of pixels moved", value)

#2 Scroll down till element is found
# flag = driver_obj.find_element(By.XPATH,"//img[@alt='Flag of India']")
# driver_obj.execute_script("arguments[0].scrollIntoView()", flag)
# flag_value =  driver_obj.execute_script("return window.pageYOffset;")
# print("No of pixels moved", flag_value)  #No of pixels moved 7549

#3 Scroll down till end
driver_obj.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value_end = driver_obj.execute_script("return window.pageYOffset;")
print("No of pixels moved", value_end)  #No of pixels moved 9527

time.sleep(5)
#4 Scroll back to start from end
driver_obj.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value_start = driver_obj.execute_script("return window.pageYOffset;")
print("No of pixels moved", value_start)  #No of pixels moved 0

