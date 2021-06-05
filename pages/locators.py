from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    MESSAGE_REGISTER = (By.CSS_SELECTOR, ".alert-success .wicon")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FORM_REGISTER = (By.CSS_SELECTOR, "#id_registration-email")
    PASS_FORM_REGISTER = (By.CSS_SELECTOR, "#id_registration-password1")
    PASS_FORM_REGISTER_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTER = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators():
    BUTTON_SELECTOR = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_TITLE_MESSAGE = (By.CSS_SELECTOR, '.alert-noicon:nth-child(1) strong')
    PRODUCT_TITLE = (By.CSS_SELECTOR, '.product_main h1')
    PRICE_CART = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.product_main .price_color')
    SUCCESS_MESSAGE_ADDING_PRODUCT = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')


class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, 'basket-items')
    TEXT_NOT_ITEM_BASKET = (By.XPATH, '//*[@id="content_inner"]/p/a')