from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demoqa.com/dynamic-properties")
driver.maximize_window()
input("Press enter to continue...")
# Create explicit wait object
wait=WebDriverWait(driver, 10)

# Wait for the 'Enable After 5 seconds' button to be clickable
enable_button=wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='enableAfter']")))
print("Enable After 5 seconds button is now clickable...")
enable_button.click()

# Wait for the 'Visible After 5 seconds' button to be visible
visible_button=wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='visibleAfter']")))
print("Visible After 5 seconds button is now visible...")
visible_button.click()

