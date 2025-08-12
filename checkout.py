import time
from selenium.webdriver.common.by import By
class Checkout():
    def __init__(self,driver):
        self.driver=driver
    def place_order(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Cart']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Place Order']").click()
        time.sleep(2)
        self.driver.find_element(By.ID,"name").send_keys("Alex")
        self.driver.find_element(By.ID, "country").send_keys("Pakistan")
        self.driver.find_element(By.ID, "city").send_keys("Rawaplindi")
        self.driver.find_element(By.ID, "card").send_keys("411111111111")
        self.driver.find_element(By.ID, "month").send_keys("June")
        self.driver.find_element(By.ID, "year").send_keys("2029")
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Purchase']").click()
        time.sleep(2)
        confirmation=self.driver.find_element(By.XPATH,"//h2[normalize-space()='Thank you for your purchase!']").text
        print("Order confirmed", confirmation)
        self.driver.find_element(By.XPATH,"//button[normalize-space()='OK']").click()
        time.sleep(2)
        # Back to homepage
        self.driver.find_element(By.XPATH, "//li[@class='nav-item active']//a[@class='nav-link']").click()
        time.sleep(2)
    def place_order2(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Cart']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Place Order']").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "name").send_keys("John")
        self.driver.find_element(By.ID, "country").send_keys("Australia")
        self.driver.find_element(By.ID, "city").send_keys("Perth")
        self.driver.find_element(By.ID, "card").send_keys("52222222222")
        self.driver.find_element(By.ID, "month").send_keys("July")
        self.driver.find_element(By.ID, "year").send_keys("2030")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Purchase']").click()
        time.sleep(2)
        confirmation = self.driver.find_element(By.XPATH, "//h2[normalize-space()='Thank you for your purchase!']").text
        print("Order confirmed", confirmation)

