import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


from PageBook import PageBook

# тестирование функционала сайта "Читай-город"


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(60)
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
    with allure.step("Проверяем что результаты поиска отображаются на странице"):
        author_name = "Марк Аврелий"
        first_product_title = driver.find_element(By.XPATH, "//span[contains(text(),'Марк Аврелий')]")
        assert author_name in first_product_title.text, "Книга не найдена"        


@allure.feature("READ")
@allure.severity("blocker")
@allure.title("Добавление товара в избранное")
def test_add_tab(driver):
    shop = PageBook(driver)
    with allure.step("Изменение города"):
        shop.city()  
    with allure.step("Скрытие информационных сообщений"):
        shop.cookies()     
    with allure.step("Поиск товара в строке поиска"):
        shop.search_input("Марк Аврелий")
    with allure.step("Добавление товара в закладки"):
        shop.add_tab()
    with allure.step("Проверяем что результаты поиска добавляются в избранное"):
        # first_product_title = driver.find_element(By.XPATH, "(//div[@class='vfm-swipe-banner-container'])[1]")
        login_banner = driver.find_element(By.CSS_SELECTOR, ".ui-header-modal.auth-modal-header").is_displayed()
        assert login_banner, "Окно для регистрации/входа не отображается"  

@allure.feature("READ")
@allure.severity("blocker")
@allure.title("Добавление товара в корзину")
def test_add_cart(driver):
    shop = PageBook(driver)
    with allure.step("Изменение города"):
        shop.city()
    with allure.step("Скрытие информационных сообщений"):
        shop.cookies()        
    with allure.step("Поиск товара через каталог"):
        shop.search_catalog()
    with allure.step("Скрытие информационных сообщений"):
        shop.cookies()
    with allure.step("Добавление товара в корзину"):
        shop.add_cart()
    with allure.step("Оформление покупки товаров"):
        shop.pay()
    with allure.step("Проверяем что результаты поиска добавляются в корзину"):
        name_book = "Все афоризмы"
        product_in_cart = driver.find_element(By.XPATH, "(//div[contains(text(),'Все афоризмы')])[1]")
        assert name_book in product_in_cart.text, "Товара нет в корзине" 


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
    with allure.step("Проверяем что появляется окно входа/регистрации"):
        login_banner = driver.find_element(By.CSS_SELECTOR, ".ui-header-modal.auth-modal-header").is_displayed()
        assert login_banner, "Окно для регистрации/входа не отображается"  


@allure.feature("READ")
@allure.severity("critical")
@allure.title("Возврат на главную страницу")
def test_return_main(driver):
    shop = PageBook(driver)
    with allure.step("Изменение города"):
        shop.city()
    with allure.step("Скрытие информационных сообщений"):
        shop.cookies()
    with allure.step("Поиск товара в строке поиска"):
        shop.search_input("Марк Аврелий")
    with allure.step("Переход на главную страницу"):
        shop.main_page()
    with allure.step("Проверяем что результаты поиска добавляются в корзину"):
        main_page = driver.current_url
        assert main_page == "https://www.chitai-gorod.ru/", "Страница не открылась" 
