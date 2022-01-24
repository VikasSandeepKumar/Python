import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class DemoFindElementByIDandName():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("http://www.yatra.com/")
        driver.find_elements_by_partial_link_text('Yatra for').click()
        #driver.find_element_by_link_text('Yatra for Business').click()
        time.sleep(10)

findbyid = DemoFindElementByIDandName()
findbyid.locate_by_id_demo()
