import pytest
import allure

from pages.login_page import LogPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckOutPage
from pages.checkout_page_two_step import CheckOutPageTwo

from utils.configurations import USERNAME, PASSWORD, URL

@allure.feature("Шаг 2 оформление заказа")
@pytest.fixture(scope='function')
def navigate_to_checkout_step_two(driver):
    with allure.step('Авторизация и добавление товара в корзину'):
        login_page = LogPage(driver)
        login_page.open(URL)
        login_page.enter_username(USERNAME)
        login_page.enter_password(PASSWORD)
        login_page.click_login_button()

    with allure.step('Добавляем товары в корзину'):
        inventory_page = InventoryPage(driver)
        inventory_page.add_item_to_cart("Sauce Labs Backpack")
        # inventory_page.add_item_to_cart("Sauce Labs Bike Light")
        inventory_page.click_cart_button()

    with allure.step('Переходим к оформлению заказа'):
        cart_page = CartPage(driver)
        cart_page.button_checkout()

    with allure.step('Заполняем форму на 1-ом шаге'):
        checkout_page = CheckOutPage(driver)
        checkout_page.fill_checkout_form(
            first_name='Markus',
            last_name='Sheppard',
            postal_code="12345"
        )
        checkout_page.click_continue_button()

    return CheckOutPageTwo(driver)

@allure.story("Положительные тесты")
def test_checkout_step_two_display(navigate_to_checkout_step_two):
    checkout_page_step_two = navigate_to_checkout_step_two

    with allure.step('Проверяем отображение товаров и суммы'):
        items = checkout_page_step_two.get_items_summary()
        total_price = checkout_page_step_two.get_total_price()

        assert "Sauce Labs Backpack" in items, "Товар 'Sauce Labs Backpack' отсутствует в итоговом списке!"
        # assert "Sauce Labs Bike Light" in items, "Товар 'Sauce Labs Bike Light' отсутствует в итоговом списке!"

        assert total_price == '32.39', f"Ожидалась сумма 32.39, но получено: {total_price}!"

@allure.story("Положительные тесты")
def test_finish_checkout(navigate_to_checkout_step_two):
    checkout_page_step_two = navigate_to_checkout_step_two

    with allure.step('Нажимаем кнопку Finish'):
        checkout_page_step_two.click_finish_button()

    with allure.step("Проверяем успешное завершение заказа"):
        assert checkout_page_step_two.is_checkout_complete(), 'Заказ не был успешно завершен'

@allure.story("Негативные тесты")
def test_no_items_in_checkout(driver):

    with allure.step('Авторизация'):
        login_page = LogPage(driver)
        login_page.enter_username(USERNAME)
        login_page.enter_password(PASSWORD)
        login_page.click_login_button()

    with allure.step('Переходим у оформлению заказа без добавление товара'):
        driver.get("https://www.saucedemo.com/checkout-step-two.html")

    with allure.step('Проверяем, что переход невозможен'):
        assert "inventory.html" in driver.current_url, "Пользователь смог перейти на шаг 2 без товаров!"

@allure.story("Негативные тесты")
def test_modify_total_price(navigate_to_checkout_step_two):
    checkout_page_step_two = navigate_to_checkout_step_two

    with allure.step('Эмулируем изменение цены'):
        checkout_page_step_two.modify_price("999.99")

    with allure.step('Проверяем, что итоговая сумма некорректная'):
        total_price = checkout_page_step_two.get_total_price()
        assert total_price != "999.99", "Итоговая сумма была изменена вручную, проверка не прошла!"
        