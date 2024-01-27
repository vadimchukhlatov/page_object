from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class NavigationAdminMenuPage(BasePage):
    LOGOUT_BUTTON = By.CSS_SELECTOR, '.fa-sign-out'

    def click_logout_button(self):
        self.click(self.LOGOUT_BUTTON)
