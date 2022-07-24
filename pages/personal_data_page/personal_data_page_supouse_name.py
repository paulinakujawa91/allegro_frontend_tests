from locators.personal_data_page_locators import PersonalDataPageLocators
from pages.login_page import LoginPage


class PersonalDataPageSpouseName(LoginPage):

    def __init__(self,driver):
        LoginPage.__init__(self,driver)

    def set_spouse_name_successful(self,spouse_first_name, spouse_last_name):
        self.driver.find_element(*PersonalDataPageLocators.set_suposes_name_link).click()
        self.driver.find_element(*PersonalDataPageLocators.set_spouse_first_name).send_keys(spouse_first_name)
        self.driver.find_element(*PersonalDataPageLocators.set_spouse_last_name).send_keys(spouse_last_name)
        self.driver.find_element(*PersonalDataPageLocators.checkbox_consent).click()
        self.driver.find_element(*PersonalDataPageLocators.save_spouse_button).click()

    def set_spouse_name_cancelled(self,spouse_first_name, spouse_last_name):
        self.driver.find_element(*PersonalDataPageLocators.set_suposes_name_link).click()
        self.driver.find_element(*PersonalDataPageLocators.set_spouse_first_name).send_keys(spouse_first_name)
        self.driver.find_element(*PersonalDataPageLocators.set_spouse_last_name).send_keys(spouse_last_name)
        self.driver.find_element(*PersonalDataPageLocators.checkbox_consent).click()
        self.driver.find_element(*PersonalDataPageLocators.cancel_spouse_link).click()

    def is_saved_spouse_name(self, spouse_first_name, spouse_last_name):
        spouse_name_text = self.driver.find_element(*PersonalDataPageLocators.spouse_name).text()
        return spouse_name_text == spouse_first_name + ' ' + spouse_last_name

    def is_cancelled_spouse_name(self, spouse_first_name, spouse_last_name):
        spouse_name_text = self.driver.find_element(*PersonalDataPageLocators.spouse_name).text()
        return spouse_name_text != spouse_first_name + ' ' + spouse_last_name
