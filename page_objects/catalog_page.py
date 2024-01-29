from selenium.webdriver.common.by import By
from page_objects.header_page import HeaderPage


class CatalogPage(HeaderPage):
    CATALOG_H2 = By.TAG_NAME, 'h2'
    CATALOG_URL_PAGE = '/catalog/component/monitor'
    PRICE_NEW_PRODUCTS = By.CSS_SELECTOR, '.price-new'

    def get_h2_catalog_text(self):
        return self.get_element(self.CATALOG_H2).text

    def find_products_price(self, index=0):
        if index == 0:
            return self.get_elements(self.PRICE_NEW_PRODUCTS)[index].text
        else:
            return self.get_elements(self.PRICE_NEW_PRODUCTS)

