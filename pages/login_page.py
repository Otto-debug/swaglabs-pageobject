from pages.base_page import BasePage
from utils.locators import LoginPage

class LogPage(BasePage):

    def enter_username(self, username):
        self.find_element(LoginPage.USERNAME).send_keys(username)

    def enter_password(self, passwd):
        self.find_element(LoginPage.PASSWORD).send_keys(passwd)

    def click_login_button(self):
        return self.find_element(LoginPage.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.get_text(LoginPage.ERROR_MESSAGE)
