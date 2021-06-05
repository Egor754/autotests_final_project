import time

import pytest

from .pages.basket_page import BasketPage
from .pages.locators import MainPageLocators
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage


#
# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

#
#
#
# def test_guest_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()
#
#
# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_product_button()
#     page.go_to_product_page()
#     page.should_dissapear_of_success_message()

@pytest.mark.xfail
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_button()
    page.go_to_product_page()
    page.solve_quiz_and_get_code()
    page.comparison_title_and_message()
    page.comparison_cart_and_product_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_button()
    page.go_to_product_page()
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = BasketPage(browser, link)
    page.open()
    page.should_be_cart_button()
    page.go_to_cart()
    cart_page = BasketPage(browser, browser.current_url)
    cart_page.should_not_be_item_cart()
    cart_page.should_be_text_item_cart()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        email = str(time.time()) + "@fakemail.org"
        password = 'iwqudijqwmodsamo'
        # user = LoginPage()
        # user.register_new_user(email, password)

    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_button()
        page.go_to_product_page()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser, link):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_button()
        page.go_to_product_page()
        page.solve_quiz_and_get_code()
        page.comparison_title_and_message()
        page.comparison_cart_and_product_price()
