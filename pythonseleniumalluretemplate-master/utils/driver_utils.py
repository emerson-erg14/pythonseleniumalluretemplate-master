from utils.browsers_utils import BrowsersUtils
from utils.json_utils import JsonUtils


class DriverUtils:

    @classmethod
    def create_instance(cls):

        browser = JsonUtils.read_environment_key_json("browser")
        headless = JsonUtils.read_environment_key_json("headless")
        execution = JsonUtils.read_environment_key_json("execution")

        if browser == 'Chrome':
            if execution == 'local':
                if headless:
                    return BrowsersUtils.chrome_local_headless()
                else:
                    return BrowsersUtils.chrome_local()
            elif execution == 'remote':
                if headless:
                    return BrowsersUtils.chrome_remote_headless()
                else:
                    return BrowsersUtils.chrome_remote()
            else:
                raise Exception(f'Execution "{execution}" is not supported')

        elif browser == 'Firefox':
            if execution == 'local':
                if headless:
                    return BrowsersUtils.firefox_local_headless()
                else:
                    return BrowsersUtils.firefox_local()

            elif execution == 'remote':
                if headless:
                    return BrowsersUtils.firefox_remote_headless()
                else:
                    return BrowsersUtils.firefox_remote()
            else:
                raise Exception(f'Execution "{execution}" is not supported')

        elif browser == 'IE':
            if execution == 'local':
                return BrowsersUtils.ie_local()
            elif execution == 'remote':
                return BrowsersUtils.ie_remote()
            else:
                raise Exception(f'Execution "{execution}" is not supported')

        elif browser == 'Edge':
            if execution == 'local':
                if headless:
                    return BrowsersUtils.edge_local_headless()
                else:
                    return BrowsersUtils.edge_local()

            elif execution == 'remote':
                if headless:
                    return BrowsersUtils.edge_remote_headless()
                else:
                    return BrowsersUtils.edge_remote()

            else:
                raise Exception(f'Execution "{execution}" is not supported')



        else:
            raise Exception(f'Browser "{browser}" is not supported')
