from resources.ngx_admin.page_objects.pages.BasePage import BasePage


class HomePage(BasePage):
    uri = "/pages"

    def __init__(self):
        super().__init__()
        self.PAGE_URL = f'{super().PAGE_URL}{self.uri}'
        self.happy_elements = super().happy_elements + []
