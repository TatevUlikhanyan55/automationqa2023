from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from os import path

driver = None


class Helpers:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)
        self.wait = WebDriverWait(self.driver, 10)

    def find(self, loc, timeout=10, get_text=False, get_attribute=False):
        elem = WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(loc))
        if get_text:
            return elem.text
        elif get_attribute:
            return elem.get_attribute(get_attribute)
        return elem

    def find_and_click(self, loc, timeout=10):
        elem = self.find(loc, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        elem.click()

    def find_and_send_keys(self, loc, inp_text, timeout=10):
        elem = self.find(loc, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        elem.send_keys(inp_text)

    def switch_window(self, window_id=0):
        self.driver.switch_to.window(self.driver.window_handles[window_id])

    def switch_to_alert(self):
        return self.driver.switch_to.alert

    def refresh_page(self):
        self.driver.refresh()

    def focus_on_element(self, element):
        self.actions.move_to_element(element).perform()

    def scroll_to(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def is_displayed(self, element):
        element.is_displayed()

    def is_selected(self, element):
        element.is_selected()
        return True

    def select_item(self, loc, timeout=10, index=1, text="", value=1, by_index: bool = False, by_text: bool = False,
                    by_value: bool = False):
        select = Select(self.find(loc, timeout))
        if by_index:
            select.select_by_index(index)
        elif by_text:
            select.select_by_visible_text(text)
        elif by_value:
            select.select_by_value(value)
        selected_option = select.first_selected_option
        return selected_option.text

    def get_file_in_temp_folder(self, FName):
        return path.join(path.dirname(path.dirname(path.realpath(__file__))), 'testdata\\' + FName)
