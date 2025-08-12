from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://candymapper.com/")

#Scroll by Pixels
driver.execute_script("window.scrollBo(0, 1000);")

#Scroll by sepecific element:
# element =driver.find_element(By.XPATH, "//button[@type='submit']")
# driver.execute_script("arguments[0].scrollIntoView(true);", element)

#Scroll to Bottom (Infinite Scroll pages ke liye)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.implicitly_wait(10)
driver.maximize_window()
input("Press enter to continue...")
