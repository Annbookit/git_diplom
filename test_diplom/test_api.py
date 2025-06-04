import allure
import requests

# тестирование функционала сайта читай-город
base_url = "https://web-gate.chitai-gorod.ru"
token_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDkxNTE1MjgsImlhdCI6MTc0ODk4MzUyOCwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6ImE3ZDU4NjUwY2E3NjVjODdmYjFmNWE5MjI0NmRlNzdlZTY3MGMyNTI2YmI4NWVkOWMwOGMyZDk0OTY0MTM1MzQiLCJ0eXBlIjoxMH0.Z7Ifu04t_pcfGIafE1v-CiNTuQcrVXiEmpyST6aVmzc"
headers = {
    "accept": "application/json",
    "accept-language": "ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": f"Bearer {token_key}",
    "content-type": "application/json",
    "origin": "https://www.chitai-gorod.ru",
    "priority": "u=1, i",
    "referer": "https://www.chitai-gorod.ru/",
    "sec-ch-ua": '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
    }


@allure.feature("READ")
@allure.severity("blocker")
@allure.title("Добавление товара в корзину")
def test_add_cart(id=2631084):
    product = {
        "id": id,
        "adData": {"item_list_name": "search", "product_shelf": ""}
    }
    resp = requests.post(base_url + '/api/v1/cart/product', json=product, headers=headers)
    print(resp.status_code)
    assert resp.status_code == 200


@allure.feature("READ")
@allure.severity("critical")
@allure.title("Добавление товара без указания id")
def test_not_id_cart():
    resp = requests.put(base_url + '/api/v1/cart/product',  headers=headers)
    assert resp.status_code == 405


@allure.feature("READ")
@allure.severity("blocker")
@allure.title("Добавление товара с не существующим id")
def test_none_id__add_cart():
    add_position = {
    "id": 333,
    "adData": {
        "item_list_name": "product-page"
        }
    }
    resp = requests.post(base_url + '/api/v1/cart/product', json=add_position, headers=headers)
    assert resp.status_code == 500


@allure.feature("READ")
@allure.severity("blocker")
@allure.title("Оформление товаров в корзине")
def test_pay_product():
    resp = requests.get(base_url + '/api/v1/orders/checkout?userType=individual&orderType=order', headers=headers)
    assert resp.status_code == 200


@allure.feature("READ")
@allure.severity("critical")
@allure.title("Удаление из корзины отсутствующего товара")
def test_del_cart():
    resp = requests.delete(base_url + '/api/v1/cart/product/186354025', headers=headers)
    assert resp.status_code == 404
