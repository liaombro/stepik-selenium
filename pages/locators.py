from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "a[href*='basket']:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class MainPageLocators(BasePageLocators):
    URL = 'http://selenium1py.pythonanywhere.com/'
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators(BasePageLocators):
    URL = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD1 = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.ID, "id_registration-password2")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")
class ProductPageLocators(BasePageLocators):
    URL = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.XPATH, "//*[contains(@class, 'alert-success')][1]//strong")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    CART_TOTAL_MESSAGE = (By.CSS_SELECTOR, ".alert-info strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR,  ".product_main .price_color")
    
class BasketPageLocators(BasePageLocators):
    URL = 'http://selenium1py.pythonanywhere.com/ru/basket/'
    FIRST_ITEM = (By.CSS_SELECTOR, ".basket-items > .row:nth-child(1)")
    CART_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")