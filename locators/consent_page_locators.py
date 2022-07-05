from selenium.webdriver.common.by import By


class ConsentPageLocators:
    consent_button = (By.XPATH, "//button[contains(., 'Ok, zgadzam się')]")