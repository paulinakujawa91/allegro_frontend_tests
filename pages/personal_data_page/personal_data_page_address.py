from locators.personal_data_page_locators import PersonalDataPageLocators
from pages.login_page import LoginPage


class PersonalDataPageAddress(LoginPage):

    def __init__(self,driver):
        LoginPage.__init__(self,driver)

    def set_address_successful(self, street, post_code, city, voivodeship, country):
        self.driver.find_element(*PersonalDataPageLocators.address_link).click()
        self.driver.find_element(*PersonalDataPageLocators.street_input).send_keys(street)
        self.driver.find_element(*PersonalDataPageLocators.post_code).send_keys(post_code)
        self.driver.find_element(*PersonalDataPageLocators.city).send_keys(city)
        self.driver.find_element(*PersonalDataPageLocators.voivodeship_s).select(voivodeship)
        self.driver.find_element(*PersonalDataPageLocators.country_s).select(country)
        self.driver.find_element(*PersonalDataPageLocators.save_address_button).click()

    def set_address_cancelled(self, street, post_code, city, voivodeship, country):
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

