import allure
import pytest

from bases.test_base import TestBase
from flows.login_flow import LoginFlow
from pages.home_page import HomePage
from pages.login_page import LoginPage


@allure.suite("Login Feature")
class TestLogin(TestBase):

    @pytest.mark.smoke
    @allure.tag("Exception Scenario")
    @allure.title("Log in with wrong credentials")
    def test_login_with_wrong_credencials(self):
        login_page = LoginPage()
        user = "teste@base2.com.br"
        password = "senha"
        expected_message = "Your account may be disabled or blocked or the username/password you entered is incorrect."

        login_page.type_user(user)
        login_page.type_password(password)
        login_page.click_login()
        received_message = login_page.get_error_message()

        assert expected_message == received_message

    @allure.tag("Exception Scenario")
    @allure.title("Assert fail exemple")
    def test_assert_fail_example(self):
        login_page = LoginPage()
        user = "teste@base2.com.br"
        password = "wrong"
        expected_message = "Wrong message."

        login_page.type_user(user)
        login_page.type_password(password)
        login_page.click_login()
        received_message = login_page.get_error_message()

        assert expected_message == received_message

    @allure.tag("Success Scenario")
    @allure.title("Log in successfully")
    def test_login_successfully(self):
        login_page = LoginPage()
        home_page = HomePage()
        user = "templateautomacao"
        password = "123456"

        login_page.type_user(user)
        login_page.type_password(password)
        login_page.click_login()
        received_message = home_page.get_logged_user()

        assert user == received_message

    @allure.tag("Exception Scenario")
    @allure.title("Log in successfully using flow")
    def test_flows_exemple(self):
        login_flow = LoginFlow()
        user = "teste@base2.com.br"
        password = "senha"
        expected_message = "Your account may be disabled or blocked or the username/password you entered is incorrect."

        received_message = login_flow.do_login(user, password)

        assert expected_message == received_message



