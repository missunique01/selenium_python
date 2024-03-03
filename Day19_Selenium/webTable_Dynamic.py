
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

# Admin --> USer Management ---> Users
driver_obj.find_element(By.LINK_TEXT,"Admin").click()
driver_obj.find_element(By.XPATH,"//li[1]/span[@class='oxd-topbar-body-nav-tab-item']").click()
driver_obj.find_element(By.XPATH,"//a[@class='oxd-topbar-body-nav-tab-link']").click()


#Check How many users are enabled and how many are in disabled status

noOfRows = driver_obj.find_elements(By.XPATH,"//div[@class='oxd-table-body']/div[@class='oxd-table-card']")

print("Total no of rows in a table are: ",len(noOfRows))
status_count = 0
Total = len(noOfRows)
#Specific Elements Status
for r in range(1,len(noOfRows)+1):
    status = driver_obj.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div["+str(r)+"]/div/div[5]").text
    if status == "Enabled":
        status_count += 1

print("Total number of users are: ", Total)
print("Total number of user in Enabled Status are: ",status_count)
print("Total number os users in Disabled Status are: ", (Total-status_count))


#  //*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div["+str(r)+"]/div/div[5]
# //*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div[5]
# //div[@class='oxd-table-body']/div[@class='oxd-table-card']//div[@role='row']//div[@role='cell' and @xpath='5']