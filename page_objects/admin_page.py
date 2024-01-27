from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class AdminPage(BasePage):
    USERNAME_INPUT = By.ID, 'input-username'
    PASSWORD_INPUT = By.ID, 'input-password'
    LOGIN_BUTTON = By.CSS_SELECTOR, '.text-end button'
    LOGOUT_BUTTON = By.CSS_SELECTOR, '.fa-sign-out'
    ADMIN_URL_PAGE = '/administration'

    def find_password_input(self):
        self.get_element(self.PASSWORD_INPUT)

    def find_username_input(self):
        self.get_element(self.USERNAME_INPUT)

    def input_password(self, text: str):
        self.input_value(self.PASSWORD_INPUT, text)

    def input_username(self, text: str):
        self.input_value(self.USERNAME_INPUT, text)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def find_total_order(self, page: str):
        self.click((By.XPATH, self._text_xpath(page)))

    def click_logout_button(self):
        self.click(self.LOGOUT_BUTTON)
