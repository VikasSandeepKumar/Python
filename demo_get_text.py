import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class DemoGetText():
    def demo_gettext(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://yatra.com")
        #text = driver.find_element_by_xpath(""//a[@href='https://www.yatra.com/travel-guidelines/international/switzerland']//div[@class='imgRes']//img").text
        text1 = driver.find_elements_by_link_text('Yatra for Business').text

        print(text1)
        driver.maximize_window()
        time.sleep(60)

findbyid = DemoGetText()
findbyid.demo_gettext()