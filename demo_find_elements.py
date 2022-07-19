import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class DemoFindElementByIDandName():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://yatra.com/")
        lista = driver.find_elements_by_tag_name('a')
        lista = driver.find_elements_by_tag_name('input')
        lista = driver.find_element(By.TAG_NAME, 'a')
        print(len(lista))
        for i in lista:
            print(i.text)
        time.sleep(10)

findbyid = DemoFindElementByIDandName()
findbyid.locate_by_id_demo()
