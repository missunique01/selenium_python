from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#object creation
service_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver_obj = webdriver.Chrome(service=service_obj, options=options)
driver_obj.implicitly_wait(10)
#Opening the URL
driver_obj.get("https://automationexercise.com/")
driver_obj.maximize_window()

# sliders = driver_obj.find_elements(By.CLASS_NAME,"carousel-indicators")
# print(len(sliders))

links = driver_obj.find_elements(By.TAG_NAME,'a')
print(len(links))


