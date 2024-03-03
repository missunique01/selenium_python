
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

driver_obj.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_onclick3")

driver_obj.maximize_window()

frame_driver = driver_obj.find_element(By.XPATH,"//iframe[@id='iframeResult']")

driver_obj.switch_to.frame(frame_driver)

field1 = driver_obj.find_element(By.XPATH,"//input[@id='field1']")

field1.clear()
field1.send_keys("Hey Bootfiul")

button= driver_obj.find_element(By.XPATH,"/html/body/button")

act = ActionChains(driver_obj)

act.double_click(button).perform()