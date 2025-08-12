import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from arraylist import fruits

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
@pytest.mark.skip(reason="this feature is not implemented")
def test_openbrowser():
    driver.get("https://www.w3schools.com/html/#gsc.tab=0")
    driver.implicitly_wait(5)
    driver.maximize_window()
def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def test_add():
    print(add(1, 2))
@pytest.mark.xfail(reason="this is known bug test is expected to fail")
def test_sub():
    print(sub(1, 2))
@pytest.mark.smoke()
def test_smoke():
    print("this is smoke test")
def test_fail():
    print("this is fail test")
@pytest.mark.regression()
def test_regression():
    print("this is regression test")
def test_login():
    print("this is login regression test is pass")

@pytest.mark.parametrize("fruits" , ["mango" , "orange" , "apple"])
def test_parametrization(fruits):
    print(f"testing with {fruits}")

