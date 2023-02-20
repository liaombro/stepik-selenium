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