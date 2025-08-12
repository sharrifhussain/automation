from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.applitools.com/app.html")
driver.save_screenshot("test.png")
driver.implicitly_wait(10)
driver.maximize_window()
input("Press enter to continue...")