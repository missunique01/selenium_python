
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

driver_obj.get("https://rahulshettyacademy.com/AutomationPractice/")

mousehover_ele = driver_obj.find_element(By.XPATH,"//button[@id='mousehover']")
top_ele = driver_obj.find_element(By.XPATH,"//div[@class='mouse-hover-content']/a[1]")

#Mouse Hover Action
#Create a object for ActionaChains Class

actionchains_obj = ActionChains(driver_obj)

actionchains_obj.move_to_element(mousehover_ele).move_to_element(top_ele).click().perform()

