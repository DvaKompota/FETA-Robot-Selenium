from typing import Union
from PageObjectLibrary import PageObject
from SeleniumLibrary.base import ContextAware
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import ElementClickInterceptedException


class CommonPage(PageObject):

    def click(self, locator: Union[WebElement, str]) -> None:
        """ Click on an element on the page.

        First try to make a normal click on the element.
        If it fails, try to click on the element with javascript.

        :param locator:     WebElement or String with xpath of the element to click.

        :return:            None
        """
        try:
            self.selib.click_element(locator)
        except ElementClickInterceptedException:
            self.selib.click_element(locator, action_chain=True)

    def is_visible(self, locator: Union[WebElement, str]) -> bool:
        """ Return True if the element is visible, False otherwise.

        :param locator:     WebElement or String with xpath of the element to check visibility of.

        :return:            True if the element is visible, False otherwise.
        """
        return bool(ContextAware(self.selib).is_visible(locator))
