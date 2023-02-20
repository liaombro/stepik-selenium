from .base_page import BasePage
from .locators import ProductPageLocators

import math 
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):
    
    
    def add_product_to_cart(self):
        locator = ProductPageLocators.ADD_TO_CART_BUTTON
        add_to_cart_button = self.browser.find_element(*locator)
        add_to_cart_button.click()
        self.solve_quiz_and_get_code()

    def should_be_success_message(self):
        locator_message = ProductPageLocators.SUCCESS_MESSAGE
        product_title = self.get_product_title()

        success_message = self.browser.find_element(*locator_message)
        
        assert product_title in success_message.text, "Success message should be displayed after 'Add to Cart' button is pressed"        
    
    def get_product_title(self):
        locator_product_title = ProductPageLocators.PRODUCT_TITLE
        product_title = self.browser.find_element(*locator_product_title)
        return product_title.text
    
    def get_product_price(self):
        locator_price = ProductPageLocators.PRODUCT_PRICE
        price = self.browser.find_element(*locator_price)
        return price.text
    
    def cart_total_should_be_equal_to_product_price(self):
        locator_cart_total = ProductPageLocators.CART_TOTAL_MESSAGE
        price = self.get_product_price()
        
        cart_total = self.browser.find_element(*locator_cart_total)
        
        assert price == cart_total.text, f"Cart total should be equal to price of the product"
        
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
