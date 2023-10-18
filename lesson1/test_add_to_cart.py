from selenium.webdriver.common.by import By


def test_add_item_in_the_cart(driver, authorization):
    text_before = driver.find_element(By.CSS_SELECTOR, "#item_4_title_link div").text
    print(text_before)

    button = driver.find_element(By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-backpack']")
    button.click()

    cart = driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']")
    cart.click()

    text_after = driver.find_element(By.CSS_SELECTOR, "a[id='item_4_title_link'] > div[class='inventory_item_name']").text
    assert text_before == text_after
