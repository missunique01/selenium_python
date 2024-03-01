from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

#Service Object Creation

service_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver_obj = webdriver.Chrome(service= service_obj, options=options)

driver_obj.implicitly_wait(10)

driver_obj.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver_obj.maximize_window()

# windowId = driver_obj.current_window_handle
#
# print(windowId)  #F2DC3261F0538360FB325A260ACFC9CF

driver_obj.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
windowIDs = driver_obj.window_handles

#Approach1
# parentWindowID = windowIDs[0]
# childWindowID = windowIDs[1]
# # print(parentWindowID) #F1C1D7CDB0DC504C35959517C1861507
# # print(childWindowID) #B723781D482650D1772B12EDAA0CCB7C
# driver_obj.switch_to.window(childWindowID)
# print("Title of Child Window", driver_obj.title)  #OrangeHRM HR Software | OrangeHRM
# driver_obj.switch_to.window(parentWindowID)
# print("Title of Parent Window", driver_obj.title) #OrangeHRM

# #Approach2 -Reading each window nand printing the titles
# for i in windowIDs:
#     driver_obj.switch_to.window(i)
#     print(driver_obj.title)

#Want to close specific windows
for i in windowIDs:
    driver_obj.switch_to.window(i)
    if driver_obj.title == "OrangeHRM HR Software | OrangeHRM":
        driver_obj.close()
