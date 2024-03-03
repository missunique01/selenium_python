
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

#Service Object Creation

options = webdriver.ChromeOptions()
service_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")

options.add_experimental_option("detach",True)
driver_obj = webdriver.Chrome(service= service_obj, options=options)

driver_obj.implicitly_wait(10)

driver_obj.get("https://text-compare.com/")

input1 = driver_obj.find_element(By.XPATH,"//textarea[@name='text1']")
input2 = driver_obj.find_element(By.XPATH,"//textarea[@name='text2']")

input1.send_keys("Hello Selenium")

act= ActionChains(driver_obj)

#input1 - Select the text (ctrl+A)
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()
# act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

#input1 - Copy the text (ctrl + C)

act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)
act.perform()

# act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

#switch tab to navigate to input2

act.send_keys(Keys.TAB)
act.perform()

# act.send_keys(Keys.TAB).perform()

#input2 - Paste the data (Ctrl+V)

act.key_down(Keys.CONTROL)
act.send_keys("v")
act.key_up(Keys.CONTROL)
act.perform()

# act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

