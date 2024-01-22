from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class MainPage(BasePage):
    ADD_TO_CART_BUTTON = By.CSS_SELECTOR, '#button_cart'
    PRICE_NEW_PRODUCTS = By.CSS_SELECTOR, '.price-new'
    SEARCH_INPUT = By.NAME, 'search'

    def add_to_cart(self):
        self.get_element(self.ADD_TO_CART_BUTTON).click()

    def find_product_price(self):
        return self.get_elements(self.PRICE_NEW_PRODUCTS)[0].text

    def find_search_input(self):
        self.get_element(self.SEARCH_INPUT)

    def navbar_menu_click(self, page: str):
        self.click((By.XPATH, self._text_xpath(page)))
