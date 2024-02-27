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
driver_obj.get("https://www.facebook.com/")
driver_obj.maximize_window()

#tag id

#driver_obj.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")
#driver_obj.find_element(By.CSS_SELECTOR,"#email").send_keys("abc123@gmail.com")
#Tag Class
#driver_obj.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc")
#driver_obj.find_element(By.CSS_SELECTOR,".inputtext").send_keys("abc")

#tag & attribute
#driver_obj.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("abcdefght")
#driver_obj.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("abcdefght")

#Tag class &attribute
driver_obj.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass]").send_keys("abcdefhgt&645")


#<div class="_6lux"><div class="_6luy _55r1 _1kbt _9nyh" id="passContainer">
# <input type="password" class="inputtext _55r1 _6luy _9npi" name="pass" id="pass" data-testid="royal_pass"
# placeholder="Password" aria-label="Password"><div class="_9ls7 hidden_elem" id="u_0_3_yI">
# <a href="#" role="button"><div class="_9lsa"><div class="_9lsb" id="u_0_4_e8"></div></div></a></div></div></div>