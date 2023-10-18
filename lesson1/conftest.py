import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(3)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def authorization(driver):
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

@pytest.fixture(scope="function")
def cart(driver, authorization):
    driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']").click()

