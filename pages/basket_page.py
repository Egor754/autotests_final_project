from .base_page import BasePage
from .locators import BasePageLocators, BasketPageLocators


class BasketPage(BasePage):
    def should_be_cart_button(self):
        assert self.is_element_present(*BasePageLocators.CART_LINK), "Cart button is not presented"

    def should_not_be_item_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "The basket is not empty"

    def should_be_text_item_cart(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_NOT_ITEM_BASKET), \
            "Success text is presented, but should not be"
