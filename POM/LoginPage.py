from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    field_username = (By.CSS_SELECTOR, "input[name='username']")
    field_password = (By.CSS_SELECTOR, "input[name='password']")
    button_login = (By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")
    txt_message_invalid = (By.XPATH, "//div[@class='oxd-alert-content oxd-alert-content--error']/p")
    logo = (By.CSS_SELECTOR, "img[alt='company-branding']")

    def field_usernameMethod(self):
        return self.driver.find_element(*LoginPage.field_username)

    def field_passwordMethod(self):
        return self.driver.find_element(*LoginPage.field_password)

    def button_loginMethod(self):
        return self.driver.find_element(*LoginPage.button_login)

    def txt_message_invalidMethod(self):
        return self.driver.find_element(*LoginPage.txt_message_invalid)

    def logoMethod(self):
        return self.driver.find_element(*LoginPage.logo)