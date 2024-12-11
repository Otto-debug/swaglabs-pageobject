import pytest
import allure

from pages.login_page import LogPage
from pages.inventory_page import InventoryPage
from utils.configurations import URL

@allure.feature("Авторизация")
@allure.story("Положительные тесты авторизации")
@pytest.mark.parametrize(
    "username, password",
    [("standard_user", "secret_sauce")]
)
def test_login_success(driver, username, password):
    with allure.step("Открываем страницу авторизации"):
        login_page = LogPage(driver)
        login_page.open(URL)

    with allure.step(f"Выполняем вход с параметрами: username={username}, password={password}"):
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login_button()

    with allure.step("Проверяем успешный вход"):
        inventory_page = InventoryPage(driver)
        assert inventory_page.is_inventory_displayed(), "Список товаров не отображается"

@allure.story("Негативные тесты")
@allure.story("Негативные тесты авторизации")
@pytest.mark.parametrize(
    "username, password, expected_error_message",
    [
        ("standard_user", "wrong_password", "Username and password do not match"),
        ("wrong_user", "secret_sauce", "Username and password do not match"),
        ("", "", "Username is required"),
    ]
)
def test_login_failure(driver, username, password, expected_error_message):
    with allure.step("Открываем страницу авторизации"):
        login_page = LogPage(driver)
        login_page.open(URL)

    with allure.step(f"Выполняем вход с параметрами: username={username}, password{password}"):
        login_page.enter_username(username)
        login_page.enter_password(password)

    with allure.step("Проверяем сообщение об ошибке"):
        error_message = login_page.get_error_message()
        assert expected_error_message in error_message, f"Ожидалась ошибка: {expected_error_message}"
