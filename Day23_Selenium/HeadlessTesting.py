from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    service_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
    options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    options.headless = True
    driver_obj = webdriver.Chrome(service=service_obj, options=options)
    return driver_obj
def headless_Edge():
    from selenium.webdriver.edge.service import Service
    service_obj = Service("C:\Drivers\msedgedriver.exe")
    options = webdriver.EdgeOptions()
    # options.add_experimental_option("detach", True)
    options.headless = True
    driver_obj = webdriver.Edge(service=service_obj, options=options)
    return driver_obj
# driver_obj = headless_chrome()
driver_obj = headless_Edge()
driver_obj.get("https://demo.nopcommerce.com/")
print(driver_obj.title)
print(driver_obj.current_url)
driver_obj.close()