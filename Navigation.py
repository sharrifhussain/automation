import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class Navigation:
    def open_site(self):
     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
     driver.get("https://www.demoblaze.com/index.html")
     driver.implicitly_wait(1000)
     driver.maximize_window()
     return driver