import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://getbootstrap.com/docs/5.0/components/dropdowns/")
driver.maximize_window()
driver.implicitly_wait(10)
dropdown1=driver.find_element(By.XPATH, "//span[@class='d-none d-lg-inline']")
# time.sleep(1)
dropdown1.click()

options=driver.find_element(By.XPATH, "//a[normalize-space()='All versions']")
options.click()
# time.sleep(1)
input("Press enter to continue...")

#time.sleep(2)  # Page dekhne ka time
#input("Press enter to continue...")
# dropdown=Select(driver.find_element(By.XPATH,"//select[@id='dropdown']"))
# time.sleep(1)
# dropdown.select_by_visible_text("Option 1")
# input("Press enter to continue...")
# time.sleep(1)



# login
# driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
# time.sleep(1)
# driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
# time.sleep(1)
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
# time.sleep(1)
#
# #Verify login success by checking Dashboard heading
# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, "//a[@class='oxd-main-menu-item active']"))
# )
# time.sleep(1)
#
# time.sleep(5)
# driver.quit()
# print("Login successfully")






