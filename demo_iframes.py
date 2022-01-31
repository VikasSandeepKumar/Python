import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class DemoIframe():
    def demo_frames(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        driver.maximize_window()
        #Switch with iframe locator
        #driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='iframeResult']"))
        #Switch with ID
        driver.switch_to.frame("iframeResult")
        #Switch with name
        #driver.switch_to.frame("iframeResult")
        #Switch with index
        driver.switch_to.frame(0)
        driver.find_element(By.XPATH, "//a[@id='w3loginbtn']").click()
        time.sleep(5)
diframe = DemoIframe()
diframe.demo_frames()