import allure

from bases.test_base import TestBase
from data_base_steps.login_db_steps import LoginDbSteps


@allure.suite("Data Base Connection Feature")
class TestDataBaseConnection(TestBase):

    @allure.tag("Data Base Connection")
    @allure.title("Connect with database and get the query result")
    def test_data_base_connection(self):
        login_db_steps = LoginDbSteps()
        product = "produto2"

        result = login_db_steps.get_specific_product_db(product)

        assert product == result[0][0]

    @allure.tag("Data Base Connection")
    @allure.title("Connect with database and get results")
    def test_data_base_connection_example(self):
        login_db_steps = LoginDbSteps()

        result = login_db_steps.get_products_db()
