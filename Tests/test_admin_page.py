from page_objects.admin_page import AdminPage


def test_admin_page_attr(browser):
    AdminPage(browser).find_username_input()
    AdminPage(browser).find_password_input()


def test_login(browser):
    AdminPage(browser).input_username('user')
    AdminPage(browser).input_password('bitnami')
    AdminPage(browser).click_login_button()
    AdminPage(browser).find_total_order('Total Orders ')
    AdminPage(browser).click_logout_button()
    AdminPage(browser).find_username_input()
