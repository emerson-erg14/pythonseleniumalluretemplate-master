import json


class JsonUtils:

    @classmethod
    def read_json(cls):
        # Read the file
        with open('config.json') as config_file:
            config = json.load(config_file)
        return config

    @classmethod
    def read_environment_key_json(cls, key):
        with open('config.json') as config_file:
            config = json.load(config_file)
            environment = config["environment"]
            result = config[environment][key]
        return result
