from locators.locators import LoginPageLocators


class LoginPage:

    def __init__(self,driver):
        self.driver = driver
        # login page elements
        self.login = LoginPageLocators.login
        self.password = LoginPageLocators.password
        self.login_button = LoginPageLocators.login_button
        self.login_span = LoginPageLocators.login_span
        self.error_message = LoginPageLocators.error_message

    def log_in(self,login,password):
        self.driver.find_element(*self.login).send_keys(login)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def get_login_span(self):
        return self.driver.find_element(*self.login_span).is_displayed()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text


