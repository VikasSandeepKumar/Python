import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

class DemoAutosuggest():
    def demo_autosuggest_dropdown(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.yatra.com")
        depart_from = driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']").click()
        depart_from.click()
        time.sleep(6)
        depart_from.send_text("New Delhi")
        time.sleep(6)
        depart_from.send.keys(keys.Enter)
        time.sleep(6)
        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.send_keys("New")
        search_results = driver.find_element(By.XPATH, "//div[@class='viewport]//div[1]/li")
        print(len(search_results))

        for results in search_results:
            print(results.text)
            if "New York (JFK)" in results.text:
                results.click()
                time.sleep(6)
                break


dauto = DemoAutosuggest()
dauto.demo_autosuggest_dropdown()


