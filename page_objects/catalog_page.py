from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class CatalogPage(BasePage):
    CATALOG_H2 = By.TAG_NAME, 'h2'

    def get_h2_catalog_text(self):
        return self.get_element(self.CATALOG_H2).text
