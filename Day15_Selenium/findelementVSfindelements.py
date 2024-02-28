
#-----------------Import stataments--------------------------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#------------------Object creations------------------------

service_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver_obj = webdriver.Chrome(service= service_obj, options=options)
#-----------------Waiting time 10 seconds for loading the window-----------
#------------- method to wait for elements to become available before throwing an exception------------
driver_obj.implicitly_wait(10)
#--------------------Get the url ---------------

driver_obj.get("https://demo.nopcommerce.com/")

#Find element() method

#1) Locator matching with single web element
# single_element = driver_obj.find_element(By.XPATH,"//input[@id = 'small-searchterms']")
# single_element.send_keys("Lenovo Thinkpad X1 Carbon Laptop")

#2) Locator matching with multiple web elements

# multiple_elements = driver_obj.find_element(By.XPATH,"//div[@class = 'footer']//a")
# print(multiple_elements.text)  #Sitemap #it printed the first element from the web page

# 3) element not available in the web page will throw an exception (NoSuchElementException)

# login_element = driver_obj.find_element(By.LINK_TEXT,"Log")
# login_element.click()  #selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"link text","selector":"Log"}

#find_elements ---

#1) Locator matching with single web element
elements = driver_obj.find_elements(By.XPATH,"//input[@id = 'small-searchterms']")
# print(len(elements))  #1
# #to access the elemeing use as below
# #Because it stored as list & sending data
# elements[0].send_keys("Lenovo Thinkpad X1 Carbon Laptop")

#2) Locator matching with multiple web elements

# multiple_elements = driver_obj.find_elements(By.XPATH,"//div[@class = 'footer']//a")
# print(len(multiple_elements))  #23 web elements are available
# #To print the first web element
# print(multiple_elements[0].text)  #Sitemap
# for i in range(len(multiple_elements)):
#     print(multiple_elements[i].text)  #Printed all the web elements
# Sitemap
# Shipping & returns
# Privacy notice
# Conditions of Use
# About us
# Contact us
# Search
# News
# Blog
# Recently viewed products
# Compare products list
# New products
# My account
# Orders
# Addresses
# Shopping cart
# Wishlist
# Apply for vendor account
# Facebook
# Twitter
# RSS
# YouTube
# nopCommerce

#----------------------------------
# 3) element not available in the web page then this will simple return 0

login_element = driver_obj.find_elements(By.LINK_TEXT,"Log")
print("Elements Returned:", len(login_element))  #0
# login_element.click()  #selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"link text","selector":"Log"}
