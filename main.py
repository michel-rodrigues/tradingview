import csv
import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.webdriver import WebDriver


def open_browser(driver: WebDriver):
    driver.get(os.environ['TRADINGVIEW_URL'])
    driver.add_cookie({'name': 'sessionid', 'value': os.environ['SESSION_ID']})
    driver.add_cookie({'name': 'sessionid_sign', 'value': os.environ['SESSION_ID_SIGN']})
    driver.get(os.environ['TRADINGVIEW_URL'])
    time.sleep(2)


def _open_search_dialog(driver: WebDriver):
    button = driver.find_element(By.ID, 'header-toolbar-symbol-search')
    button.click()


def _choose_stock(stock: str, driver: WebDriver):
    input_tag = driver.find_element(By.XPATH, '//input[@class="search-ZXzPWcCf upperCase-ZXzPWcCf input-qm7Rg5MB"]')
    input_tag.send_keys(stock)
    input_tag.send_keys(Keys.ENTER)


def navigate_to_stock(stock: str, driver: WebDriver):
    _open_search_dialog(driver)
    _choose_stock(stock, driver)


def fetch_stocks():
    # Apagar a primeira linha do CSV
    with open('stocks.csv', newline='', encoding='iso-8859-1') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        return sorted(row['Código'] for row in reader if len(row['Código']) <= 6)


if __name__ == "__main__":
    firefox = webdriver.Firefox(service=Service(executable_path='geckodriver'))
    open_browser(firefox)
    for stock in fetch_stocks():
        navigate_to_stock(stock, driver=firefox)
        input()
    firefox.close()
