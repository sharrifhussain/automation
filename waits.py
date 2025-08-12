from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
driver.maximize_window()
driver.implicitly_wait(10)
startbutton=driver.find_element(By.CSS_SELECTOR, "div[id='start'] button")
startbutton.click()
print("start waiting button for the next text hat is hello world")

hellotext= wait = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "finish")))
print("textappeard", hellotext.text)
input("Press enter to continue...")


