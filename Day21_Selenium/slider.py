
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

driver_obj.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")

driver_obj.maximize_window()

min_slider = driver_obj.find_element(By.XPATH,"/html/body/div[2]/div[2]/span[1]")

max_slider = driver_obj.find_element(By.XPATH,"/html/body/div[2]/div[2]/span[2]")

print("Before moving slider locations")
print(min_slider.location)  # {'x': 59, 'y': 250}
print(max_slider.location)  # {'x': 545, 'y': 250}

act = ActionChains(driver_obj)


act.drag_and_drop_by_offset(min_slider,100,0).perform()
act.drag_and_drop_by_offset(max_slider,-100,0).perform()

print("After moving Slider Locations")
print(min_slider.location)  # {'x': 161, 'y': 250}
print(max_slider.location)  # {'x': 443, 'y': 250}