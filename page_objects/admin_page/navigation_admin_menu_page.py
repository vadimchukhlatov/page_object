from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class NavigationAdminMenuPage(BasePage):
    LOGOUT_BUTTON = By.CSS_SELECTOR, '.fa-sign-out'
    USER_PROFILE = By.ID, 'nav-profile'
    MENU_CATALOG = By.CSS_SELECTOR, '#menu-catalog'
    MENU_PRODUCTS = By.LINK_TEXT, 'Products'

    def login_check(self):
        self.get_element(self.USER_PROFILE)

    def click_logout_button(self):
        self.click(self.LOGOUT_BUTTON)

    def click_product_page(self):
        self.click(self.MENU_CATALOG)
        self.click(self.MENU_PRODUCTS)
