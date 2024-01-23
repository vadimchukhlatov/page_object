from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class HeaderPage(BasePage):
    MY_ACCOUNT_PREVIEW = By.CSS_SELECTOR, 'li:nth-child(2) span'
    REGISTER_BUTTON = By.CSS_SELECTOR, 'a[href*="register"]'

    def click_my_account_preview(self):
        self.click(self.MY_ACCOUNT_PREVIEW)

    def click_register_button(self):
        self.click(self.REGISTER_BUTTON)

