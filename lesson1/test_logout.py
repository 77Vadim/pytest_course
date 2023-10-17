from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_logout(driver, authorization):
    burger_menu = driver.find_element(By.ID,'react-burger-menu-btn')
    burger_menu.click()

    logout = driver.find_element(By.CSS_SELECTOR, '#logout_sidebar_link')
    logout.click()

    url_after = driver.current_url

    assert 'https://www.saucedemo.com/' == url_after
