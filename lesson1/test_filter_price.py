import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_filter_low(driver, authorization):
    price_before = driver.find_elements(By.CSS_SELECTOR, 'div.inventory_item_price')
    print(len(price_before))
    list_before = []
    for x in price_before:
        list_before.append(float(x.text[1:]))
        print(x.text)

    button_filter = Select(driver.find_element(By.CSS_SELECTOR, 'select[data-test="product_sort_container"]'))
    button_filter.select_by_visible_text('Price (low to high)')
    time.sleep(3)

    price_after = driver.find_elements(By.CSS_SELECTOR, 'div.inventory_item_price')
    list_after = []
    for x in price_after:
        list_after.append(float(x.text[1:]))
        print(x.text)

    assert list_after == sorted(list_before)

def test_filter_high(driver, authorization):
    price_before = driver.find_elements(By.CSS_SELECTOR, 'div.inventory_item_price')
    print(len(price_before))
    list_before = []
    for x in price_before:
        list_before.append(float(x.text[1:]))
        print(x.text)

    button_filter = Select(driver.find_element(By.CSS_SELECTOR, 'select[data-test="product_sort_container"]'))
    button_filter.select_by_visible_text('Price (high to low)')
    time.sleep(3)

    price_after = driver.find_elements(By.CSS_SELECTOR, 'div.inventory_item_price')
    list_after = []
    for x in price_after:
        list_after.append(float(x.text[1:]))
        print(x.text)

    assert list_after == sorted(list_before, reverse=True)