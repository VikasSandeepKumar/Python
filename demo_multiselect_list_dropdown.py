import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

class DemoDropdownMultiSelect():
    def demo_dropdown(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.seleniumeasy.com/test/basic-select-dropdowm-demo.html")
        dd_demo = driver.find_element_by_id("multi-selet")
        dd_multiple = Select(dd_demo)

        dd_multi.select_by_index(1)
        dd_multi.select_by_value("New Jersey")
        dd_multi.select_by_visible_text()

        dd_multi.select_by_index(4)
        dd_multi.select_by_value("Ohio")
        dd_multi.select_by_visible_text("Texas")

demo_multiselect = DemoDropdownMultiSelect()
demo_multiselect.demo_dropdown()
