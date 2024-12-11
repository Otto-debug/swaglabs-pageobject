from selenium.webdriver.common.by import By

# Тут я описываю селекторы, по которым буду искать объекты на страницах

class LoginPage:
    USERNAME = (By.CSS_SELECTOR, '#user-name')
    PASSWORD = (By.CSS_SELECTOR, '#password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login-button')
    ERROR_MESSAGE = (By.CLASS_NAME, 'error-message-container')

class InventPage:
    INVENTORY_LIST = (By.CLASS_NAME, 'inventory_list')
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_ADD_BUTTON = (By.CLASS_NAME, 'btn_inventory')
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    CART_BUTTON = (By.CSS_SELECTOR, ".shopping_cart_link")
    FILTER_DROPDOWN = (By.CSS_SELECTOR, ".product_sort_container")

class CarTPage:
    CART_ITEMS = (By.CLASS_NAME, 'cart_item')
    ITEM_NAME = (By.CLASS_NAME, 'inventory_item_name')
    REMOVE_BUTTON = (By.CLASS_NAME, "cart_button")
    CHECKOUT_BUTTON = (By.ID, 'checkout')
    CART_TOTAL = (By.CLASS_NAME, 'summary_total_label')

class CheckOutStepOnePage:
    FIRST_NAME_FIELD = (By.ID, 'first-name')
    LAST_NAME_FIELD = (By.ID, 'last-name')
    POSTAL_CODE_FIELD = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    CANCEL_BUTTON = (By.ID, 'cancel')
    ERROR_MESSAGE = (By.ID, '.error-message-container')

class CheckOutStepTwoPage:
    ITEM_LIST = (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
    TOTAL_PRICE = (By.CSS_SELECTOR, ".summary_total_label")
    FINISH_BUTTON = (By.ID, 'finish')
    CANCEL_BUTTON = (By.ID, 'cancel')
    COMPLETE_TEXT = (By.CSS_SELECTOR, '.complete-header')
