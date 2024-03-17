import allure
from selenium.webdriver.common.by import By
from page_objects.header_page import HeaderPage


class CartPage(HeaderPage):
    H1_PAGE = By.ID, 'shopping-cart'

    @allure.step
    def wait_for_product_in_cart(self):
        self.get_element(self.H1_PAGE)
