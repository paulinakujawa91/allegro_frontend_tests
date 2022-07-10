from selenium.webdriver.common.by import By


class LogoutPageLocators:

    arrow_head_button = (By.XPATH, "//div[@data-dropdown-id='user_dropdown']/button")
    logout_link = (By.XPATH,'//a[@data-analytics-click-value="logout-button"]')
    my_account_button = (By.XPATH, '//a[@data-analytics-interaction-value="Konto"]')
    logout_view = (By.XPATH, "//span[contains(.,'Moje Allegro')]")
