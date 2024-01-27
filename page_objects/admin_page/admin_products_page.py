from selenium.webdriver.common.by import By
from page_objects.admin_page.navigation_admin_menu_page import NavigationAdminMenuPage


class AdminProductsPage(NavigationAdminMenuPage):
    ADD_NEW_BUTTON = By.CSS_SELECTOR, '[title~=Add]'
    NEW_PRODUCT_SUB_MENU_GENERAL = By.LINK_TEXT, 'General'
    NEW_PRODUCT_NAME_INPUT = By.CSS_SELECTOR, '#input-name-1'
    NEW_PRODUCT_META_TAG_INPUT = By.CSS_SELECTOR, '#input-meta-title-1'
    NEW_PRODUCT_SUB_MENU_DATA = By.LINK_TEXT, 'Data'
    NEW_PRODUCT_MODEL_INPUT = By.CSS_SELECTOR, '#input-model'
    NEW_PRODUCT_SUB_MENU_SEO = By.LINK_TEXT, 'SEO'
    NEW_PRODUCT_KEYWORD_SEO_INPUT = By.CSS_SELECTOR, '#input-keyword-0-1'
    SAFE_PRODUCT_BUTTON = By.CSS_SELECTOR, '.float-end > button'
    PRODUCT_LIST = By.CSS_SELECTOR, 'tbody .form-check-input'
    DELETE_BUTTON = By.CSS_SELECTOR, '.btn-danger'

    def click_add_new_product_button(self):
        self.click(self.ADD_NEW_BUTTON)
        return self

    def click_to_general(self):
        self.click(self.NEW_PRODUCT_SUB_MENU_GENERAL)
        return self

    def input_product_name(self, product_name: str):
        self.input_value(self.NEW_PRODUCT_NAME_INPUT, product_name)
        return self

    def input_meta_tag(self, meta_tag_name: str):
        self.input_value(self.NEW_PRODUCT_META_TAG_INPUT, meta_tag_name)
        return self

    def click_to_data(self):
        self.click(self.NEW_PRODUCT_SUB_MENU_DATA)
        return self

    def input_model(self, model: str):
        self.input_value(self.NEW_PRODUCT_MODEL_INPUT, model)
        return self

    def click_to_seo(self):
        self.click(self.NEW_PRODUCT_SUB_MENU_SEO)
        return self

    def input_seo_keyword(self, seo_keyword: str):
        self.input_value(self.NEW_PRODUCT_KEYWORD_SEO_INPUT, seo_keyword)
        return self

    def click_save_product_button(self):
        self.click(self.SAFE_PRODUCT_BUTTON)
        return self

    def click_choice_products(self):
        self.get_elements(self.PRODUCT_LIST)[0].click()

    def click_delete_button(self):
        self.click(self.DELETE_BUTTON)

    def click_alert_accept(self):
        self.get_alert_accept()

