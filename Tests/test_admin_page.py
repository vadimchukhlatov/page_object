from page_objects.admin_page.admin_login_page import AdminLoginPage
from page_objects.admin_page.admin_dashboard_page import AdminDashboardPage


def test_admin_page_attr(browser, base_url):
    AdminLoginPage(browser).open_page(base_url + AdminLoginPage.ADMIN_URL_PAGE)  # Или лучше сделать внутри страницы метод с переходом?
    AdminLoginPage(browser).find_username_input()
    AdminLoginPage(browser).find_password_input()


def test_login(browser, base_url):
    AdminLoginPage(browser).open_page(base_url + AdminLoginPage.ADMIN_URL_PAGE)
    AdminLoginPage(browser).input_username('user').input_password('bitnami').click_login_button()
    AdminDashboardPage(browser).find_total_order('Total Orders ')
    AdminDashboardPage(browser).click_logout_button()
    AdminLoginPage(browser).find_username_input()
