from locators.consent_page_locators import ConsentPageLocators
from locators.login_page_locators import LoginPageLocators


class LoginPage:
    test_url = "https://allegro.pl.allegrosandbox.pl/logowanie"

    def __init__(self,driver):
        self.driver = driver
        self.driver.get(self.test_url)
        self.driver.find_element(*ConsentPageLocators.consent_button).click()

    def log_in(self,email,password):
        self.driver.find_element(*LoginPageLocators.login).send_keys(email)
        self.driver.find_element(*LoginPageLocators.password).send_keys(password)
        self.driver.find_element(*LoginPageLocators.login_button).click()

    def is_login_successfuly(self):
        return self.driver.find_element(*LoginPageLocators.login_span).is_displayed()

    def get_error_message(self):
        return self.driver.find_element(*LoginPageLocators.error_message).text

    def skip_2fa(self):
        self.driver.find_element(*LoginPageLocators.skip_button).click()


