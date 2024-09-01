from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from add.config import Config
from add.locators import ButtonsLocators, SigningLocators
import pytest


class TestLoggingIn:
    @pytest.mark.parametrize('email, password', [['alexandermenshikov13777@yandex.ru', '123456']])
    def test_enter_account_button(self, driver, email, password):
        driver.get(Config.URL)
        driver.find_element(*ButtonsLocators.ENTER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ButtonsLocators.ENTER_BUTTON))

        driver.find_element(*SigningLocators.EMAIL_FIELD).send_keys(email)

        driver.find_element(*SigningLocators.PASSWORD_FIELD).send_keys(password)

        driver.find_element(*ButtonsLocators.ENTER_BUTTON).click()

        make_order_button = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ButtonsLocators.MAKE_ORDER_BUTTON))

        assert make_order_button.is_displayed()

    @pytest.mark.parametrize('email, password', [['alexandermenshikov13777@yandex.ru', '123456']])
    def test_personal_account_button(self, driver, email, password):
        driver.get(Config.URL)
        driver.find_element(*ButtonsLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ButtonsLocators.ENTER_BUTTON))

        driver.find_element(*SigningLocators.EMAIL_FIELD).send_keys(email)

        driver.find_element(*SigningLocators.PASSWORD_FIELD).send_keys(password)

        driver.find_element(*ButtonsLocators.ENTER_BUTTON).click()

        make_order_button = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ButtonsLocators.MAKE_ORDER_BUTTON))

        assert make_order_button.is_displayed()

    @pytest.mark.parametrize('email, password', [['alexandermenshikov13777@yandex.ru', '123456']])
    def test_registration_form_button(self, driver, email, password):
        driver.get(Config.URL)
        driver.find_element(*ButtonsLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*ButtonsLocators.REGISTER_INSTEAD_LINK).click()
        driver.find_element(*ButtonsLocators.REGISTRATION_FORM_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ButtonsLocators.ENTER_BUTTON))

        driver.find_element(*SigningLocators.EMAIL_FIELD).send_keys(email)

        driver.find_element(*SigningLocators.PASSWORD_FIELD).send_keys(password)

        driver.find_element(*ButtonsLocators.ENTER_BUTTON).click()

        make_order_button = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ButtonsLocators.MAKE_ORDER_BUTTON))

        assert make_order_button.is_displayed()

    @pytest.mark.parametrize('email, password', [['alexandermenshikov13777@yandex.ru', '123456']])
    def test_password_restore_form_button(self, driver, email, password):
        driver.get(Config.URL)
        driver.find_element(*ButtonsLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*ButtonsLocators.PASSWORD_RESTORE_BUTTON).click()
        driver.find_element(*ButtonsLocators.FROM_PASSWORD_RESTORE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ButtonsLocators.ENTER_BUTTON))

        driver.find_element(*SigningLocators.EMAIL_FIELD).send_keys(email)

        driver.find_element(*SigningLocators.PASSWORD_FIELD).send_keys(password)

        driver.find_element(*ButtonsLocators.ENTER_BUTTON).click()

        make_order_button = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ButtonsLocators.MAKE_ORDER_BUTTON))

        assert make_order_button.is_displayed()
