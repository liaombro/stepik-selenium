from selenium.webdriver.common.by import By

class MainPageLocators:
    URL = 'http://selenium1py.pythonanywhere.com/'
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators:
    URL = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    
class ProductPageLocators:
    URL = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.XPATH, "//*[contains(@class, 'alert-success')][1]//strong")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    CART_TOTAL_MESSAGE = (By.CSS_SELECTOR, ".alert-info strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR,  ".product_main .price_color")