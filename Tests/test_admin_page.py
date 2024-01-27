import random
import time

from page_objects.admin_page.admin_login_page import AdminLoginPage
from page_objects.admin_page.admin_products_page import AdminProductsPage
from page_objects.alert_element import AlertSuccessElement

USERNAME = 'user'
PASSWORD = 'bitnami'


def test_admin_page_attr(browser, base_url):
    AdminLoginPage(browser).open_page(
        base_url + AdminLoginPage.ADMIN_URL_PAGE)  # Или лучше сделать внутри страницы метод с переходом?
    AdminLoginPage(browser).find_username_input()
    AdminLoginPage(browser).find_password_input()


def test_login(browser, base_url):
    AdminLoginPage(browser).open_page(base_url + AdminLoginPage.ADMIN_URL_PAGE)
    AdminLoginPage(browser).input_username(USERNAME).input_password(PASSWORD).click_login_button()
    AdminLoginPage(browser).login_check()
    AdminLoginPage(browser).click_logout_button()
    AdminLoginPage(browser).find_username_input()


def test_add_new_product(browser, base_url):
    AdminLoginPage(browser).open_page(base_url + AdminLoginPage.ADMIN_URL_PAGE)
    AdminLoginPage(browser).input_username(USERNAME).input_password(PASSWORD).click_login_button()
    AdminProductsPage(browser).click_product_page()
    AdminProductsPage(browser) \
        .click_add_new_product_button() \
        .click_to_general() \
        .input_product_name(str(random.randint(1, 1000))) \
        .input_meta_tag(str(random.randint(1, 1000))) \
        .click_to_data() \
        .input_model(str(random.randint(1, 1000))) \
        .click_to_seo() \
        .input_seo_keyword(str(random.randint(1, 1000))) \
        .click_save_product_button()
    AlertSuccessElement(browser)


def test_delete_product(browser, base_url):
    AdminLoginPage(browser).open_page(base_url + AdminLoginPage.ADMIN_URL_PAGE)
    AdminLoginPage(browser).input_username(USERNAME).input_password(PASSWORD).click_login_button()
    AdminProductsPage(browser).click_product_page()
    AdminProductsPage(browser).click_choice_products()
    AdminProductsPage(browser).click_delete_button()
    AdminProductsPage(browser).click_alert_accept()
    AlertSuccessElement(browser)
