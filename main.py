import pytest
# from locators import BasePageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


url = "https://www.ozon.ru/"
phrase = "беспроводные наушники"

@pytest.fixture
#1. Перейдите на сервис http://www.ozon.ru/
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    # yield конструкция делит функцию на часть до и после тестов
    yield browser
    browser.quit()

class TestOzonUrl:
    def test_find_the_url(self, browser):
        browser.get(url)

    def test_find_elements(self, browser):
        browser.get(url)
        search_field = browser.find_element(By.XPATH, '//input[@placeholder="Искать на Ozon"]')
        search_field.send_keys(phrase)
        search_field.send_keys(Keys.RETURN)



        search_brand = browser.find_element(By.XPATH, '(//span[contains(text(), "Посмотреть все")])[2]')
        search_brand.click()
        search_beats = browser.find_element(By.XPATH, '//span[@class = "ys5"][contains(text(), "Beats")]')
        search_beats.click()

        search_brand = browser.find_element(By.XPATH, '(//span[@class = "show"])[2]')
        search_brand.click()
        search_samsung = browser.find_element(By.XPATH, '//span[@class = "ys5"][contains(text(), "Samsung")]')
        search_samsung.click()

        search_brand = browser.find_element(By.XPATH, '(//span[@class = "show"])[2]')
        search_brand.click()
        search_xiaomi = browser.find_element(By.XPATH, '//span[@class = "ys5"][contains(text(), "Xiaomi")]')
        search_xiaomi.click()

        price_element = browser.find_element(By.XPATH, '(//input[@type="text"])[3]')
        price_element.send_keys(Keys.DELETE)
        price_element.send_keys('20000')
 #4.  Ограничить цену – до 50 000

# #5. Отметить чекбокс – Высокий рейтинг


#6.  Из результатов поиска добавьте в корзину все нечетные товаров:
#
# def test_add_to_cart(browser):
#     page = ProductPage(url="", browser)
#     page.open()
#     page.add_to_cart_button()
#
#     if add_to_cart_button()

# • если нет кнопки добавить, то добавляем следующий четный товар,
# • нужно добавлять товар именно в корзину
# • не кликаем по кнопку «В корзину» которая относится к экспресс доставке,
# • если на товаре есть только кнопка «В корзину», которая относится к экспресс доставке,
# то пропускаем такой товар ищем следующий четный
# • добавляем в корзину пока не получится всего 8 добавленных.
# • Также требуется организовать способ хранения наименования товаров в отдельном классе для дальнейшей проверки по сценарию
# 7.  Перейдите в корзину, убедитесь, что все добавленные ранее товары находятся в корзине
# shopping_cart = browser.find_element(By.XPATH, )
# shopping_cart.click()
# assert "Ваша корзина - 8 товаров"
# 8.  Проверить, что отображается текст «Ваша корзина  - N товаров»
# 9.  Удалите все товары из корзины

# 10. Проверьте, что корзина не содержит никаких товаров
# 11. Добавить шаг, в котором будет приложен файл с информацией о всех добавленных товарах (наименование и цена).
# Также указать товар с наибольшей ценой. Сделать форматированный текст, чтоб было читаемо в аллюр отчете.
