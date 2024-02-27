#Importing
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
driver_obj.get("https://demo.nopcommerce.com/")
driver_obj.maximize_window()

#Locator ID
#driver_obj.find_element(By.ID, "small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

#Locator Name
driver_obj.find_element(By.NAME,"q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
#LOcator Link_Text and Partial_Link_text
# driver_obj.find_element(By.PARTIAL_LINK_TEXT,"Register").click()
#driver_obj.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()


#driver_obj.close()