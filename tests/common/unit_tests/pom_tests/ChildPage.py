from tests.common.unit_tests.pom_tests.ParentPage import ParentPage


class ChildPage(ParentPage):
    uri = "/child"
    element = "Child element"

    def __init__(self):
        super().__init__()
        self.url = f'{super().url}{self.uri}'

    def child_method(self):
        return f'Child method: url={self.url}, element={self.element}'
