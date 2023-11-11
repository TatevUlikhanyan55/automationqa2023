import pytest

from PythonPytestHomework435.Selenium_commands.POM.tests.base_test import BaseTest


class TestShoesSelection(BaseTest):
    def test_check_best_sellers_functionality(self):
        self.navigate_shoes_page_and_check_best_sellers_functionality()


