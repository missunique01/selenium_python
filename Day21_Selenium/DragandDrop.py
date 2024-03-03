
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

driver_obj.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

driver_obj.maximize_window()
act = ActionChains(driver_obj)


#-----------Rome & Italy--------------------------
rome_source_ele = driver_obj.find_element(By.ID,"box6")
italy_target_ele = driver_obj.find_element(By.ID, "box106")
act.drag_and_drop(rome_source_ele,italy_target_ele).perform()

#-------------------Seoul & South Korea-------------
seoul_source_ele = driver_obj.find_element(By.ID,"box5")
southkorea_target_ele = driver_obj.find_element(By.ID, "box105")
act.drag_and_drop(seoul_source_ele,southkorea_target_ele).perform()

#----------------------Washington & USA-----------------------------
WashingtonDC_source_ele = driver_obj.find_element(By.ID,"box3")
US_target_ele = driver_obj.find_element(By.ID, "box103")
act.drag_and_drop(WashingtonDC_source_ele,US_target_ele).perform()

#---------------------Stockholm & Sweden ------------------------------
Stockholm_source_ele = driver_obj.find_element(By.ID,"box2")
sweden_target_ele = driver_obj.find_element(By.ID, "box102")
act.drag_and_drop(Stockholm_source_ele,sweden_target_ele).perform()

#-----------------------Madrid &Spain -----------------------------
Madrid_source_ele = driver_obj.find_element(By.ID,"box7")
Spain_target_ele = driver_obj.find_element(By.ID, "box107")
act.drag_and_drop(Madrid_source_ele,Spain_target_ele).perform()

#-----------------------Oslo & Norway-----------------
Oslo_source_ele = driver_obj.find_element(By.ID,"box1")
Norway_target_ele = driver_obj.find_element(By.ID, "box101")
act.drag_and_drop(Oslo_source_ele,Norway_target_ele).perform()

#-----------------------Copenhagen & Denmark-----------------
Copenhagen_source_ele = driver_obj.find_element(By.ID,"box4")
Denmark_target_ele = driver_obj.find_element(By.ID, "box104")
act.drag_and_drop(Copenhagen_source_ele,Denmark_target_ele).perform()


