from pages.test_button import SimpleButtonPage
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait #для ожидания
from selenium.webdriver.support import expected_conditions as EC #для ожидания кондиции



def test_button1_exist(browser):
    simpele_page = SimpleButtonPage(browser)
    simpele_page.open()
    assert simpele_page.button_is_displaed()

# def test_button1_clicked(browser):
#     simpele_page = SimpleButtonPage(browser)
#     simpele_page.open()
#     simpele_page.click_button()
#     assert 'Submitted' == simpele_page.result_text()


def test_button1_clicked():
    browser = webdriver.Chrome()
    browser.get('https://www.qa-practice.com/elements/button/simple')
    browser.find_element(By.ID, 'submit-id-submit').click()
    assert 'Submitted' == browser.find_element(By.ID, 'result').text

def test_girls():
    browser = webdriver.Chrome()
    browser.implicitly_wait(2)
    browser.get('https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html')
    WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), 'Position'))# Для того, что бы подождать время загрузки объекта

    girls = browser.find_element(By.CLASS_NAME, 'product-image-photo')
    first_girl = girls
    assert ('https://magento.softwaretestingboard.com/pub/media/catalog/product/cache/7c4c1ed835fbbf2269f24539582c6d44/w/j/wj12-blue_main_1.jpg') == first_girl.get_attribute('src')
    sorter = browser.find_element(By.ID, 'sorter')
    select = Select(sorter)
    select.select_by_value('price')
    WebDriverWait(browser, 10).until(EC.staleness_of(first_girl))
    girls = browser.find_element(By.CLASS_NAME, 'product-image-photo')
    first_girl = girls
    assert ('https://magento.softwaretestingboard.com/pub/media/catalog/product/cache/7c4c1ed835fbbf2269f24539582c6d44/w/j/wj09-green_main_1.jpg') == first_girl.get_attribute('src')


