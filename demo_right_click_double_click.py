import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager

class DemoRightDoubleClick():
    def demo_right_double(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")

        #Right click
        # achains = ActionChains(driver)
        # elem1 = driver.find_element_by_xpath("//span[@class='context-menu-one btn btn-neutral']")
        # copyelem = driver.find_element_by_xpath("//span[normalize-space()='Copy']")
        # achains.context_click(elem1).perform()
        # time.sleep(5)
        # copyelem.click()
        # # time.sleep(3)

        # Double Click
        achains = ActionChains(driver)
        elem2 = driver.find_element_by_xpath("//button[normalize-space()='Double-Click Me To See Alert']")
        achains.double_click(elem2).perform()
        time.sleep(3)



drightclick = DemoRightDoubleClick()
drightclick.demo_right_double()