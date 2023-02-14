import selenium
import logging

from utils.json_utils import JsonUtils
from selenium.webdriver import chrome
from selenium.webdriver.edge.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.ie.service import Service as IeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService


class BrowsersUtils:

    USE_WEB_DRIVER_MANAGER = JsonUtils.read_environment_key_json("use_web_driver_manager")

    # Chrome
    @classmethod
    def chrome_local_headless(cls):
        options = selenium.webdriver.ChromeOptions()
        options.add_argument('headless')

        if cls.USE_WEB_DRIVER_MANAGER:
            service = ChromeService(ChromeDriverManager().install())
            return webdriver.Chrome(service=service, options=options)
        else:
            return selenium.webdriver.Chrome(options=options)

    @classmethod
    def chrome_local(cls):
        if cls.USE_WEB_DRIVER_MANAGER:
            service = ChromeService(ChromeDriverManager().install())
            return webdriver.Chrome(service=service)
        else:
            return selenium.webdriver.Chrome()

    @classmethod
    def chrome_remote_headless(cls):
        options = selenium.webdriver.ChromeOptions()
        options.add_argument("--headless")
        return selenium.webdriver.Remote(
            command_executor=JsonUtils.read_environment_key_json("selenium_hub"),
            options=options
        )

    @classmethod
    def chrome_remote(cls):
        options = selenium.webdriver.ChromeOptions()
        return selenium.webdriver.Remote(
            command_executor=JsonUtils.read_environment_key_json("selenium_hub"),
            options=options
        )

    # Firefox
    @classmethod
    def firefox_local_headless(cls):
        options = selenium.webdriver.FirefoxOptions()
        options.add_argument('--headless')

        if cls.USE_WEB_DRIVER_MANAGER:
            service = FirefoxService(executable_path=GeckoDriverManager().install())
            return webdriver.Firefox(service=service, options=options)
        else:
            return selenium.webdriver.Firefox(options=options)

    @classmethod
    def firefox_local(cls):
        if cls.USE_WEB_DRIVER_MANAGER:
            service = FirefoxService(executable_path=GeckoDriverManager().install())
            return webdriver.Firefox(service=service)
        else:
            return selenium.webdriver.Firefox()

    @classmethod
    def firefox_remote_headless(cls):
        options = selenium.webdriver.FirefoxOptions()
        options.add_argument('--headless')
        return selenium.webdriver.Remote(
            command_executor=JsonUtils.read_environment_key_json("selenium_hub"),
            options=options
        )

    @classmethod
    def firefox_remote(cls):
        options = selenium.webdriver.FirefoxOptions()
        return selenium.webdriver.Remote(
            command_executor=JsonUtils.read_environment_key_json("selenium_hub"),
            options=options
        )

    # IE
    @classmethod
    def ie_local(cls):
        options = selenium.webdriver.IeOptions()
        options.ignore_protected_mode_settings = True
        options.ignore_zoom_level = True
        options.require_window_focus = True
        options.add_argument("IntroduceInstabilityByIgnoringProtectedModeSettings=true")

        if cls.USE_WEB_DRIVER_MANAGER:
            service = IeService(IEDriverManager(log_level=logging.ERROR).install())
            return webdriver.Edge(service=service, options=options)
        else:
            return selenium.webdriver.Ie(options=options)

    @classmethod
    def ie_remote(cls):
        options = selenium.webdriver.IeOptions()
        return selenium.webdriver.Remote(
            command_executor=JsonUtils.read_environment_key_json("selenium_hub"),
            options=options
        )

    # Edge
    @classmethod
    def edge_local_headless(cls):
        options = Options()
        options.add_argument("headless")
        if cls.USE_WEB_DRIVER_MANAGER:
            service = EdgeService(EdgeChromiumDriverManager(log_level=logging.ERROR).install())
            return webdriver.Edge(service=service, options=options)
        else:
            return selenium.webdriver.Edge(options=options)

    @classmethod
    def edge_local(cls):
        if cls.USE_WEB_DRIVER_MANAGER:
            service = EdgeService(EdgeChromiumDriverManager(log_level=logging.ERROR).install())
            return webdriver.Edge(service=service)
        else:
            return selenium.webdriver.Edge()

    @classmethod
    def edge_remote_headless(cls):
        options = Options()
        options.add_argument("headless")
        return selenium.webdriver.Remote(
            command_executor=JsonUtils.read_environment_key_json("selenium_hub"),
            options=options
        )

    @classmethod
    def edge_remote(cls):
        options = Options()
        return selenium.webdriver.Remote(
            command_executor=JsonUtils.read_environment_key_json("selenium_hub"),
            options=options
        )
