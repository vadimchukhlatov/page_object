from page_objects.admin_page import AdminPage


def test_admin_page_attr(browser, base_url):
    AdminPage(browser).open_page(base_url + AdminPage.ADMIN_URL_PAGE)  # Или лучше сделать внутри страницы метод с переходом?
    AdminPage(browser).find_username_input()
    AdminPage(browser).find_password_input()


def test_login(browser, base_url):
    AdminPage(browser).open_page(base_url + AdminPage.ADMIN_URL_PAGE)
    AdminPage(browser).input_username('user')
    AdminPage(browser).input_password('bitnami')
    AdminPage(browser).click_login_button()
    AdminPage(browser).find_total_order('Total Orders ')
    AdminPage(browser).click_logout_button()
    AdminPage(browser).find_username_input()
