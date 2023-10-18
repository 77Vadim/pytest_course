from selenium.webdriver.common.by import By


def test_checkout(driver, cart):
    driver.find_element(By.CSS_SELECTOR, 'button[data-test="checkout"]').click()

    driver.find_element(By.CSS_SELECTOR, 'input[data-test="firstName"]').send_keys('Vadim')
    driver.find_element(By.CSS_SELECTOR, 'input[data-test="lastName"]').send_keys('qwerr')
    driver.find_element(By.CSS_SELECTOR, 'input[data-test="postalCode"]').send_keys('1234')

    driver.find_element(By.CSS_SELECTOR, 'input[data-test="continue"]').click()

    driver.find_element(By.CSS_SELECTOR, 'button[data-test="finish"]').click()

    assert driver.current_url == 'https://www.saucedemo.com/checkout-complete.html'
