from resources.pages.BasePage import BasePage


class TextBoxPage(BasePage):
    uri = "/text-box"
    page_heading_text = 'Text Box'
    full_name_field = '//input[@id="userName"]'
    email_field = '//input[@id="userEmail"]'
    current_address_field = '//textarea[@id="currentAddress"]'
    permanent_address_field = '//textarea[@id="permanentAddress"]'
    submit_button = '//button[@id="submit"]'
    output_name = '//p[@id="name"]'
    output_email = '//p[@id="email"]'
    output_current_address = '//p[@id="currentAddress"]'
    output_permanent_address = '//p[@id="permanentAddress"]'

    def __init__(self):
        super().__init__()
        self.PAGE_URL = f'{super().PAGE_URL}{self.uri}'
        self.happy_elements = super().happy_elements + [self.page_heading]
