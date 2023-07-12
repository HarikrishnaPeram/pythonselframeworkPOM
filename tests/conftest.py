import pytest
from selenium import webdriver
import pytest

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait



def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request): #request is the instance for the fixture
    #request.config.getOption("--browser_name")
    driver = webdriver.Chrome(executable_path="C:/Users/selenium/work space/chromedriver.exe")
    #service_obj = Service("C:/Users/selenium/work space/chromedriver.exe")
    #driver = webdriver.Chrome(service=service_obj)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
