from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from add.config import Config
from add.locators import ButtonsLocators, ConstructorPageLocators


class TestAccountToConstructorSwitching:
    def test_account_constructor_button_click(self, driver):
        driver.get(Config.URL)
        driver.find_element(*ButtonsLocators.ENTER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ButtonsLocators.ENTER_BUTTON))

        driver.find_element(*ButtonsLocators.CONSTRUCTOR_BUTTON).click()

        make_order_button = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ConstructorPageLocators.CONSTRUCTOR_PAGE))

        assert make_order_button.is_displayed()

    def test_account_logo_click(self, driver):
        driver.get(Config.URL)
        driver.find_element(*ButtonsLocators.ENTER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ButtonsLocators.ENTER_BUTTON))

        driver.find_element(*ButtonsLocators.LOGO_BUTTON).click()

        make_order_button = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ConstructorPageLocators.CONSTRUCTOR_PAGE))

        assert make_order_button.is_displayed()