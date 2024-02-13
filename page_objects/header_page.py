import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class HeaderPage(BasePage):
    MY_ACCOUNT_PREVIEW = By.CSS_SELECTOR, 'li:nth-child(2) span'
    REGISTER_BUTTON = By.CSS_SELECTOR, 'a[href*="register"]'
    SHOPPING_CART_BUTTON = By.CSS_SELECTOR, 'a[href*="cart"]'
    CURRENCY_LIST = By.CSS_SELECTOR, '#form-currency .d-none.d-md-inline'
    CURRENCY_NAME = By.CSS_SELECTOR, 'a[href*="{}"]'
    CURRENCY_ICON = By.CSS_SELECTOR, '#form-currency strong'

    @allure.step("Нажимаю на открытие под меню 'Моего аккаунта'")
    def click_my_account_preview(self):
        self.click(self.MY_ACCOUNT_PREVIEW)

    @allure.step("Нажимаю на кнопку перехода в раздел регистрации")
    def click_register_button(self):
        self.click(self.REGISTER_BUTTON)

    @allure.step("Нажимаю на кнопку перехода в корзину")
    def click_to_shopping_cart(self):
        self.click(self.SHOPPING_CART_BUTTON)

    @allure.step("Нажимаю на кнопку отображения всех валют")
    def click_to_currency_list(self):
        self.click(self.CURRENCY_LIST)

    @allure.step("Выбираю валюту {currency_name}")
    def click_choice_currency(self, currency_name: str):
        self.click((self.CURRENCY_NAME[0], self.CURRENCY_NAME[1].format(currency_name)))

    @allure.step("Ищу текст выбранной валюты")
    def get_currency_icon_text(self):
        return self.get_element(self.CURRENCY_ICON).text
