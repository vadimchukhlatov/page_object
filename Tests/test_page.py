from page_objects.main_page import MainPage
from page_objects.catalog_page import CatalogPage
from page_objects.alert_element import AlertSuccessElement
from page_objects.register_page import RegisterPage
from page_objects.cart_page import CartPage


def test_mac_price(browser, base_url):
    MainPage(browser).open_page(base_url)
    assert MainPage(browser).find_products_price() == '$602.00'


def test_search_attr(browser, base_url):
    MainPage(browser).open_page(base_url)
    MainPage(browser).find_search_input()


def test_catalog_attr(browser, base_url):
    MainPage(browser).open_page(base_url)
    MainPage(browser).navbar_menu_click('Software')
    assert CatalogPage(browser).get_h2_catalog_text() == 'Software'


def test_reg_page_attr(browser, base_url):
    MainPage(browser).open_page(base_url)  # На сколько правильно каждый раз инициализировать класс, вместо присвоения в этой строке в переменную и уже дальнейшее использование
    MainPage(browser).click_my_account_preview()
    MainPage(browser).click_register_button()
    RegisterPage(browser).click_continue_button()
    assert RegisterPage(browser).find_password_error_text() == 'Password must be between 4 and 20 characters!'


def test_add_to_cart(browser, base_url):
    MainPage(browser).open_page(base_url)
    browser.execute_script('$("#carousel-banner-0").remove()')  # Без удаления карусели выскакивает ошибка при клике Message: move target out of bounds
    MainPage(browser).add_to_cart()
    AlertSuccessElement(browser).shopping_cart.click()
    CartPage(browser).wait_for_product_in_cart()


def test_main_currency(browser, base_url):
    MainPage(browser).open_page(base_url)
    browser.execute_script('$("#carousel-banner-0").remove()')
    MainPage(browser).click_to_currency_list()
    MainPage(browser).click_choice_currency('EUR')
    currency = MainPage(browser).get_currency_icon_text()
    for price in MainPage(browser).find_products_price(index=1):
        assert currency in price.text


def test_catalog_currency(browser, base_url):
    CatalogPage(browser).open_page(base_url + CatalogPage.CATALOG_URL_PAGE)
    CatalogPage(browser).click_to_currency_list()
    CatalogPage(browser).click_choice_currency('GBP')
    currency = CatalogPage(browser).get_currency_icon_text()
    for price in CatalogPage(browser).find_products_price(index=1):
        assert currency in price.text
