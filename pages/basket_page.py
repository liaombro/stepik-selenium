from pages.base_page import BasePage
from pages.locators import BasePageLocators, BasketPageLocators

class BasketPage(BasePage):

    def should_be_empty_cart(self):
        self.should_be_no_products_in_cart()
        self.should_be_cart_is_empty_message()
    
    def should_be_no_products_in_cart(self):
        item_locator = BasketPageLocators.FIRST_ITEM
        
        assert self.is_not_element_present(item_locator) == True, "No items should be displayed"
    
    def should_be_cart_is_empty_message(self):
        cart_is_empty_locator = BasketPageLocators.CART_IS_EMPTY_MESSAGE
                
        assert self.is_element_visible(cart_is_empty_locator) == True, "'Cart is empty' message should be displayed"