from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from add.config import Config
from add.locators import ConstructorPageLocators


class TestConstructorTabs:
    def test_bulki_tab_chosen(self, driver):
        driver.get(Config.URL)
        driver.find_element(*ConstructorPageLocators.BULKI_TAB)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ConstructorPageLocators.BULKI_SECTION))
        bulki_tab_selected = driver.find_element(*ConstructorPageLocators.BULKI_SELECTED)

        assert bulki_tab_selected

    def test_sousy_tab_chosen(self, driver):
        driver.get(Config.URL)
        driver.find_element(*ConstructorPageLocators.SOUSY_TAB).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ConstructorPageLocators.SOUSY_SECTION))
        sousy_tab_selected = driver.find_element(*ConstructorPageLocators.SOUSY_SELECTED)

        assert sousy_tab_selected

    def test_nachinki_tab_chosen(self, driver):
        driver.get(Config.URL)
        driver.find_element(*ConstructorPageLocators.NACHINKI_TAB).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ConstructorPageLocators.NACHINKI_SECTION))
        nachinki_tab_selected = driver.find_element(*ConstructorPageLocators.NACHINKI_SELECTED)

        assert nachinki_tab_selected
