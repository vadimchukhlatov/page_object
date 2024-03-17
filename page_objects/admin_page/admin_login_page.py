import allure
from selenium.webdriver.common.by import By
from page_objects.admin_page.navigation_admin_menu_page import NavigationAdminMenuPage


class AdminLoginPage(NavigationAdminMenuPage):
    USERNAME_INPUT = By.ID, 'input-username'
    PASSWORD_INPUT = By.ID, 'input-password'
    LOGIN_BUTTON = By.CSS_SELECTOR, '.text-end button'
    ADMIN_URL_PAGE = '/administration'

    @allure.step("Ищу поле ввода пароля")
    def find_password_input(self):
        self.get_element(self.PASSWORD_INPUT)

    @allure.step("Ищу поле ввода имени")
    def find_username_input(self):
        self.get_element(self.USERNAME_INPUT)

    @allure.step("Ввожу текст в поле пароля - {text}")
    def input_password(self, text: str):
        self.input_value(self.PASSWORD_INPUT, text)
        return self

    @allure.step("Ввожу текст в поле имени - {text}")
    def input_username(self, text: str):
        self.input_value(self.USERNAME_INPUT, text)
        return self

    @allure.step("Нажимаю кнопку логина")
    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)
        return self
