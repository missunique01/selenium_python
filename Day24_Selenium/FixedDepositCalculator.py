import time

from Day24_Selenium import XlUtility
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

options = webdriver.ChromeOptions()
service_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
options.add_experimental_option("detach",True)
driver_obj = webdriver.Chrome(service=service_obj,options=options)
driver_obj.implicitly_wait(10)

driver_obj.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver_obj.maximize_window()

file = "C:\Selenium_Practice_Data_Files\calData.xlsx"

rows = XlUtility.getRowCount(file,"Sheet1")
#Capturing data from excel
for r in range(2,rows+1):
    principle = XlUtility.readData(file,"Sheet1", r, 1)
    rateofInterest = XlUtility.readData(file, "Sheet1", r, 2)
    per1 = XlUtility.readData(file, "Sheet1", r, 3)
    per2 = XlUtility.readData(file, "Sheet1", r, 4)
    fre = XlUtility.readData(file, "Sheet1", r, 5)
    exp_mat_Value = XlUtility.readData(file, "Sheet1", r, 6)

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
        XlUtility.writeData(file,"Sheet1",r,8,"Passed")
        XlUtility.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("Test Failed")
        XlUtility.writeData(file, "Sheet1", r, 8, "Failed")
        XlUtility.fillRedColor(file,"Sheet1",r,8)
    driver_obj.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]").click()

    time.sleep(5)

driver_obj.close()