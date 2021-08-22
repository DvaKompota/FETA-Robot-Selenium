from PageObjectLibrary import PageObject


class ElementsPage(PageObject):
    PAGE_URL = "https://demoqa.com/elements"

    header = "//header"
    header_link = f'{header}/a'
    header_img = f'{header_link}/img'

    page_heading = '//*[@class ="main-header"]'
    page_heading_text = 'Elements'
    page_subheading = '//*[@class="col-12 mt-4 col-md-6"]'
    page_subheading_text = 'Please select an item from left to start practice.'

    def __init__(self):
        super().__init__()
        self.happy_elements = [self.header, self.header_link, self.header_img, self.page_heading, self.page_subheading]

    def open_page(self):
        self.selib.go_to(self.PAGE_URL)
        self.selib.wait_until_element_is_visible(self.header)

    def validate_happy_elements(self):
        for element in self.happy_elements:
            self.selib.element_should_be_visible(element)

    def validate_page_heading(self):
        self.selib.element_text_should_be(self.page_heading, self.page_heading_text)
        self.selib.element_text_should_be(self.page_subheading, self.page_subheading_text)
