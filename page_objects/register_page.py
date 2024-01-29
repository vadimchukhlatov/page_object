from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class RegisterPage(BasePage):
    CONTINUE_BUTTON = By.CSS_SELECTOR, '.text-end button'
    PASSWORD_ERROR = By.ID, 'error-password'

    def click_continue_button(self):
        self.click(self.CONTINUE_BUTTON)

    def find_password_error_text(self):
        return self.get_element(self.PASSWORD_ERROR).text
