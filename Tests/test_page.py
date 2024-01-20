import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_mac_price(browser, base_url):
    browser.get(base_url)
    browser.find_element(By.CSS_SELECTOR, 'img[alt="MacBook"]').click()
    assert WebDriverWait(browser, timeout=3).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, '.price-new'))).text == '$602.00'


def test_search_attr(browser, base_url):
    browser.get(base_url)
    WebDriverWait(browser, timeout=3).until(ec.visibility_of_element_located((By.NAME, 'search')))


def test_catalog_attr(browser, base_url):
    browser.get(base_url)
    browser.find_element(By.XPATH, "//a[text()='Software']").click()
    assert WebDriverWait(browser, timeout=3).until(
        ec.visibility_of_element_located((By.TAG_NAME, 'h2'))).text == 'Software'


def test_admin_page_attr(browser, base_url):
    browser.get(base_url + '/administration')
    WebDriverWait(browser, timeout=3).until(
        ec.visibility_of_element_located((By.ID, 'input-username')))
    browser.find_element(By.ID, 'input-password')


def test_reg_page_attr(browser, base_url):
    browser.get(base_url)
    browser.find_element(By.CSS_SELECTOR, 'li:nth-child(2) span').click()
    browser.find_element(By.CSS_SELECTOR, 'a[href*="register"]').click()
    browser.find_element(By.CSS_SELECTOR, '.text-end button').click()
    assert WebDriverWait(browser, timeout=3).until(ec.visibility_of_element_located(
        (By.ID, 'error-password'))).text == 'Password must be between 4 and 20 characters!'


def test_login(browser, base_url):
    browser.get(base_url + '/administration/')
    WebDriverWait(browser, timeout=3).until(
        ec.visibility_of_element_located((By.ID, 'input-username'))).send_keys('user')
    browser.find_element(By.ID, 'input-password').send_keys('bitnami')
    browser.find_element(By.CSS_SELECTOR, '.text-end button').click()
    WebDriverWait(browser, timeout=3).until(
        ec.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Total Orders ')]")))
    browser.find_element(By.CSS_SELECTOR, '.fa-sign-out').click()
    WebDriverWait(browser, timeout=3).until(ec.visibility_of_element_located((By.ID, 'input-username')))


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
