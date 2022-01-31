import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


class DemoJs():
    def demo_JavaScript(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.salesforce.com/au/form/signup/freetrial-sales/?d=7010M000002JnsPQAS")
        #driver.get("https://training.rcvacademy.com/")
        driver.execute_script("window.open('https://training.rcvacademy.com/', '_self')")
        time.sleep(10)
        demo_element = driver.execute_script("return document.getElementsByTagName('p')[1];")
        driver.execute_script("arguments[0].click();", demo_element)

demojs = DemoJs()
demojs.demo_JavaScript()