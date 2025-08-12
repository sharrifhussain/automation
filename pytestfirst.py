from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
def test_openbrowser():
    driver.get("https://www.w3schools.com/html/#gsc.tab=0")
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.quit()

