from PageObjectLibrary import PageObject
from selenium.common.exceptions import ElementClickInterceptedException


class CommonPage(PageObject):

    def click(self, locator):
        try:
            self.selib.click_element(locator)
        except ElementClickInterceptedException:
            self.selib.click_element(locator, action_chain=True)
