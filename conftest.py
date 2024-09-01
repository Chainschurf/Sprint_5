import pytest
from selenium import webdriver
from add.config import Config
from add.locators import ButtonsLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver():
    chrome = webdriver.Chrome()
    chrome.get(Config.URL)
    yield chrome
    chrome.quit()


@pytest.fixture
def register_page(driver):
    driver.get(Config.URL)
    driver.find_element(*ButtonsLocators.ENTER_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 15).until(
        expected_conditions.visibility_of_element_located(ButtonsLocators.ENTER_BUTTON))

    driver.find_element(*ButtonsLocators.REGISTER_INSTEAD_LINK).click()
    WebDriverWait(driver, 15).until(
        expected_conditions.visibility_of_element_located(ButtonsLocators.REGISTER_BUTTON))
