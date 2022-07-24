from selenium.webdriver.common.by import By


class LoginPageLocators:
    email = (By.ID, 'login')
    password = (By.ID, 'password')
    login_button = (By.XPATH, "//button[contains(., 'Zaloguj się')]")
    login_span = (By.XPATH, "//div[contains(., 'Pomóż nam chronić Twoje konto')]")
    error_message = (By.XPATH, "//div[contains(., 'Login, e-mail lub hasło są nieprawidłowe')]")
    skip_button = (By.ID, "skip-confirmation-btn")