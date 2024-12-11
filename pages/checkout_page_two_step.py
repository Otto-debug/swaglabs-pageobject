from pages.base_page import BasePage
from utils.locators import CheckOutStepTwoPage


class CheckOutPageTwo(BasePage):
    def get_items_summary(self):
        """Возвращает список товаров на 2-ом оформлении"""
        elements = self.find_elements(CheckOutStepTwoPage.ITEM_LIST)
        return [element.text for element in elements]

    def get_total_price(self):
        """Возвращает итоговую сумму заказа"""
        total_price_text = self.find_element(CheckOutStepTwoPage.TOTAL_PRICE).text
        return total_price_text.split("$")[-1]

    def click_finish_button(self):
        self.find_element(CheckOutStepTwoPage.FINISH_BUTTON).click()

    def click_cancel_button(self):
        self.find_element(CheckOutStepTwoPage.CANCEL_BUTTON).click()

    def is_checkout_complete(self):
        """Проверка завершения заказа"""
        return "THANK YOU FOR YOU ORDER" in self.find_element(CheckOutStepTwoPage.COMPLETE_TEXT).text

    def modify_price(self, new_price):
        """Изменяет итоговую цену через JavaScript (для негативных тестов)."""
        script = f"document.querySelector('.summary_total_label').innerText = 'Total: ${new_price}';"
        self.driver.execute_script(script)
