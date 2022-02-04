import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class DemoSliders():
    def sliders_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.allonlinestore.in/men/")
        driver.maximize_window()
        elem1 = driver.find_element_by_xpath("//span[@class='irs-handle from']")
        elem2 = driver.find_element_by_xpath("//span[@class='irs-handle to']")
        #ActionChains(driver).drag_and_drop_by_offset(elem1, 60, 0).perform()
        #ActionChains(driver).click_and_hold(elem1).pause(1).move_by_offset(50, 0).release().perform()
        #ActionChains(driver).move_to_element(elem1).pause(1).click_and_hold(elem1).move_by_offset(80, 0).release().perform()
        ActionChains(driver).move_to_element(elem2).pause(1).click_and_hold(elem2).move_by_offset(-80, 0).release().perform()
        time.sleep(4)

ds = DemoSliders()
ds.sliders_demo()
