import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
class Product():
    def __init__(self, driver):
        self.driver=driver

    def add_product1(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//div[@id='tbodyid']//div[1]//div[1]//a[1]//img[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//a[@class='btn btn-success btn-lg']").click()
        time.sleep(2)
        alert=Alert(self.driver)
        alert.accept()
    def add_product2(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@class='col-lg-9']//div[2]//div[1]//a[1]//img[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[@class='btn btn-success btn-lg']").click()
        time.sleep(2)
        alert = Alert(self.driver)
        alert.accept()
        alert.accept()




