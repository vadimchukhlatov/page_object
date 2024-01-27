from selenium.webdriver.common.by import By
from page_objects.admin_page.navigation_admin_menu_page import NavigationAdminMenuPage


class AdminDashboardPage(NavigationAdminMenuPage):

    def find_total_order(self, page: str):
        self.click((By.XPATH, self._text_xpath(page)))
