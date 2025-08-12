from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://petstore.octoperf.com/actions/Account.action?signonForm=")
#driver.get("https://petstore.octoperf.com/actions/Account.action?newAccountForm=")
driver.find_element(By.LINK_TEXT,"www.mybatis.org").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"www.mybatis.org").click()
#driver.find_element(By.LINK_TEXT,"Register Now!").click()
# driver.find_element(By.NAME, "username").send_keys("sharrifhussain17@gmail.com")
# driver.find_element(By.NAME, "password").send_keys("Hussain786@")
# driver.find_element(By.NAME, "repeatedPassword").send_keys("Hussain786@")
# driver.find_element(By.NAME, "account.firstName").send_keys("Ahmed")
# driver.find_element(By.NAME, "account.lastName").send_keys("ali")
# driver.find_element(By.NAME, "account.email").send_keys("sharrifhussain17@gmail.com")
# driver.find_element(By.NAME, "account.phone").send_keys("03339507996")
# driver.find_element(By.NAME, "account.address1").send_keys("Gulraiz, lahore")
# driver.find_element(By.NAME, "account.address2").send_keys("Gulraiz, Rwp")
# driver.find_element(By.NAME, "account.city").send_keys("Multan")
# driver.find_element(By.NAME, "account.state").send_keys("Punjab")
# driver.find_element(By.NAME, "account.zip").send_keys("44000")
# driver.find_element(By.NAME, "account.country").send_keys("Pakistan")
# driver.find_element(By.NAME, "newAccount").click()
driver.maximize_window()
input("Press enter to continue...")




