from Pages.login_page import LoginPage

VALID_EMAIL = "xxkekcxx@gmail.com"
VALID_PASSWORD = "qwerty1@QWERTY."
INVALID_EMAIL = "test1234gmail.com"
INVALID_PASSWORD = "qwerty1234"

def test_valid_login_success(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.fill_email_field(VALID_EMAIL)
    login_page.fill_password_field(VALID_PASSWORD)
    login_page.click_login_button()
    assert login_page.is_sign_out_displayed()

def test_with_wrong_email(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.fill_email_field(INVALID_EMAIL)
    login_page.fill_password_field(VALID_PASSWORD)
    login_page.click_login_button()
    assert login_page.get_alert_text() == "Wrong email or password"
    login_page.accept_alert()

def test_with_valid_email_(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.fill_email_field(VALID_EMAIL)
    login_page.fill_password_field(INVALID_PASSWORD)
    login_page.click_login_button()
    assert login_page.get_alert_text() == "Wrong email or password"
    login_page.accept_alert()
def test_login_unregistered_user(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.fill_email_field("nicole_stttr@gmail.com")
    login_page.fill_password_field(VALID_PASSWORD)
    login_page.click_login_button()
    assert login_page.get_alert_text() == "Wrong email or password"
    login_page.accept_alert()