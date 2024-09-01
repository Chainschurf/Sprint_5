from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from add.config import Config
from add.locators import SigningLocators, ButtonsLocators
import pytest


class TestLoggingIn:
    @pytest.mark.parametrize('email, password', [['menshikov_13@gmail.com', '123456']])
    def test_logging_out_button(self, driver, email, password):
        driver.get(Config.URL)
        driver.find_element(*ButtonsLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ButtonsLocators.ENTER_BUTTON))

        driver.find_element(*SigningLocators.EMAIL_FIELD).send_keys(email)

        driver.find_element(*SigningLocators.PASSWORD_FIELD).send_keys(password)

        driver.find_element(*ButtonsLocators.ENTER_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ButtonsLocators.MAKE_ORDER_BUTTON))

        driver.find_element(*ButtonsLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(
                    expected_conditions.visibility_of_element_located(ButtonsLocators.LOGOUT_BUTTON))

        driver.find_element(*ButtonsLocators.LOGOUT_BUTTON).click()

        enter_button = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ButtonsLocators.ENTER_BUTTON))

        assert enter_button.is_displayed()