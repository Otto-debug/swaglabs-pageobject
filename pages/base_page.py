from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        return self.driver.get(url)

    def find_element(self, locator):
        return WebDriverWait(self.driver, timeout=60).until(EC.presence_of_element_located(locator),
                                                            message=f"Can't find element {locator}")

    def find_elements(self, locator):
        return WebDriverWait(self.driver, timeout=60).until(EC.presence_of_all_elements_located(locator),
                                                            message=f"Can't find elements {locator}")

    def get_text(self, locator):
        try:
            return self.find_element(locator).text
        except NoSuchElementException:
            return False

    # def get_text(self, locator):
    #     try:
    #         return WebDriverWait(self.driver, timeout=20).until(EC.presence_of_element_located(locator),
    #                                                             message=f"Can't find element {locator}")
    #     except NoSuchElementException:
    #         return False
