from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    
    def go_to_login_page(self):
        login_link_locator = (By.CSS_SELECTOR, "#login_link")
        login_link = self.browser.find_element(*login_link_locator)
        login_link.click() 

    def should_be_login_link(self):
        login_link_locator = (By.CSS_SELECTOR, "#login_link")
        assert self.is_element_present(login_link_locator), "Login link is not presented"
