import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver


# For printing title of the page

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver
