
import pytest
from selenium import webdriver

from Pages.add_contact_page import ContactPage
from Pages.contact_page import ContactsPage
from Pages.login_page import LoginPage
from Tests.test_login import VALID_EMAIL, VALID_PASSWORD


@pytest.fixture

def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    driver.get("https://telranedu.pages.dev")

    yield driver

    driver.quit()

@pytest.fixture
def authenticated_client(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.fill_email_field(VALID_EMAIL)
    login_page.fill_password_field(VALID_PASSWORD)
    login_page.click_login_button()

    return driver

@pytest.fixture
def ensure_min_contacts(authenticated_client):
    contacts_page = ContactsPage(authenticated_client)
    contact_page = ContactPage(authenticated_client)

    contacts_page = ContactPage(authenticated_client)
    while contacts_page.get_contact_cards_number() < 1:
        contact_page.create_contact_steps(create_contact())
        contacts_page.open_contacts_list()
    return authenticated_client
