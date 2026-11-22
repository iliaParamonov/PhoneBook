from Pages.registration_page import RegistrationPage
from Models.User import User
import uuid

def test_registration_success(driver):
    registration_page = RegistrationPage(driver)

    random_suffix = uuid.uuid4().hex[:8]
    user = User(
        f"PIO0201{random_suffix}@yandex.ry",
        "PIO0201@yandex.ru"
    )
    registration_page.open_registration_page()
    registration_page.fill_email_field(user.username)
    registration_page.fill_password_field(user.password)
    registration_page.click_registration_button()

    assert registration_page.is_sign_out_displayed() is True


def test_registration_with_wrong_email(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        "0_test.gmail.com",
        "Asd12345!"
    )
    registration_page.open_registration_page()
    registration_page.fill_email_field(user.username)
    registration_page.fill_password_field(user.password)
    registration_page.click_registration_button()

    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()


def test_registration_with_wrong_password(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        "1_test@gmail.com",
        "Asd1234"
    )
    registration_page.open_registration_page()
    registration_page.fill_email_field(user.username)
    registration_page.fill_password_field(user.password)
    registration_page.click_registration_button()

    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()

def test_registration_with_wrong_already_existed(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        "2_test@gmail.com",
        "Asdasdasd236!"
    )
    registration_page.open_registration_page()
    registration_page.fill_email_field(user.username)
    registration_page.fill_password_field(user.password)
    registration_page.click_registration_button()

    assert registration_page.get_alert_text() == "User already exist"
    registration_page.accept_alert()