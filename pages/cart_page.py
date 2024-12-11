from pages.base_page import BasePage
from utils.locators import CarTPage

class CartPage(BasePage):
    def get_cart_items(self):
        return self.find_elements(CarTPage.CART_ITEMS)

    def get_cart_item_names(self):
        items = self.get_cart_items()
        return [item.find_element(CarTPage.ITEM_NAME).text for item in items]

    def remove_item(self, item_name):
        items = self.get_cart_items()
        for item in items:
            if item_name in item.text:
                item.find_element(CarTPage.REMOVE_BUTTON).click()
                break

    def button_checkout(self):
        self.find_element(CarTPage.CHECKOUT_BUTTON).click()

    def get_cart_total(self):
        return self.get_text(CarTPage.CART_TOTAL)
