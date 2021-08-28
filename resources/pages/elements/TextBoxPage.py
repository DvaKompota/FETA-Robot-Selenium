from resources.pages.BasePage import BasePage


class TextBoxPage(BasePage):
    uri = "/text-box"
    page_heading_text = 'Text Box'
    full_name_field = '//input[@id="userName"]'
    submit_button = '//button[@id="submit"]'
    output_name_field = '//*[@id="name"]'

    def __init__(self):
        super().__init__()
        self.PAGE_URL = f'{super().PAGE_URL}{self.uri}'
        self.happy_elements = super().happy_elements + [self.page_heading]
