
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

#Service Object Creation

options = webdriver.ChromeOptions()
service_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")

options.add_experimental_option("detach",True)
driver_obj = webdriver.Chrome(service= service_obj, options=options)

driver_obj.implicitly_wait(10)

driver_obj.get("https://opensource-demo.orangehrmlive.com/")
driver_obj.maximize_window()
#Login to application
driver_obj.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
driver_obj.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
driver_obj.find_element(By.XPATH,"//button[@type='submit']").click()

#Go to Admin
driver_obj.find_element(By.LINK_TEXT,"Admin").click()
#Go to user Management
driver_obj.find_element(By.XPATH,"//li[1]/span[@class='oxd-topbar-body-nav-tab-item']").click()
#Go to USers
driver_obj.find_element(By.XPATH,"//a[@class='oxd-topbar-body-nav-tab-link']").click()

noOfRows = driver_obj.find_elements(By.XPATH,"//div[@class='oxd-table']//div[@class='oxd-table-body oxd-card-table-body']")
print(noOfRows)
# for r in range(1,len(noOfRows)+1):
#     print(r)

# //div[@class='orangehrm-container']
# //div[@class='orangehrm-container']/div[@class='oxd-table']/div[@class='rowgroup']
# //*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]