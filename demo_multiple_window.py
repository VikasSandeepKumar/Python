import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class DemoMultipleWindow():
    def demo_window(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.yatra.com/")
        parent_handle = driver.current_window_handle
        print(parent_handle)
        driver.find_element(By.XPATH, "//a[@title='Offers']").click()
        all_handles = driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to_window(handle)
                driver.find_element(By.XPATH, "//a[normalize-space()='Confirm your Eligibility']")
                time.sleep(10)
                driver.close()
                time.sleep(10)
                break

        #driver.switch_to_window(parent_handle)
        driver.find_element(By.XPATH,"//a[@title='Offers']").click()

dmultiplewindows = DemoMultipleWindow()
dmultiplewindows.demo_window()