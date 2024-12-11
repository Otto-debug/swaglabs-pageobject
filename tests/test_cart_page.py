import allure
import pytest

from pages.login_page import LogPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from utils.configurations import USERNAME, PASSWORD, URL

@allure.feature("Корзина")
@pytest.fixture(scope="function")
def login_and_add_items_to_cart(driver):
    with allure.step('Авторизация и добавление товара в корзину'):
        login_page = LogPage(driver)
        login_page.open(URL)
        login_page.enter_username(USERNAME)
        login_page.enter_password(PASSWORD)
        login_page.click_login_button()

        inventory_page = InventoryPage(driver)
        inventory_page.add_item_to_cart("Sauce Labs Backpack")
        # inventory_page.add_item_to_cart("Sauce Labs Bike Light")
        inventory_page.click_cart_button()

    return CartPage(driver)

@allure.story("Положительные тесты корзины")
def test_items_in_cart(login_and_add_items_to_cart):
    cart_page = login_and_add_items_to_cart

    with allure.step('Проверяем наличие товаров в корзине'):
        items = cart_page.get_cart_item_names()
        assert "Sauce Labs Backpack" in items, "Товар 'Sauce Labs Backpack' отсутствует в корзине!"
        # assert "Sauce Labs Bike Light" in items, "Товар 'Sauce Labs Bike Light' отсутствует в корзине!"

@allure.story("Негативные тесты корзины")
def test_remove_all_items_from_cart(login_and_add_items_to_cart):
    cart_page = login_and_add_items_to_cart

    with allure.step('Удаляем все товары из корзины'):
        cart_page.remove_item('Sauce Labs Backpack')
        # cart_page.remove_item('Sauce Labs Bike Light')

    with allure.step('Проверяем что корзина пуста'):
        items = cart_page.get_cart_items()

        assert len(items) == 0, "Корзина должна быть пустой после удаления всех товаров!"
