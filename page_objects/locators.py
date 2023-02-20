from selenium.webdriver.common.by import By

class MainPageLocators:
    URL = 'http://selenium1py.pythonanywhere.com/'
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators:
    URL = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")