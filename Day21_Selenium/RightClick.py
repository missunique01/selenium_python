
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

driver_obj.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

driver_obj.maximize_window()

button_rightclick = driver_obj.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")

act = ActionChains(driver_obj)
act.context_click(button_rightclick).perform()