import os
from selenium import webdriver

PLATFORM_TO_URL = {
    'qe': {
        'home': 'https://home.qe.com',
    },
    'local': {
        'home': 'localhost:8000',
    }
}

VARIABLES = {
    'qe': {
        'username': 'test',
        'password': 'testpassword',
    }
}


def _get_phantomjs():
    return webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true'],
                               service_log_path=os.path.devnull)

BROWSER_TO_DRIVER = {
    '0': _get_phantomjs,
}


