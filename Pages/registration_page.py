from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Pages.base_page import BasePage


class RegistrationPage(BasePage):
    REGISTRATION_LINK = (By.CSS_SELECTOR, "a[href='/login']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[name='registration']")
    SIGN_OUT_BUTTON = (By.XPATH, "//*[text()='Sign Out']")

    def open_registration_page(self):
        self.click(self.REGISTRATION_LINK)

    def fill_email_field(self, email):
        self.fill(self.EMAIL_INPUT, email)

    def fill_password_field(self, password):
        self.fill(self.PASSWORD_INPUT, password)

    def click_registration_button(self):
        self.click(self.REGISTRATION_BUTTON)

    def is_sign_out_displayed(self):
        try:
            WebDriverWait(self.driver, timeout = 10).until(
                expected_conditions.visibility_of_element_located(self.SIGN_OUT_BUTTON)
            )
            return True
        except TimeoutException:
            return False