# from PageObjectLibrary import PageObject
from resources.pages.elements.ElementsPage import ElementsPage


class TextBoxPage(ElementsPage):
    PAGE_URL = "https://demoqa.com/text-box"

    page_heading_text = 'Text Box'

    def __init__(self):
        super().__init__()
        self.happy_elements = [self.header, self.header_link, self.header_img, self.page_heading]

    def validate_page_heading(self):
        self.selib.element_text_should_be(self.page_heading, self.page_heading_text)
