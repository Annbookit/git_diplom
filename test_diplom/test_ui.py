import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from PageBook import PageBook

# тестирование функционала сайта "Читай-город"


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get("https://www.chitai-gorod.ru/")
    yield driver
    driver.quit()


@allure.feature("READ")
@allure.severity("blocker")
@allure.title("Поиск товара через строку поиска")
def test_search_product(driver):
    shop = PageBook(driver)
    with allure.step("Изменение города"):
        shop.city()
    with allure.step("Скрытие информационных сообщений"):
        shop.cookies()
    with allure.step("Поиск товара в строке поиска"):
        shop.search_input("Марк Аврелий")


@allure.feature("READ")
@allure.severity("blocker")
@allure.title("Добавление товара в избранное")
def test_add_tab(driver):
    shop = PageBook(driver)
    with allure.step("Изменение города"):
        shop.city()
    with allure.step("Поиск товара в строке поиска"):
        shop.search_input("Марк Аврелий")
    with allure.step("Скрытие информационных сообщений"):
        shop.cookies()
    with allure.step("Добавление товара в закладки"):
        shop.add_tab()


@allure.feature("READ")
@allure.severity("blocker")
@allure.title("Добавление товара в корзину")
def test_add_cart(driver):
    shop = PageBook(driver)
    with allure.step("Изменение города"):
        shop.city()
    with allure.step("Поиск товара через каталог"):
        shop.search_catalog()
    with allure.step("Скрытие информационных сообщений"):
        shop.cookies()
    with allure.step("Добавление товара в корзину"):
        shop.add_cart()
    with allure.step("Оформление покупки товаров"):
        shop.pay()


@allure.feature("READ")
@allure.severity("critical")
@allure.title("Добавление отзыва на товар")
def test_add_comment(driver):
    shop = PageBook(driver)
    with allure.step("Изменение города"):
        shop.city()
    with allure.step("Поиск товара в строке поиска"):
        shop.search_input("Харуки Мураками")
    with allure.step("Скрытие информационных сообщений"):
        shop.cookies()
    with allure.step("Открывание страницы с товаром"):
        shop.page_product()
    with allure.step("Комментирование товара"):
        shop.comment()


@allure.feature("READ")
@allure.severity("critical")
@allure.title("Возврат на главную страницу")
def test_return_main(driver):
    shop = PageBook(driver)
    with allure.step("Изменение города"):
        shop.city()
    with allure.step("Поиск товара в строке поиска"):
        shop.search_input("Марк Аврелий")
    with allure.step("Скрытие информационных сообщений"):
        shop.cookies()
    with allure.step("Переход на главную страницу"):
        shop.main_page()
