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
driver_obj.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver_obj.maximize_window()

#LOgin into application

driver_obj.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
driver_obj.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
driver_obj.find_element(By.XPATH,"//button[@type='submit']").click()

#Go to the other page OrangeHRM, Inc
driver_obj.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()

windowIds = driver_obj.window_handles

driver_obj.switch_to.window(windowIds[1])
# Solutions --> People Management --> Hr Administration
time.sleep(5)
solutions_Ele = driver_obj.find_element(By.XPATH,"//*[@id='navbarSupportedContent']/ul/li[1]/a")
time.sleep(5)
people_ele = driver_obj.find_element(By.XPATH,"//*[@id='navbarSupportedContent']/ul/li[1]/div/div/div/div/ul/li[1]")
time.sleep(5)
hrAdmin_ele = driver_obj.find_element(By.LINK_TEXT,"HR Administration")


#Mouse Hover Action
#Create a object for ActionaChains Class

actionchains_obj = ActionChains(driver_obj)

actionchains_obj.move_to_element(solutions_Ele).move_to_element(people_ele).move_to_element(hrAdmin_ele).click().perform()
