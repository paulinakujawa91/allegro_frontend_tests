from locators.address_data_locators import AddressDataPageLocators
from pages.login_page import LoginPage


class MainAddressPage(LoginPage):

    def __init__(self,driver):
        LoginPage.__init__(self,driver)

    def set_correct_main_address(self, street, post_code, city, voivodeship, country):
        self.driver.find_element(*AddressDataPageLocators.set_address_link).click()
        self.driver.find_element(*AddressDataPageLocators.street_input).send_keys(street)
        self.driver.find_element(*AddressDataPageLocators.post_code).send_keys(post_code)
        self.driver.find_element(*AddressDataPageLocators.city).send_keys(city)
        self.driver.find_element(*AddressDataPageLocators.voivodeship_s).select(voivodeship)
        self.driver.find_element(*AddressDataPageLocators.country_s).select(country)
        self.driver.find_element(*AddressDataPageLocators.save_address_button).click()

    def set_main_address_cancelled(self, street, post_code, city, voivodeship, country):
        self.driver.find_element(*AddressDataPageLocators.set_address_link).click()
        self.driver.find_element(*AddressDataPageLocators.street_input).send_keys(street)
        self.driver.find_element(*AddressDataPageLocators.post_code).send_keys(post_code)
        self.driver.find_element(*AddressDataPageLocators.city).send_keys(city)
        self.driver.find_element(*AddressDataPageLocators.voivodeship_s).select(voivodeship)
        self.driver.find_element(*AddressDataPageLocators.country_s).select(country)
        self.driver.find_element(*AddressDataPageLocators.cancel_address_link).click()

    def is_saved_correct_main_address(self, street, post_code, city, voivodeship, country):
        main_address_text = self.driver.find_element(*AddressDataPageLocators.main_address).text()
        return main_address_text == street + ' ' + post_code + ' ' + city + ' ' + voivodeship + ' ' + country

    def is_cancelled_main_address(self, street, post_code, city, voivodeship, country):
        main_address_text = self.driver.find_element(*AddressDataPageLocators.main_address).text()
        return main_address_text != street + ' ' + post_code + ' ' + city + ' ' + voivodeship + ' ' + country
