from pages.base_page import BasePage
from utils.locators import CheckOutStepOnePage


class CheckOutPage(BasePage):
    def fill_checkout_form(self, first_name, last_name, postal_code):
        """Заполняем форму"""
        self.find_element(CheckOutStepOnePage.FIRST_NAME_FIELD).send_keys(first_name)
        self.find_element(CheckOutStepOnePage.LAST_NAME_FIELD).send_keys(last_name)
        self.find_element(CheckOutStepOnePage.POSTAL_CODE_FIELD).send_keys(postal_code)

    def click_continue_button(self):
        self.find_element(CheckOutStepOnePage.CONTINUE_BUTTON).click()

    def click_cancel_button(self):
        self.find_element(CheckOutStepOnePage.CANCEL_BUTTON).click()

    def get_error_message(self):
        return self.find_element(CheckOutStepOnePage.ERROR_MESSAGE).text

    def get_current_url(self):
        """Возвращает текущий url"""
        return self.driver.current_url
