import time

import pytest
import allure
from base_page import BasePage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



url = "https://www.ozon.ru/"
phrase = "беспроводные наушники"

@pytest.fixture
# фикстура нужна для подготовки тестового окружения, для создания параметров
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    # конструкция yield делит функцию на часть до и после
    yield browser
    browser.quit()

class TestOzon:
    @pytest.mark.smoke
    def test_find_url(self, browser):
        browser.get(url)

    def test_find_elements(self, browser, wait=10):
        browser.get(url)
        search_field = browser.find_element(By.XPATH, '//input[@placeholder="Искать на Ozon"]')
        search_field.send_keys(phrase)
        search_field.send_keys(Keys.RETURN)

        all_items = browser.find_element(By.XPATH, '//p[contains(text(), "Найти")]')
        all_items.send_keys('Beats').click

        all_items = browser.find_element(By.XPATH, '(//span[contains(text(), "Посмотреть все")])[2]')
        all_items.click()
        item2 = browser.find_element(By.XPATH, '//span[text()="Samsung"]')
        item2.click()
        time.sleep(wait)

        all_items = browser.find_element(By.XPATH, '(//span[contains(text(), "Посмотреть все")])[2]')
        all_items.click()
        item3 = browser.find_element(By.XPATH, '(//span[text()="Xiaomi"])[2]')
        item3.click()
        time.sleep(wait)

