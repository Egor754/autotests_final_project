import time

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL_FORM_REGISTER)
        input_email.send_keys(email)
        input_pass = self.browser.find_element(*LoginPageLocators.PASS_FORM_REGISTER)
        input_pass.send_keys(password)
        input_pass2 = self.browser.find_element(*LoginPageLocators.PASS_FORM_REGISTER_2)
        input_pass2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        button.click()


    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert 'login' in self.browser.current_url, "There is no 'login'in the link"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"