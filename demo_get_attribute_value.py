import time
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager

class DemoGetAttributeValue():
    def demo_getvalue(self):
        driver = webdriver.Chrome(executable_path="\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://yatra.com")
        driver.maximize_window()
        attr_value = driver.find_elements_by_xpath("//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").get_attribute("value")
        print(attr_value)
        time.sleep(4)

attrobj = DemoGetAttributeValue()
attrobj.demo_getvalue()
