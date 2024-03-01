
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
driver_obj.implicitly_wait(10)
#--------------------Get the url ---------------

driver_obj.get("https://rahulshettyacademy.com/AutomationPractice/")

driver_obj.maximize_window()

# driver_obj.find_element(By.XPATH,"//input[@id = 'checkBoxOption1']").click()

mul_elements = driver_obj.find_elements(By.XPATH,"//input[@type = 'checkbox']")

print(len(mul_elements))
#Approach1
# for i in range(len(mul_elements)):
#     mul_elements[i].click()

#Appraoch2

# for checkbox in mul_elements:
#     checkbox.click()

#Select multiple checkboxes by choice
# for checkbox in mul_elements:
#     checkbox_Options = checkbox.get_attribute('value')
#     if checkbox_Options == 'option1' or checkbox_Options == "option3":
#         checkbox.click()

#Select Last two checkboxes
# # range(1,2)
# len_mul_elements = len(mul_elements)
#
# for i in range(len_mul_elements-2, len_mul_elements):
#     mul_elements[i].click()

#Select first 2 checkboxes

# len_mul_elements = len(mul_elements)
# for i in range(len_mul_elements):
#     if i<2:
#         mul_elements[i].click()

#clearing the checkboxes

for i in range(len(mul_elements)):
    mul_elements[i].click()
for i in range(len(mul_elements)):
    if mul_elements[i].is_selected():
        mul_elements[i].click()


