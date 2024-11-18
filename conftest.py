import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(2)
    return browser