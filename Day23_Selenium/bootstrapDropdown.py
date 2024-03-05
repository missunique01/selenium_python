
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()

service_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")

options.add_experimental_option("detach", True)

driver_obj = webdriver.Chrome(service=service_obj, options=options)

driver_obj.implicitly_wait(10)

driver_obj.get("https://www.dummyticket.com/")
driver_obj.maximize_window()
driver_obj.find_element(By.LINK_TEXT,"Buy Ticket").click()

#perform click action on the Countru filed s
driver_obj.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()

#Capturing all the elements from the dropdown
country_ele = driver_obj.find_elements(By.XPATH,"//ul[@class='select2-results__options']//li")

print("Total countries available in the dropdown list are:", len(country_ele))

for i in country_ele:
    if i.text == "India":
        i.click()
        break



# for i in range(1,len(country_ele)+1):
#     if country_ele[i].text == "India":
#         driver_obj.find_element(By.XPATH,"//ul[@class='select2-results__options']//li["+str(i)+"]").click()
#         break
# driver_obj.close()