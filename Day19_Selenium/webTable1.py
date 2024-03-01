
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

driver_obj.implicitly_wait(1)

driver_obj.get("https://testautomationpractice.blogspot.com/")

driver_obj.maximize_window()
#1 Counts number of rows & Columns

# noOfRows  = driver_obj.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
# print("No of rows in the table: ", len(noOfRows))  #7

# noOfColumns = driver_obj.find_elements(By.XPATH,"//table[@name='BookTable']//tbody//tr[1]/th")
# print("No of columns in the table: ", len(noOfColumns))  #4

#2 Read Specific row and column data

# specific_data = driver_obj.find_element(By.XPATH,"//table[@name='BookTable']//tr[5]//td[1]")
# print(specific_data.text)  #Master In Selenium


#Read all the rows and columns
#Approach1
# noOfRows = driver_obj.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
# print(len(noOfRows))
# noOfColumns = driver_obj.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr/td")
# print(len(noOfColumns))
# # print("Printing all the rows & columns in the table")
# for r in range(2, len(noOfRows)+1):
#     for c in noOfColumns:
#         print(c.text)

#Appraoch2
# noOfRows = driver_obj.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
# print(len(noOfRows))
# noOfColumns = driver_obj.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr/th")
# print(len(noOfColumns))
# # print("Printing all the rows & columns in the table")
# for r in range(2, len(noOfRows)+1):
#     for c in range(1,len(noOfColumns)+1):
#         all_data = driver_obj.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(all_data, end="      ")  #end is used to print each row data in a single line -----
#     print() #This is will give some spcae for each row data

#4 Read data based on condition (List book name whoauthor is Mukesh)
noOfRows = driver_obj.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr")

for r in range(2,len(noOfRows)+1):
    author = driver_obj.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if author == "Mukesh":
        bookName = driver_obj.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        prize_of_Book = driver_obj.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[4]").text
        print("Book Name is ", bookName,"And the author name is ", author, "The prize of book is ",prize_of_Book)
