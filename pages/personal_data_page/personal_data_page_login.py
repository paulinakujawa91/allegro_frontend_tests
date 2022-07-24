from locators.personal_data_page_locators import PersonalDataPageLocators
from pages.login_page import LoginPage


class PersonalDataPageLogin(LoginPage):

    def __init__(self,driver):
        LoginPage.__init__(self,driver)

    def set_login_successful(self,login):
        self.driver.find_element(*PersonalDataPageLocators.set_login_link).click()
        self.driver.find_element(*PersonalDataPageLocators.login_input).send_keys(login)
        self.driver.find_element(*PersonalDataPageLocators.save_login_button).click()

    def set_login_cancelled(self,login):
        self.driver.find_element(*PersonalDataPageLocators.set_login_link).click()
        self.driver.find_element(*PersonalDataPageLocators.login_input).send_keys(login)
        self.driver.find_element(*PersonalDataPageLocators.cancel_login_link).click()

    def is_saved_login(self, login):
        login_name_text = self.driver.find_element(*PersonalDataPageLocators.login_name).text()
        return login_name_text == login

    def is_cancelled_login(self, login):
        login_name_text = self.driver.find_element(*PersonalDataPageLocators.login_name).text()
        return login_name_text != login
