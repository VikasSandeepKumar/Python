import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

class DemoScreenshot():
    def demo_screen_capture(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        continuedemo = driver.find_element(By.XPATH, "//button[@id='login-continue-btn']")
        continuedemo.screenshot(".\\test.png")
        contiunedemo.click()
        time.sleep(10)
        driver.get_screenshot_as_file("C:\\C:\\Users\Dheeraj Reddy\PycharmProjects\LearningPython\\error.jpg")
        driver.save_screenshot(".\\test1.png")

ddscreenshot = DemoScreenshot()
ddscreenshot.demo_screen_capture()