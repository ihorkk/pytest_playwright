import pytest
from pages.checkboxes_page import CheckBox
from utils.tools import take_screenshot


class TestCheckBoxes:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.checkbox = CheckBox(self.page)
        self.page.goto('https://demoqa.com/checkbox')

    def test_check_boxes(self, test_setup):
        # Verify the functionality of the checkboxes
        self.checkbox.expand_home_directory()
        self.checkbox.select_checkbox('Downloads')
        self.checkbox.check_results('Downloads')
        self.checkbox.select_checkbox('Documents')
        self.checkbox.check_results('Documents')
        self.checkbox.select_checkbox('Desktop')
        self.checkbox.check_results('Desktop')
        take_screenshot(self.page, "checkboxes")


