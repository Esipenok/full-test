import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options # это для безголового режима


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(2)
    return browser