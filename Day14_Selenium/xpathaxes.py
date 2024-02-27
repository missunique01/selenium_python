

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

driver_obj.get("https://money.rediff.com/gainers/bse/daily/groupa")

#---------------Maximize the browser window after loading--------------
driver_obj.maximize_window()

#---------------- XPATH Axes----------------------
#SELF
# text_msg = driver_obj.find_element(By.XPATH,"//a[contains(text(),'Indian Hotels Co')]/self::a").text
# print(text_msg) #Indian Hotels Co

# #Parent
# text_msg = driver_obj.find_element(By.XPATH,"//a[contains(text(),'Indian Hotels Co')]/parent::td").text
# print(text_msg) #Indian Hotels Co

#Child

# child_nodes = driver_obj.find_elements(By.XPATH,"//a[contains(text(),'Indian Hotels Co')]/ancestor::tr/child::td")
# print(len(child_nodes)) #5

#Ancestor

# text_msg = driver_obj.find_element(By.XPATH,"//a[contains(text(),'Indian Hotels Co')]/ancestor::tr").text
# print(text_msg) #Indian Hotels Co A 579.70 589.75 + 1.73

#Descendent
#
# descendents = driver_obj.find_elements(By.XPATH,"//a[contains(text(),'Indian Hotels Co')]/ancestor::tr/descendant::*")
# print("Number of descendent nodes : ",len(descendents))

#Following
# following_elements = driver_obj.find_elements(By.XPATH,"//a[contains(text(),'Indian Hotels Co')]/ancestor::tr/following::*")
# print("Number of following nodes : ",len(following_elements))

#Following Sibling

# following_sibling_elements = driver_obj.find_elements(By.XPATH,"//a[contains(text(),'Indian Hotels Co')]/ancestor::tr/following-sibling::*")
# print("Number of following siblings nodes : ",len(following_sibling_elements))  #196

#Preceeding
# preceding_elements = driver_obj.find_elements(By.XPATH,"//a[contains(text(),'Indian Hotels Co')]/ancestor::tr/preceding::tr")
# print("Number of preceding nodes : ",len(preceding_elements))  #81

#Precedding sibling
preceding_sib_elements = driver_obj.find_elements(By.XPATH,"//a[contains(text(),'Indian Hotels Co')]/ancestor::tr/preceding-sibling::tr")
print("Number of precedings siblings nodes : ",len(preceding_sib_elements))  #80



driver_obj.close()

