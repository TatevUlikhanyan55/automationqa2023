from selenium.webdriver.common.by import By
from PythonPytestHomework435.Selenium_commands.POM.lib.helpers import Helpers


class HomePage(Helpers):

    def __init__(self, driver):
        super().__init__(driver)

    shoes_section =(By.LINK_TEXT, 'SHOES')

    def click_on_shoes_section(self):
        self.find_and_click(self.shoes_section)

