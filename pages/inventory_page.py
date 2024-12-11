from pages.base_page import BasePage
from utils.locators import InventPage

from selenium.webdriver.common.by import By

class InventoryPage(BasePage):
    def is_inventory_displayed(self):
        return bool(self.find_element(InventPage.INVENTORY_LIST))

    def get_item_names(self):
        items = self.find_elements(InventPage.ITEM_NAME)
        return [item.text for item in items]
    
    def add_item_to_cart(self, item_name):
        items = self.find_elements(InventPage.ITEM_NAME)
        add_buttons = self.find_elements(InventPage.ITEM_ADD_BUTTON)

        for name, button in zip(items, add_buttons):
            if name.text == item_name:
                button.click()
                break

    def get_cart_badge_count(self):
        badge = self.find_elements(InventPage.CART_BADGE)
        return int(badge[0].text) if badge else 0

    def click_cart_button(self):
        self.find_element(InventPage.CART_BUTTON).click()

    def apply_filter(self, filter_option):
        dropdown = self.find_element(InventPage.FILTER_DROPDOWN).click()
        dropdown.find_element(By.XPATH, f"//option[text()='{filter_option}']").click()

