import pytest
from tests import BaseTestClass


class TestDemoClass(BaseTestClass):
    @pytest.mark_testrail(1)
    def test_demo_class(self):
        pass