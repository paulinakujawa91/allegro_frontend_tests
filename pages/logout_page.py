from locators.logout_page_locators import LogoutPageLocators
from pages.login_page import LoginPage


class LogoutPage(LoginPage):

    def __init__(self,driver):
        LoginPage.__init__(self,driver)

    def log_out(self):
        self.driver.find_element(*LogoutPageLocators.arrow_head_button).click()
        self.driver.find_element(*LogoutPageLocators.my_account_button).click()
        self.driver.find_element(*LogoutPageLocators.logout_link).click()

    def is_logout_successfull(self):
        return self.driver.find_element(*LogoutPageLocators.logout_view).is_displayed()