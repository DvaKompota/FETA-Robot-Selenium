from PageObjectLibrary import PageObject
from selenium.common.exceptions import ElementClickInterceptedException


class BasePage(PageObject):
    PAGE_URL = "https://demoqa.com"
    header = "//header"
    header_link = f'{header}/a'
    header_img = f'{header_link}/img'
    page_heading = '//*[@class ="main-header"]'
    page_subheading = '//*[@class="col-12 mt-4 col-md-6"]'
    ad_banner = '//*[@id="fixedban"]'
    ad_banner_close = '//*[@id="close-fixedban"]'
    happy_elements = [header, header_link, header_img]

    def click(self, locator):
        try:
            self.selib.click_element(locator)
        except ElementClickInterceptedException:
            self.selib.click_element(locator, action_chain=True)
