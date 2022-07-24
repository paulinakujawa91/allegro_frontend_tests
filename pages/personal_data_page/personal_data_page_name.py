from locators.personal_data_page_locators import PersonalDataPageLocators
from pages.login_page import LoginPage


class PersonalDataPageName(LoginPage):

    def __init__(self,driver):
        LoginPage.__init__(self,driver)

    def settings_page(self):
        self.driver.find_element(*PersonalDataPageLocators.arrow_head_button).click()
        self.driver.find_element(*PersonalDataPageLocators.my_account_button).click()

    def set_name_data_successful(self, first_name, last_name):
        self.driver.find_element(*PersonalDataPageLocators.set_name_link).click()
        self.driver.find_element(*PersonalDataPageLocators.first_name).send_keys(first_name)
        self.driver.find_element(*PersonalDataPageLocators.last_name).send_keys(last_name)
        self.driver.find_element(*PersonalDataPageLocators.save_name_button).click()

    def set_name_data_cancelled(self, first_name, last_name):
        self.driver.find_element(*PersonalDataPageLocators.set_name_link).click()
        self.driver.find_element(*PersonalDataPageLocators.first_name).send_keys(first_name)
        self.driver.find_element(*PersonalDataPageLocators.last_name).send_keys(last_name)
        self.driver.find_element(*PersonalDataPageLocators.cancel_name_link).click()

    def is_saved_name_data(self, first_name, last_name):
        p_name_text = self.driver.find_element(*PersonalDataPageLocators.p_name).text()
        return p_name_text == first_name + ' ' + last_name

    def is_cancelled_name_data(self, first_name, last_name):
        p_name_text = self.driver.find_element(*PersonalDataPageLocators.p_name).text()
        return p_name_text != first_name + ' ' + last_name
