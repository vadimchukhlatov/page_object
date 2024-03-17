import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class NavigationAdminMenuPage(BasePage):
    LOGOUT_BUTTON = By.CSS_SELECTOR, '.fa-sign-out'
    USER_PROFILE = By.ID, 'nav-profile'
    MENU_CATALOG = By.CSS_SELECTOR, '#menu-catalog'
    MENU_CUSTOMERS = By.CSS_SELECTOR, '#menu-customer'
    MENU_PRODUCTS = By.LINK_TEXT, 'Products'
    SUB_MENU_CUSTOMERS = By.CSS_SELECTOR, '#menu a[href*="customer&user_token"]'

    @allure.step("Проверка логина в админку")
    def login_check(self):
        self.get_element(self.USER_PROFILE)

    @allure.step("Нажимаю на кнопку выхода из учетной записи")
    def click_logout_button(self):
        self.click(self.LOGOUT_BUTTON)

    @allure.step("Нажимаю на страницу продуктов")
    def click_product_page(self):
        self.click(self.MENU_CATALOG)
        self.click(self.MENU_PRODUCTS)

    @allure.step("Нажимаю на страницу пользователей")
    def click_to_customers_page(self):
        self.click(self.MENU_CUSTOMERS)
        self.click(self.SUB_MENU_CUSTOMERS)
