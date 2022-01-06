from resources.demoqa.pages.BasePage import BasePage


class ElementsPage(BasePage):
    uri = "/elements"
    page_heading_text = 'Elements'
    page_subheading_text = 'Please select an item from left to start practice.'

    def __init__(self):
        super().__init__()
        self.PAGE_URL = f'{super().PAGE_URL}{self.uri}'
        self.happy_elements = super().happy_elements + [self.page_heading, self.page_subheading]
