import random
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from page_objects.main_page import MainPage
from page_objects.catalog_page import CatalogPage
from page_objects.header_page import HeaderPage
from page_objects.register_page import RegisterPage



def test_mac_price(browser):
    assert MainPage(browser).find_product_price() == '$602.00'


def test_search_attr(browser):
    MainPage(browser).find_search_input()


def test_catalog_attr(browser):
    MainPage(browser).navbar_menu_click('Software')
    assert CatalogPage(browser).get_h2_catalog_text() == 'Software'


def test_reg_page_attr(browser):
    HeaderPage(browser).click_my_account_preview()
    HeaderPage(browser).click_register_button()
    RegisterPage(browser).click_continue_button()
    assert RegisterPage(browser).find_password_error_text() == 'Password must be between 4 and 20 characters!'


def test_add_to_cart(browser, base_url):
    browser.get(base_url)
    browser.execute_script('$("#carousel-banner-0").remove()')
    good = random.choice(WebDriverWait(browser, timeout=3).until(
        ec.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[formaction*="cart.add"]'))))
    ActionChains(browser) \
        .move_to_element(good) \
        .click() \
        .perform()
    WebDriverWait(browser, timeout=2).until(ec.visibility_of_element_located((By.CSS_SELECTOR, '.btn-close'))).click()
    browser.find_element(By.CSS_SELECTOR, 'a[href*="cart"]').click()
    WebDriverWait(browser, timeout=2).until(ec.visibility_of_element_located((By.ID, 'shopping-cart')))


def test_value_main(browser, base_url):
    browser.get(base_url)
    browser.execute_script('$("#carousel-banner-0").remove()')
    WebDriverWait(browser, timeout=2).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, '#form-currency .d-none.d-md-inline'))).click()
    WebDriverWait(browser, timeout=2).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, f'a[href*="{random.choice(["EUR", "GBP"])}"]'))).click()
    currency = WebDriverWait(browser, timeout=3).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, '#form-currency strong'))).text
    for price in WebDriverWait(browser, timeout=3).until(
            ec.visibility_of_all_elements_located((By.CSS_SELECTOR, '.price .price-new'))):
        print(price.text)
        assert currency in price.text


def test_value_catalog(browser, base_url):
    browser.get(base_url + '/en-gb/catalog/component/monitor')
    WebDriverWait(browser, timeout=2).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, '#form-currency .d-none.d-md-inline'))).click()
    WebDriverWait(browser, timeout=2).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, f'a[href*="{random.choice(["EUR", "GBP"])}"]'))).click()
    currency = WebDriverWait(browser, timeout=3).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, '#form-currency strong'))).text
    for price in WebDriverWait(browser, timeout=3).until(
            ec.visibility_of_all_elements_located((By.CSS_SELECTOR, '.price .price-new'))):
        assert currency in price.text
