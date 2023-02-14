import allure
import pyodbc

from utils.allure_utils import AllureUtils
from utils.json_utils import JsonUtils


class DataBaseUtils:

    @classmethod
    def connection(cls):
        server = JsonUtils.read_environment_key_json("db_url")
        database = JsonUtils.read_environment_key_json("db_name")
        username = JsonUtils.read_environment_key_json("db_user")
        password = JsonUtils.read_environment_key_json("db_password")
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        return cnxn

    @classmethod
    @allure.step('Executed query: {query}')
    def return_query_result(cls, query):
        cnxn = cls.connection()
        cursor = cnxn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        AllureUtils.allure_log_query(result, cursor.description)
        return result

    @classmethod
    @allure.step('Executed query: {query}')
    def execute_query(cls, query):
        cnxn = cls.connection()
        cursor = cnxn.cursor()

        cursor.execute(query)
        cnxn.commit()
