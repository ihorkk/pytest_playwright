import pytest
from pages.radiobuttons_page import RadioButton
from utils.tools import take_screenshot


class TestRadioButtons:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.radio = RadioButton(self.page)
        self.page.goto('https://demoqa.com/radio-button')

    def test_radio_buttons(self, test_setup):
        # Verify the functionality of the radio buttons
        self.radio.select_radio_btn('Yes')
        self.radio.check_result('Yes')
        self.radio.select_radio_btn('Impressive')
        self.radio.check_result('Impressive')
        take_screenshot(self.page, "radio_buttons")