from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        actual = self.browser.current_url
        
        assert 'login' in actual, "URL should contain 'login'"

    def should_be_login_form(self):
        locator = LoginPageLocators.LOGIN_FORM
        login_form = self.browser.find_element(*locator)
        
        assert login_form.is_displayed(), "Login form should be displayed"

    def should_be_register_form(self):
        locator = LoginPageLocators.REGISTER_FORM
        register_form = self.browser.find_element(*locator)
        
        assert register_form.is_displayed(), "Register form should be displayed"
        
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        password_field.send_keys(password)
        repeat_password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        repeat_password_field.send_keys(password)
        submit_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)
        submit_button.click()