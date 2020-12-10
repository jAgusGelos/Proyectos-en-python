from selenium import webdriver
from time import sleep

class AfipBot:
    def __init__(self):
        self.driver = webdriver.Chrome("C:\\Program Files (x86)\\WebDriver\\chromedriver.exe")
        self.driver.get("https://serviciosjava2.afip.gob.ar/rcel/jsp/menu_ppal.jsp")
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[1]/td/a/span[2]").click()



AfipBot()