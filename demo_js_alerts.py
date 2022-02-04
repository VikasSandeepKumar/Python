import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class DemoJsPopup():
    def demo_js_alerts(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_prompt")
        driver.switch_to.frame("iframeResult")
        driver.maximize_window()
        # Accept alert
        # driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        # time.sleep(2)
        # driver.switch_to.alert.accept()
        # time.sleep(2)

        # Dismiss alert
        # driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        # time.sleep(2)
        # driver.switch_to.alert.dismiss()
        # time.sleep(2)
        #
        # Send text in alert
        #driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        driver.find_element_by_xpath("//button[normalize-space()='Try it']").click()
        time.sleep(2)
        driver.switch_to.alert.send_keys(" Hyderabad ")
        driver.switch_to.alert.accept()
        time.sleep(2)

dpopup = DemoJsPopup()
dpopup.demo_js_alerts()
