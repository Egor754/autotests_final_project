import math
import time

from selenium.common.exceptions import NoAlertPresentException

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def go_to_product_page(self):
        product_button = self.browser.find_element(*ProductPageLocators.BUTTON_SELECTOR)
        product_button.click()

    def should_be_product_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_SELECTOR), "Product button is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_ADDING_PRODUCT), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_ADDING_PRODUCT), \
            "Success message is presented, but should not be"

    def comparison_title_and_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_TITLE_MESSAGE), "Product message is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_TITLE), "Product title is not presented"
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE_MESSAGE).text == self.browser.find_element(
            *ProductPageLocators.PRODUCT_TITLE).text, 'Message != title'

    def comparison_cart_and_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_PRODUCT), "Price product is not presented"
        assert self.is_element_present(*ProductPageLocators.PRICE_CART), "Price cart title is not presented"
        assert self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text in self.browser.find_element(
            *ProductPageLocators.PRICE_CART).text, 'Price cart != price product'

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
