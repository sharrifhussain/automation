import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

@pytest.fixture(params=[2,4,6])
def sample_data(request):
    return request.param

@pytest.fixture(params=[5,8,7])
def test_data(request):
    return request.param

def test_subtract(test_data):
    result = test_data-2
    print(f" result is {result}")

def test_multiplication(sample_data):
    result =sample_data*2
    print(f" result is {result}")
