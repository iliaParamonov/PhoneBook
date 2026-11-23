
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage:

    URL = "https://telranedu.pages.dev/login"

    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SIGN_OUT_BUTTON = (By.XPATH, "//*[normalize-space()='Sign Out']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_login_page(self):
        self.driver.get(self.URL)

    def fill_email_field(self, email):
        field = self.wait.until(
            EC.visibility_of_element_located(self.EMAIL_INPUT)
        )
        field.clear()
        field.send_keys(email)

    def fill_password_field(self, password):
        field = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        field.clear()
        field.send_keys(password)

    def click_login_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def is_sign_out_displayed(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.SIGN_OUT_BUTTON)
            )
            return True
        except TimeoutException:
            return False

    def get_alert_text(self):
        alert = self.wait.until(
            EC.alert_is_present()
        )
        return alert.text

    def accept_alert(self):
        alert = self.wait.until(
            EC.alert_is_present()
        )
        alert.accept()
