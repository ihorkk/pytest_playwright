import pytest
from pages.buttons_page import Buttons
from utils.tools import take_screenshot


class TestButtons:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.buttons = Buttons(self.page)
        self.page.goto('https://demoqa.com/buttons')

    def test_buttons(self, test_setup):
        # Verify the functionality of the buttons
        self.buttons.perform_double_click()
        self.buttons.check_double_click_result()
        self.buttons.perform_right_click()
        self.buttons.check_right_click_result()
        self.buttons.perform_dynamic_click()
        self.buttons.check_dynamic_click_result()
        take_screenshot(self.page, "buttons")



