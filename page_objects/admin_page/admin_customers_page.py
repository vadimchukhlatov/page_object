from selenium.webdriver.common.by import By
from page_objects.admin_page.navigation_admin_menu_page import NavigationAdminMenuPage


class AdminCustomersPage(NavigationAdminMenuPage):
    ADD_NEW_BUTTON = By.CSS_SELECTOR, '[title~=Add]'
    NEW_PRODUCT_SUB_MENU_GENERAL = By.LINK_TEXT, 'General'
    NEW_FIRST_NAME_INPUT = By.CSS_SELECTOR, '#input-firstname'
    NEW_LAST_NAME_INPUT = By.CSS_SELECTOR, '#input-lastname'
    NEW_EMAIL_INPUT = By.CSS_SELECTOR, '#input-email'
    NEW_PASSWORD_INPUT = By.CSS_SELECTOR, '#input-password'
    NEW_PASSWORD_CONFIRM_INPUT = By.CSS_SELECTOR, '#input-confirm'
    SAFE_CUSTOMERS_BUTTON = By.CSS_SELECTOR, '.float-end > button'

    def click_to_add_new_customer(self):
        self.click(self.ADD_NEW_BUTTON)
        return self

    def click_to_general(self):
        self.click(self.NEW_PRODUCT_SUB_MENU_GENERAL)
        return self

    def input_first_name(self, customer_name: str):
        self.input_value(self.NEW_FIRST_NAME_INPUT, customer_name)
        return self

    def input_last_name(self, customer_last_name: str):
        self.input_value(self.NEW_LAST_NAME_INPUT, customer_last_name)
        return self

    def input_email(self, customer_email: str):
        self.input_value(self.NEW_EMAIL_INPUT, customer_email)
        return self

    def input_password(self, password: str):
        self.input_value(self.NEW_PASSWORD_INPUT, password)
        return self

    def input_password_confirm(self, confirm_password: str):
        self.input_value(self.NEW_PASSWORD_CONFIRM_INPUT, confirm_password)
        return self

    def click_save_customers_button(self):
        self.click(self.SAFE_CUSTOMERS_BUTTON)
        return self
