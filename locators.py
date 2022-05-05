from selenium.webdriver.common.by import By

class BasePageLocators():
    OZON = (By.XPATH, '//input[@placeholder="Искать на Ozon"]')
    SEARCH = (By.XPATH, '//*[@aria-label="Поиск"]')