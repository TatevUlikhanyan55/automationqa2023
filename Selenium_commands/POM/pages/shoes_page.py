# from hamcrest import equal_to

from selenium.webdriver.common.by import By
from PythonPytestHomework435.Selenium_commands.POM.lib.helpers import Helpers


class ShoesPage(Helpers):

    def __init__(self, driver):
        super().__init__(driver)

    best_sellers_btn = (By.CLASS_NAME, 'aaa-z')

    def click_on_best_sellers_btn(self):
        best_sellers_btn_txt=self.find(By.CLASS_NAME, get_text=True)
        assert best_sellers_btn_txt == "Shop All Women’s Best Selling Shoes"
        self.find_and_click(self.best_sellers_btn)

