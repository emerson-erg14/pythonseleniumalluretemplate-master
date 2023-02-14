import pytest

from utils.allure_utils import AllureUtils
from utils.driver_utils import DriverUtils
from utils.json_utils import JsonUtils


class TestBase:

    @pytest.fixture(autouse=True)
    def base_test(self, before_suite, after_suite, request):
        # setUp
        DriverUtils.INSTANCE = DriverUtils.create_instance()
        DriverUtils.INSTANCE.get(JsonUtils.read_environment_key_json("default_application_url"))

        tests_failed_before_module = request.session.testsfailed

        yield

        # tearDown
        tests_failed_during_module = request.session.testsfailed - tests_failed_before_module
        AllureUtils.allure_take_screenshot_in_the_end(tests_failed_during_module, "Image from the final result")
        DriverUtils.INSTANCE.quit()










