import pytest

@pytest.mark.usefixtures("get_driver")
class BaseTest:
    def navigate_shoes_page_and_check_best_sellers_functionality(self):
        self.homepage.click_on_shoes_section()
        self.shoespage.click_on_best_sellers_btn()


