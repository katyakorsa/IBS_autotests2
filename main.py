import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

link = "https://www.ozon.ru/"

#1. Перейдите на сервис http://www.ozon.ru/
browser = webdriver.Chrome()
browser.get(link)

#2. Выполните поиск по «беспроводные наушники»
search_box = browser.find_element(By.XPATH, '//input[@placeholder="Искать на Ozon"]')
search_box.send_keys("беспроводные наушники")
search_button = browser.find_element(By.XPATH, '//*[@aria-label="Поиск"]')
search_button.click()

#3. Бренды : Beats, Samsung, Xiaomi
# добавить отладку времени - ожидание 10 секунд, чтобы тест не торопился выполнять следующий шаг
# подумать как лучше реализовать поиск по брендам - сразу нажать кнопку "показать все" или вводить в поле поиска бренд, кликать на бренд, затем освобождать поле и писать новое наименование
# если нажимать кнопку "показать все айтемы", то нужно будет воспользоваться ползунком для поиска
# подумать, как реализовать алгоритм для повторяющихся операций
# реализовать класс для всех айтемов

search_brand = browser.find_element(By.XPATH, '(//span[@class = "show"])[2]')
search_brand.click()
# search_brand_beats = browser.find_element(By.XPATH, '//span[@class = "x5s"][contains(text(), "Beats")]')
# search_brand_beats.click()
# search_brand_samsung = browser.find_element(By.XPATH, '//span[@class = "x5s"][contains(text(), "Samsung")]')
# search_brand_samsung.click()
# search_brand_xiaomi = browser.find_element(By.XPATH, '//span[@class = "x5s"][contains(text(), "Xiaomi")]')
# search_brand_xiaomi.click()

#4.  Ограничить цену – до 50 000

#5. Отметить чекбокс – Высокий рейтинг
# checkbox_rating = browser.find_element(By.XPATH, '//div[@value="Высокий рейтинг"]')
# checkbox_rating.click()

#6.  Из результатов поиска добавьте в корзину все нечетные товаров:
# • если нет кнопки добавить, то добавляем следующий четный товар,
# • нужно добавлять товар именно в корзину
# • не кликаем по кнопку «В корзину» которая относится к экспресс доставке,
# • если на товаре есть только кнопка «В корзину», которая относится к экспресс доставке, то пропускаем такой товар ищем следующий четный
# • добавляем в корзину пока не получится всего 8 добавленных.
# • Также требуется организовать способ хранения наименования товаров в отдельном классе для дальнейшей проверки по сценарию
# 7.  Перейдите в корзину, убедитесь, что все добавленные ранее товары находятся в корзине
# 8.  Проверить, что отображается текст «Ваша корзина  - N товаров»
# 9.  Удалите все товары из корзины
# 10. Проверьте, что корзина не содержит никаких товаров
# 11. Добавить шаг, в котором будет приложен файл с информацией о всех добавленных товарах (наименование и цена). Также указать товар с наибольшей ценой. Сделать форматированный текст, чтоб было читаемо в аллюр отчете.
