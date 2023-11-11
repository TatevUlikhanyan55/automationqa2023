from selenium.webdriver.common.by import By

from PythonPytestHomework435.Selenium_commands.POM.lib.helpers import Helpers


class CustomerServicePage(Helpers):
    customer_service_page_header = (By.CLASS_NAME, 'mb-z')

    def assert_header_on_customer_service_page(self, header_text = 'Customer Service Center'):
        actual_text =self.find(self.customer_service_page_header, get_text=True)
        assert actual_text == header_text