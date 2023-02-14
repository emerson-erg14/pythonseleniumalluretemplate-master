import allure

from allure_commons.types import AttachmentType
from utils.driver_utils import DriverUtils
from utils.json_utils import JsonUtils
from utils.utils import Utils


class AllureUtils:

    @classmethod
    def allure_always_take_screenshot(cls, description):
        allure.attach(DriverUtils.INSTANCE.get_screenshot_as_png(), name=description,
                      attachment_type=AttachmentType.PNG)

    @classmethod
    def allure_take_screenshot_each_step(cls, description):
        take_screenshot_each_step = JsonUtils.read_environment_key_json("take_screenshot_each_step")
        if take_screenshot_each_step:
            allure.attach(DriverUtils.INSTANCE.get_screenshot_as_png(), name=description,
                          attachment_type=AttachmentType.PNG)

    @classmethod
    def allure_take_screenshot_in_the_end(cls, condition_erro, description):
        take_screenshot_test_just_in_error = JsonUtils.read_environment_key_json("take_screenshot_test_just_in_error")
        if take_screenshot_test_just_in_error:
            if condition_erro == 1:
                allure.attach(DriverUtils.INSTANCE.get_screenshot_as_png(), name=description,
                              attachment_type=AttachmentType.PNG)
        else:
            allure.attach(DriverUtils.INSTANCE.get_screenshot_as_png(), name=description,
                          attachment_type=AttachmentType.PNG)

    @classmethod
    def allure_log_query(cls, result, description):
        results = Utils.convert_into_list(result, description)
        allure.attach(f'{results}', "Query result:", allure.attachment_type.TEXT, results)
