import pytest
import allure

from pages.login_page import LogPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckOutPage

from utils.configurations import USERNAME, PASSWORD, URL

@allure.feature("Шаг 1 оформление заказа")
@pytest.fixture(scope="function")
def navigate_to_checkout_step_one(driver):
    with allure.step("Авторизация и добавление товаров в корзину"):
        login_page = LogPage(driver)
        login_page.open(URL)
        login_page.enter_username(USERNAME)
        login_page.enter_password(PASSWORD)
        login_page.click_login_button()

    with allure.step("Добавляем товар в корзину"):
        inventory_page = InventoryPage(driver)
        inventory_page.add_item_to_cart("Sauce Labs Backpack")
        inventory_page.click_cart_button()

    with allure.step("Переходим к оформлению заказа"):
        cart_page = CartPage(driver)
        cart_page.button_checkout()

    return CheckOutPage(driver)

@allure.story("Положительные тесты")
def test_checkout_step_one_success(navigate_to_checkout_step_one):
    checkout_page = navigate_to_checkout_step_one

    with allure.step("Заполняем форму с корректными данным"):
        checkout_page.fill_checkout_form(
            first_name='Markus',
            last_name='Sheppard',
            postal_code="12345"
        )

    with allure.step('Переходим к следующему шагу'):
        checkout_page.click_continue_button()
        assert "checkout-step-two" in checkout_page.get_current_url(), "Не удалось перейти на шаг 2 оформления заказа!"

@allure.story("Положительные тесты")
def test_cancel_button(navigate_to_checkout_step_one):
    checkout_page = navigate_to_checkout_step_one

    with allure.step("Проверяем кнопку Cancel"):
        checkout_page.click_cancel_button()

    with allure.step("Проверяем вернулись ли мы обратно на страницу Cart"):
        assert 'cart' in checkout_page.get_current_url(), "Кнопка 'Cancel' не вернула пользователя в корзину!"

@allure.story("Негативные тесты")
@pytest.mark.parametrize(
    "first_name, last_name, postal_code, error_message",
    [
        ("", "", "", "Error: First Name is required"),
        ("Markus", "", "", "Error: Last Name is required"),
        ("Markus", "Sheppard", "", "Error: Postal Code is required"),
        ("Markus", "Sheppard", "!!!", "Error: Postal Code is invalid"),  # Проверка на некорректный индекс
    ]
)
def test_checkout_step_one_validation(navigate_to_checkout_step_one,
                                      first_name, last_name,
                                      postal_code, error_message):
    checkout_page = navigate_to_checkout_step_one

    with allure.step(f'Заполняем форму данными: {first_name}, {last_name}, {postal_code}'):
        checkout_page.fill_checkout_form(
            first_name=first_name,
            last_name=last_name,
            postal_code=postal_code
        )
    with allure.step('Прожимаем кнопку Continue'):
        checkout_page.click_continue_button()

    with allure.step('Проверяем сообщение об ошибке'):
        actual_error = checkout_page.get_error_message()
        assert error_message in actual_error, f"Ожидалось сообщение: {error_message}, но получено: {actual_error}"
