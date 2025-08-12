from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.applitools.com/app.html")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Start typing to search...']").send_keys("Hello")
driver.maximize_window()
input("Press enter to continue...")


