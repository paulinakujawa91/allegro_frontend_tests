from locators.locators import HomePageLocators


class HomePage:

    def __init__ (self,driver):
        self.driver = driver
        # home page elements
        self.arrow_head_button = HomePageLocators.arrow_head_button
        self.login_button = HomePageLocators.login_button

    def open_home_page(self):
        self.driver.find_element(*self.arrow_head_button).click()
        self.driver.find_element(*self.login_button).click()
