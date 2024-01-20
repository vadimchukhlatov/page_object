import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--base_url", default="http://192.168.0.113:8081")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    match browser_name:
        case "chrome":
            service = Service()
            driver = webdriver.Chrome(service=service)
        case "edge":
            driver = webdriver.Edge()
        case "firefox":
            driver = webdriver.Firefox()
        case _:
            raise Exception("Driver not supported")
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    yield driver
    driver.close()