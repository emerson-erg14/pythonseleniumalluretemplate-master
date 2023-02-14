import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.allure_utils import AllureUtils
from utils.driver_utils import DriverUtils
from utils.json_utils import JsonUtils



class PageBase:

    TIME_OUT = JsonUtils.read_environment_key_json("default_time_out_in_seconds")

    def __init__(self):
        self.instance = DriverUtils.INSTANCE


    def wait_for_Element(self, locator):
        element = WebDriverWait(self.instance, self.TIME_OUT).until(EC.presence_of_element_located(locator))
        WebDriverWait(self.instance, self.TIME_OUT).until(EC.element_to_be_clickable(element))
        return element

    @allure.step('Typing value: "{text}" on the element: "{locator}"')
    def send_Keys(self, locator, text):
        self.wait_for_Element(locator).send_keys(text)
        AllureUtils.allure_take_screenshot_each_step("Image from the input:")

    @allure.step('Clicking on the element "{locator}"')
    def click(self, locator):
        self.wait_for_Element(locator).click()
        AllureUtils.allure_take_screenshot_each_step("Image from the click on the element:")

    @allure.step('Getting value from the locator: "{locator}"')
    def get_text(self, locator):
        text = self.wait_for_Element(locator).text
        AllureUtils.allure_take_screenshot_each_step("Image getting the value:")
        return text

    @allure.step('Returning the state of the locator: "{locator}"')
    def is_enabled(self, locator):
        element = WebDriverWait(self.instance, self.TIME_OUT).until(EC.visibility_of_element_located(locator))
        AllureUtils.allure_take_screenshot_each_step("Image getting the value returned:")
        return bool(element)
