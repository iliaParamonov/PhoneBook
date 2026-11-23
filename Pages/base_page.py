
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        def find_visible(driver):
            elements = driver.find_elements(*locator)

            for element in elements:
                if element.is_displayed():
                    return element

            return False

        return WebDriverWait(self.driver, 10).until(
            find_visible,
            message=f"Не найден элемент {locator}. URL: {self.driver.current_url}"
        )

    def click(self, locator):
        self.find(locator).click()

    def fill(self, locator, value):
        field = self.find(locator)
        field.clear()
        field.send_keys(value)

    def get_alert_text(self):
        alert = WebDriverWait(self.driver, 10).until(
            EC.alert_is_present()
        )
        return alert.text

    def accept_alert(self):
        alert = WebDriverWait(self.driver, 10).until(
            EC.alert_is_present()
        )
        alert.accept()
