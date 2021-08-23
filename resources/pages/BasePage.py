from PageObjectLibrary import PageObject


class BasePage(PageObject):
    PAGE_URL = "https://demoqa.com"
    header = "//header"
    header_link = f'{header}/a'
    header_img = f'{header_link}/img'
    page_heading = '//*[@class ="main-header"]'
    page_subheading = '//*[@class="col-12 mt-4 col-md-6"]'
    happy_elements = [header, header_link, header_img]
