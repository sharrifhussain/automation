import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

@pytest.fixture()
def hello_name():
    data = {"name":"shao"}
    yield data
    print("tearing down: using this down in upcoming functions")

@pytest.fixture()
def hello_name1():
    data = {"name":"ali"}
    yield data
    print("tearing down: using this down in upcoming functions")

def test_test1(hello_name):
    print("test1 running with:", hello_name ["name"])

def test_test2(hello_name1):
    print("test2 running with:", hello_name1 ["name"])
