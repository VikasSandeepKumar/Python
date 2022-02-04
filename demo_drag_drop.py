import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class DemoDragDrop():
    def drag_drop(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://jqueryui.com/droppable/")
        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@class='demo-frame']"))
        elem1 = driver.find_element_by_id("draggable")
        elem2 = driver.find_element_by_id("droppable")
        #ActionChains(driver).drag_and_drop(elem1, elem2).perform()
        ActionChains(driver).drag_and_drop_by_offset(elem1, 419, 238).perform()
        
        time.sleep(5)

dd = DemoDragDrop()
dd.drag_drop()

