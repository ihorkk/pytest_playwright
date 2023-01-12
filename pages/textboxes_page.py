from playwright.sync_api import Page, expect


class TextBox:

    def __init__(self, page: Page):
        self.page = page
        # form
        self.__fullname_input = self.page.locator('[id="userName"]')
        self.__email_input = self.page.locator('[id="userEmail"]')
        self.__current_address_input = self.page.locator('[id="currentAddress"]')
        self.__permanent_address_input = self.page.locator('[id="permanentAddress"]')
        self.__submit_btn = self.page.locator('[id="submit"]')
        # output form
        self.__form_output = self.page.locator('div[id="output"]')
        self.__name_output = self.page.locator('[id="name"]')
        self.__email_output = self.page.locator('[id="email"]')
        self.__current_address_output = self.page.locator('p[id="currentAddress"]')
        self.__permanent_address_output = self.page.locator('p[id="permanentAddress"]')

    def set_username(self, user_name) -> None:
        self.__fullname_input.fill(user_name)

    def set_email(self, email) -> None:
        self.__email_input.fill(email)

    def set_current_address(self, address) -> None:
        self.__current_address_input.fill(address)

    def set_permanent_address(self, address) -> None:
        self.__permanent_address_input.fill(address)

    def submit_form(self) -> None:
        self.__submit_btn.click()
        self.__form_output.wait_for(state='visible')

    def check_output_form(self, user_name, email, address1, address2) -> None:
        assert self.__name_output.text_content() == f'Name:{user_name}', \
            f'Expected {user_name}, got {self.__name_output.text_content()}'
        assert self.__email_output.text_content() == f'Email:{email}', \
            f'Expected {email}, got {self.__email_output.text_content()}'
        expect(self.__current_address_output).to_have_text(f'Current Address :{address1}')
        expect(self.__permanent_address_output).to_have_text(f'Permananet Address :{address2}')
