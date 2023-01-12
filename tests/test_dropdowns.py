import pytest
from pages.dropdowns_page import DropdownMenu
from utils.test_data import Data
from utils.tools import take_screenshot


class TestDropdowns:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.menu = DropdownMenu(self.page)
        self.page.goto('https://demoqa.com/select-menu')

    def test_dropdowns(self, test_setup):
        # Verify the functionality of the dropdown menus
        self.menu.select_group_1_option_1()
        self.menu.select_professor()
        self.menu.select_color_old()
        self.menu.select_multiple_colors(Data.colors)
        self.menu.select_multiple_cars()
        take_screenshot(self.page, "dropdowns")
