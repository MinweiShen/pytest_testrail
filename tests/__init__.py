import pytest
from consts import (
    PLATFORM_TO_URL,
    VARIABLES,
    BROWSER_TO_DRIVER
)


class BaseTestClass():
    @classmethod
    def setup_class(cls):
        cls.platform = pytest.config.getoption('--platform')
        cls.env = VARIABLES[cls.platform]

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        self.driver = BROWSER_TO_DRIVER[pytest.config.getoption('--browser')]()
        self.login()

    def teardown_method(self, method):
        self.logout()
        if self.driver:
            self.driver.quit()

    def login(self):
        pass

    def logout(self):
        pass
