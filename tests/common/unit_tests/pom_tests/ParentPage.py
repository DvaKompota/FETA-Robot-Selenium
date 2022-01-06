from PageObjectLibrary import PageObject


class ParentPage(PageObject):
    url = "//parent"
    element = "Parent element"

    def parent_method(self):
        return f'Parent method: url={self.url}, element={self.element}'
