import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def test_add():
    a=5
    b=2
    assert a+b==7

def test_sub():
    a=5
    b=1
    assert a-b!=4

def test_fruits():
    fruits = {"mango" , "apple" , "orange"}
    assert "apple" in fruits

def test_multiplication():
    num=6
    assert num>0
    assert num%2==0
    assert isinstance(num,int)

def test_length():
    items={1,2,3,4,5,6,7,8,9,10}
    assert len(items)==7