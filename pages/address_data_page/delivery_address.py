from locators.address_data_locators import AddressDataPageLocators
from pages.login_page import LoginPage


class DeliveryAddressPage(LoginPage):

    def __init__(self,driver):
        LoginPage.__init__(self,driver)

    def set_correct_delivery_address(self, delivery_first_name, delivery_last_name, delivery_company, delivery_phone_number, delivery_country, delivery_street, delivery_post_code, delivery_city):
        self.driver.find_element(*AddressDataPageLocators.set_delivery_address_link).click()
        self.driver.find_element(*AddressDataPageLocators.delivery_first_name_input).send_keys(delivery_first_name)
        self.driver.find_element(*AddressDataPageLocators.delivery_last_name_input).send_keys(delivery_last_name)
        self.driver.find_element(*AddressDataPageLocators.delivery_company_input).send_keys(delivery_company)
        self.driver.find_element(*AddressDataPageLocators.delivery_phone_number_input).send_keys(delivery_phone_number)
        self.driver.find_element(*AddressDataPageLocators.delivery_country_s).select(delivery_country)
        self.driver.find_element(*AddressDataPageLocators.delivery_street_input).send_keys(delivery_street)
        self.driver.find_element(*AddressDataPageLocators.delivery_post_code).send_keys(delivery_post_code)
        self.driver.find_element(*AddressDataPageLocators.delivery_city).send_keys(delivery_city)
        self.driver.find_element(*AddressDataPageLocators.save_delivery_address_button).click()

    def set_main_delivery_cancelled(self, delivery_first_name, delivery_last_name, delivery_company, delivery_phone_number, delivery_country, delivery_street, delivery_post_code, delivery_city):
        self.driver.find_element(*AddressDataPageLocators.set_delivery_address_link).click()
        self.driver.find_element(*AddressDataPageLocators.delivery_first_name_input).send_keys(delivery_first_name)
        self.driver.find_element(*AddressDataPageLocators.delivery_last_name_input).send_keys(delivery_last_name)
        self.driver.find_element(*AddressDataPageLocators.delivery_company_input).send_keys(delivery_company)
        self.driver.find_element(*AddressDataPageLocators.delivery_phone_number_input).send_keys(delivery_phone_number)
        self.driver.find_element(*AddressDataPageLocators.delivery_country_s).select(delivery_country)
        self.driver.find_element(*AddressDataPageLocators.delivery_street_input).send_keys(delivery_street)
        self.driver.find_element(*AddressDataPageLocators.delivery_post_code).send_keys(delivery_post_code)
        self.driver.find_element(*AddressDataPageLocators.delivery_city).send_keys(delivery_city)
        self.driver.find_element(*AddressDataPageLocators.cancel_delivery_address_link).click()

    def is_saved_correct_delivery_address(self, delivery_first_name, delivery_last_name, delivery_company, delivery_phone_number, delivery_street, delivery_post_code, delivery_city, delivery_country):
        delivery_address_text = self.driver.find_element(*AddressDataPageLocators.delivery_address).text()
        return delivery_address_text == delivery_first_name + ' ' + delivery_last_name + ' ' + delivery_company + ' ' + delivery_phone_number + ' ' + delivery_street + ' ' + delivery_post_code + ' ' + delivery_city + ' ' + ' ' + delivery_country

    def is_cancelled_delivery_address(self, delivery_first_name, delivery_last_name, delivery_company, delivery_phone_number, delivery_street, delivery_post_code, delivery_city, delivery_country):
        delivery_address_text = self.driver.find_element(*AddressDataPageLocators.delivery_address).text()
        return delivery_address_text != delivery_first_name + ' ' + delivery_last_name + ' ' + delivery_company + ' ' + delivery_phone_number + ' ' + delivery_street + ' ' + delivery_post_code + ' ' + delivery_city + ' ' + ' ' + delivery_country
