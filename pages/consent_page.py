from locators import locators


class ConsentPage:

    def __init__ (self,driver):
        self.driver = driver
        # consent page elements
        self.consent_button = locators.ConsentPageLocators.consent_button

    def open_page(self):
        self.driver.get('https://allegro.pl.allegrosandbox.pl/')

    def accept_consent(self):
        self.driver.find_element(*self.consent_button).click()