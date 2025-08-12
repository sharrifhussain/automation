from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://codepen.io/RobotsPlay/pres/pyNLdL?editors=1000")
driver.implicitly_wait(10)
driver.maximize_window()
iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)

wait = WebDriverWait(driver, 10)
dropdownCheckboxes = driver.find_element(By.XPATH, "//label[@class='dropdown-label']")
dropdownCheckboxes.click()

option = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Selection One']")))
option.click()
input("Press enter to continue...")


