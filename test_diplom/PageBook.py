from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PageBook:
    def __init__(self, browser):
        self.browser = browser

# скрыть элементы на странице
    def cookies(self):
        try:
            self.browser.find_element(By.CSS_SELECTOR, ".popmechanic-close").click()
        except Exception:
            pass
        try:
            self.browser.find_element(By.XPATH, "//div[contains(text(),'Понятно, закрыть')]").click()
        except Exception:
            pass

# выбор города доставки
    def city(self):
        self.browser.find_element(By.XPATH, "//div[text()='Изменить город ']").click()
        self.browser.find_element(By.CSS_SELECTOR, ".chg-app-input__control.chg-app-input__control--prefix").send_keys("Курган")
        self.browser.find_element(By.XPATH, "//li[contains(text(),'Курган')]").click()

# поиск нужного товара
    def search_input(self, search_name):
        self.browser.implicitly_wait(15)
        self.browser.find_element(By.CSS_SELECTOR, "input.search-form__input.search-form__input--search").send_keys(search_name)
        self.browser.find_element(By.XPATH, "//button[@aria-label='Найти']").click()

# добавление товара в избранное
    def add_tab(self):
        self.browser.implicitly_wait(15)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.PAGE_DOWN)
        self.browser.find_element(By.XPATH, "//article[1]//div[5]//button[2]").click()

# поиск нужного товара по каталогу
    def search_catalog(self):
        self.browser.implicitly_wait(15)
        self.browser.find_element(By.XPATH, "//button[@class='chg-app-button chg-app-button--primary chg-app-button--m chg-app-button--blue catalog-btn header__catalog-menu catalog-btn header__catalog-menu']").click()
        self.browser.find_element(By.XPATH, "//span[contains(text(),'Художественная литература')]").click()
        self.browser.find_element(By.XPATH, "//span[@class='categories-level-menu__item-title'][contains(text(),'Афоризмы. Цитаты')]").click()

# добавление понравившегося товара в корзину
    def add_cart(self):
        self.browser.implicitly_wait(15)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.PAGE_DOWN)
        self.browser.find_element(By.XPATH, "//article[@data-chg-product-brand='Яуза-пресс ООО']//button[@aria-label='false']").click()
        self.browser.find_element(By.XPATH, "//button[@aria-label='Корзина']").click()

# покупка на сайте выбранного товара
    def pay(self):
        self.browser.implicitly_wait(15)
        self.browser.get("https://www.chitai-gorod.ru/cart")
        self.browser.find_element(By.XPATH, "(//button[@class='chg-app-button chg-app-button--primary chg-app-button--xl chg-app-button--brand-blue chg-app-button--block cart-sidebar__order-button cart-sidebar__order-button'])[1]").send_keys("Марк Аврелий")
        # browser.find_element(By.CSS_SELECTOR, "svg.search-form__icon-search").click()

# возврат на главную страницу
    def main_page(self):
        self.browser.implicitly_wait(15)
        self.browser.find_element(By.CSS_SELECTOR, ".header__logo-wrapper").click()

# открытие карточки товара
    def page_product(self):
        self.browser.implicitly_wait(15)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.PAGE_DOWN)
        self.browser.find_element(By.XPATH, "(//a[contains(text(),'Мой любимый sputnik')])[1]").click()

# добавление отзыва на книгу
    def comment(self):
        self.browser.implicitly_wait(15)
        self.browser.find_element(By.CSS_SELECTOR, ".popmechanic-close").click()
        self.browser.find_element(By.XPATH, "(//button[contains(text(),'Понятно, закрыть')])[1]").click()
        body = self.browser.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.PAGE_DOWN)
        self.browser.find_element(By.XPATH, "(//button[@class='product-reviews__button product-reviews__button-review chg-app-button chg-app-button--primary chg-app-button--small chg-app-button--brand-blue'])[1]").click()
