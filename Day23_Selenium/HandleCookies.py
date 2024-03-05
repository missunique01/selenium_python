from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
service_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
options.add_experimental_option("detach", True)
driver_obj = webdriver.Chrome(service=service_obj, options=options)
driver_obj.implicitly_wait(10)

driver_obj.get("https://demo.nopcommerce.com/")
driver_obj.maximize_window()

#Getting Cookies
cookies = driver_obj.get_cookies()
print("Size of Cookies: ", len(cookies))

#Printing details of all the cookies
# for c in cookies:
#     # print(c)
#     print(c.get('name'), ":", c.get('value'))

#Add new cookies to browser

driver_obj.add_cookie({"name": "MyCookie", "value" : "123456"})
cookies = driver_obj.get_cookies()
print("Size of Cookies after adding our own cookie: ", len(cookies))

#Deleting a Specific cookie from browser

driver_obj.delete_cookie("MyCookie")
cookies = driver_obj.get_cookies()
print("Size of Cookies after deletion: ", len(cookies))


#Delete all the cookies

driver_obj.delete_all_cookies()
cookies = driver_obj.get_cookies()
print("Size of Cookies after deleting all the cookies: ", len(cookies))

driver_obj.quit()