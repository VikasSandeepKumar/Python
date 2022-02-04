import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager

class DemoMouseOver():
    def demo_mouse_events(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.yatra.com/")
        morebutton = driver.find_element_by_xpath("//span[@class='more-arr']")
        achains = ActionChains(driver)
        achains.move_to_element(morebutton).perform()
        time.sleep(3)
        driver.find_element_by_xpath("//span[normalize-space()='Xplore']").click()
        time.sleep(3)

dmouse = DemoMouseOver()
dmouse.demo_mouse_events()

