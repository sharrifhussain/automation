from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://candymapper.com/m/login?r=%2Fm%2Faccount")
#CSS selector by Email
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Email']").send_keys("sharrifhussain17@gmail.com")
#CSS selector by Password
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Password']").send_keys("Hussain786$")
#CSS selector by Sign-in button
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
driver.maximize_window()
input("Press enter to continue...")