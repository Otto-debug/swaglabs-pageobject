import allure
import pytest

from pages.login_page import LogPage
from pages.inventory_page import InventoryPage


from utils.configurations import USERNAME, PASSWORD, URL

@allure.feature('Главная страница')
@pytest.fixture(scope="function")
def login_and_go_to_inventory(driver):
    with allure.step('Логинимся на сайт'):
        login_page = LogPage(driver)
        login_page.open(URL)
        login_page.enter_username(USERNAME)
        login_page.enter_password(PASSWORD)
        login_page.click_login_button()

    with allure.step('Переходим на страницу товаров'):
        return InventoryPage(driver)

@allure.story('Положительные тесты страницы товаров')
@pytest.mark.parametrize(
    "item_name, expected_count",
    [
        ("Sauce Labs Backpack", 1),
        # ("Sauce Labs Bike Light", 1),
    ]
)
def test_add_item_to_cart(login_and_go_to_inventory, item_name, expected_count):
    inventory_page = login_and_go_to_inventory

    with allure.step(f'Добавляем товар: {item_name}'):
        inventory_page.add_item_to_cart(item_name)

    with allure.step('Проверяем кол-во товаров в корзине'):
        cart_count = inventory_page.get_cart_badge_count()
        assert cart_count == expected_count, f"Ожидалось {expected_count} товара в корзине, но найдено {cart_count}!"

@allure.story('Негативные тесты странице товаров')
def test_access_inventory_without_login(driver):
    with allure.step('Переходим на страницу товаров, без авторизации'):
        driver.get("https://www.saucedemo.com/inventory.html")

    with allure.step('Проверяем редирект на страницу авторизации'):
        assert 'login' in driver.current_url, "Пользователь смог получить доступ к странице без авторизации!"


