import pytest
from pages.textboxes_page import TextBox
from utils.test_data import Data
from utils.tools import take_screenshot


class TestTextBoxes:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.text_box = TextBox(self.page)
        self.page.goto('https://demoqa.com/text-box')

    def test_text_boxes(self, test_setup):
        # Verify the functionality of the text boxes
        self.text_box.set_username(Data.username)
        self.text_box.set_email(Data.email)
        self.text_box.set_current_address(Data.current_address)
        self.text_box.set_permanent_address(Data.permanent_address)
        self.text_box.submit_form()
        # Check the result
        self.text_box.check_output_form(Data.username, Data.email, Data.current_address, Data.permanent_address)
        take_screenshot(self.page, "text_boxes")
