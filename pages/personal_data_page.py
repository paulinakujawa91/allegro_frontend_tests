from locators.personal_data_page_locators import PersonalDataPageLocators
from pages.login_page import LoginPage
from selenium.webdriver.support.select import Select


class PersonalDataPageName(LoginPage):

    def __init__(self,driver):
        LoginPage.__init__(self,driver)

    def settings_page(self):
        self.driver.find_element(*PersonalDataPageLocators.arrow_head_button).click()
        self.driver.find_element(*PersonalDataPageLocators.my_account_button).click()

    def set_name_data_successfull(self, first_name, last_name):
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

class PersonalDataPageLogin(LoginPage):

    def __init__(self,driver):
        LoginPage.__init__(self,driver)

    def set_login_successfull(self,login):
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

class PersonalDataPageSpouseName(LoginPage):

    def __init__(self,driver):
        LoginPage.__init__(self,driver)

    def set_spouse_name_successfull(self,spouse_first_name, spouse_last_name):
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

class PersonalDataPageAddress(LoginPage):

    def __init__(self,driver):
        LoginPage.__init__(self,driver)

    def set_spouse_name_successfull(self, street, post_code, city, voivodeship, country):
        self.driver.find_element(*PersonalDataPageLocators.address_link).click()
        self.driver.find_element(*PersonalDataPageLocators.street_input).send_keys(street)
        self.driver.find_element(*PersonalDataPageLocators.post_code).send_keys(post_code)
        self.driver.find_element(*PersonalDataPageLocators.city).send_keys(city)
        self.driver.find_element(*PersonalDataPageLocators.voivodeship_s).select(voivodeship)
        self.driver.find_element(*PersonalDataPageLocators.country_s).select(country)
        self.driver.find_element(*PersonalDataPageLocators.save_address_button).click()

    def set_spouse_name_cancelled(self, street, post_code, city, voivodeship, country):
        self.driver.find_element(*PersonalDataPageLocators.address_link).click()
        self.driver.find_element(*PersonalDataPageLocators.street_input).send_keys(street)
        self.driver.find_element(*PersonalDataPageLocators.post_code).send_keys(post_code)
        self.driver.find_element(*PersonalDataPageLocators.city).send_keys(city)
        self.driver.find_element(*PersonalDataPageLocators.voivodeship_s).select(voivodeship)
        self.driver.find_element(*PersonalDataPageLocators.country_s).select(country)
        self.driver.find_element(*PersonalDataPageLocators.cancel_address_link).click()

    def is_saved_address(self, street, post_code, city, voivodeship, country):
        address_text = self.driver.find_element(*PersonalDataPageLocators.address).text()
        return address_text == street + ' ' + post_code + ' ' + city + ' ' + voivodeship + ' ' + country

    def is_cancelled_address(self, street, post_code, city, voivodeship, country):
        address_text = self.driver.find_element(*PersonalDataPageLocators.address).text()
        return address_text != street + ' ' + post_code + ' ' + city + ' ' + voivodeship + ' ' + country

