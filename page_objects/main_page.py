from selenium.webdriver.common.by import By
from page_objects.header_page import HeaderPage


class MainPage(HeaderPage):
    ADD_TO_CART_BUTTON = By.CSS_SELECTOR, 'button[formaction*="cart.add"]'
    PRICE_NEW_PRODUCTS = By.CSS_SELECTOR, '.price-new'
    SEARCH_INPUT = By.NAME, 'search'

    def add_to_cart(self, index=0):
        if index == 0:
            self.click(self.ADD_TO_CART_BUTTON)
        else:
            self.get_elements(self.ADD_TO_CART_BUTTON)[index].click()

    def find_products_price(self, index=0):
        if index == 0:
            return self.get_elements(self.PRICE_NEW_PRODUCTS)[index].text
        else:
            return self.get_elements(self.PRICE_NEW_PRODUCTS)

    def find_search_input(self):
        self.get_element(self.SEARCH_INPUT)

    def navbar_menu_click(self, page: str):
        self.click((By.XPATH, self._text_xpath(page)))
