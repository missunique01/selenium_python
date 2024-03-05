import time

from Day24_Selenium import XlUtility
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import mysql.connector
options = webdriver.ChromeOptions()
service_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
options.add_experimental_option("detach",True)
driver_obj = webdriver.Chrome(service=service_obj,options=options)
driver_obj.implicitly_wait(10)

driver_obj.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver_obj.maximize_window()

try:
    con = mysql.connector.connect(host="localhost", port=3306,user="root",passwd = "Nazma786@", database = "pythonseleniumdb")
    curs = con.cursor()
    curs.execute("select * from caldata")

    #To print multiple records in the table
    for row in curs:

        #Capturing data from excel
        principle = row[0]
        rateofInterest = row[1]
        per1 = row[2]
        per2 =row[3]
        fre = row[4]
        exp_mat_Value = row[5]

        #Passing data to application
        driver_obj.find_element(By.XPATH,"//input[@id = 'principal']").send_keys(principle)
        driver_obj.find_element(By.XPATH,"//input[@id = 'interest']").send_keys(rateofInterest)
        driver_obj.find_element(By.XPATH,"//input[@id = 'tenure']").send_keys(per1)
        periodDrp = Select(driver_obj.find_element(By.XPATH,"//select[@id = 'tenurePeriod']"))
        periodDrp.select_by_visible_text(per2)
        freqDrp = Select(driver_obj.find_element(By.XPATH,"//select[@id = 'frequency']"))
        freqDrp.select_by_visible_text(fre)
        driver_obj.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[1]").click()

        #Calucalate the maturity value
        act_mvalue = driver_obj.find_element(By.XPATH,"//span[@id='resp_matval']/strong").text

        #Validation
        if float(exp_mat_Value) == float(act_mvalue):
            print("Test Passed")
        else:
            print("Test Failed")
        driver_obj.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]").click()
        time.sleep(5)
except:
    print("Connect Failed")

con.close()
driver_obj.close()
