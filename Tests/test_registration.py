import time

from Pages.registration_page import RegistrationPage

VALID_PASSWORD = "PIO0201@yandex.ru"
EXISTING_EMAIL = "PIO0201@yandex.ru"
INVALID_EMAIL = "test4321@yandex.ru"
INVALID_PASSWORD = "test"


def unique_email():
    # новый email при каждом запуске, чтобы тест не падал из-за дубля
    return f"nicole_{int(time.time())}@gmail.com"


def test_valid_registration_success(driver):
    page = RegistrationPage(driver)
    page.open_registration_page()
    page.fill_email_field(unique_email())
    page.fill_password_field(VALID_PASSWORD)
    page.click_registration_button()
    assert page.is_sign_out_displayed()


def test_registration_with_existing_email(driver):
    page = RegistrationPage(driver)
    page.open_registration_page()
    page.fill_email_field(EXISTING_EMAIL)
    page.fill_password_field(VALID_PASSWORD)
    page.click_registration_button()
    alert_text = page.get_alert_text()
    print(repr(alert_text))
    assert alert_text
    page.accept_alert()


def test_registration_with_invalid_email(driver):
    page = RegistrationPage(driver)
    page.open_registration_page()
    page.fill_email_field(INVALID_EMAIL)
    page.fill_password_field(VALID_PASSWORD)
    page.click_registration_button()
    alert_text = page.get_alert_text()
    assert "Wrong email or password format" in alert_text
    assert "Email must contains one @" in alert_text
    page.accept_alert()


def test_registration_with_invalid_password(driver):
    page = RegistrationPage(driver)
    page.open_registration_page()
    page.fill_email_field(unique_email())
    page.fill_password_field(INVALID_PASSWORD)
    page.click_registration_button()
    alert_text = page.get_alert_text()
    assert "Wrong email or password format" in alert_text
    assert "at least one special symbol" in alert_text
    page.accept_alert()


def test_registration_with_empty_fields(driver):
    page = RegistrationPage(driver)
    page.open_registration_page()
    page.click_registration_button()
    alert_text = page.get_alert_text()
    assert "Wrong email or password format" in alert_text
    assert "Email must contains one @" in alert_text
    assert "at least one uppercase letter" in alert_text
    assert "at least one lowercase letter" in alert_text
    assert "at least one digit" in alert_text
    assert "at least one special symbol" in alert_text
    page.accept_alert()