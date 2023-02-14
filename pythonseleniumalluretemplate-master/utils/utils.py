import random

from utils.json_utils import JsonUtils


class Utils:


    @classmethod
    def get_radon_chars(cls, length):
        sample_string = 'abcdefghijklmnopqrstuvxzyw'  # define the specific string
        # define the condition for random string
        result = ''.join((random.choice(sample_string)) for x in range(length))

    @classmethod
    def get_radon_numbers(cls, length):
        sample_string = '1234567890'  # define the specific string
        # define the condition for random string
        result = ''.join((random.choice(sample_string)) for x in range(length))

    @classmethod
    def read_file(cls, path):
        return open(path, "r").read()

    @classmethod
    def listToString(cls, s):
        # initialize an empty string
        str1 = ""

        # traverse in the string
        for ele in s:
            str1 += ele

            # return string
        return str1

    @classmethod
    def convert_into_list(cls, result, description):
        results = []
        columns = [column[0] for column in description]
        for row in result:
            results.append(dict(zip(columns, row)))
        return results
