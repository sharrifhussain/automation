from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#By using Relative XPATH
driver.get("https://candymapper.com/m/login?r=%2Fm%2Faccount")
#XPATH By Email
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("sharrifhussain17@gmail.com")
#XPATH By Password
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Hussain786$")
#XPATH By Sign-in button
driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.maximize_window()
input("Press enter to continue...")

# #By using Absoulte XPATH
# driver.get("https://candymapper.com/m/login?r=%2Fm%2Faccount")
# #XPATH By Email
# driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/section[1]/div[1]/span[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]").send_keys("sharrifhussain17@gmail.com")
# #XPATH By Password
# driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/section[1]/div[1]/span[1]/div[1]/div[1]/div[1]/form[1]/div[2]/input[1]").send_keys("Hussain786$")
# #XPATH By Sign-in button
# driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/section[1]/div[1]/span[1]/div[1]/div[1]/div[1]/form[1]/div[3]/button[1]").click()
# driver.maximize_window()
# input("Press enter to continue...")







