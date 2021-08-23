from resources import pages
from robot.libraries.BuiltIn import BuiltIn
import config


feta = pages.BasePage().selib


def robot_log(message):
    BuiltIn().log(message)


def setup_browser():
    options = ''
    options += 'add_argument("--headless")' if config.headless else ''
    options += '; ' if options and config.maximized else ''
    options += 'add_argument("--start-maximized")' if config.maximized else ''
    options += '; ' if options and config.fixed_size else ''
    options += f'add_argument("--window-size={config.horizontal},{config.vertical}")' if config.fixed_size else ''
    feta.open_browser(browser=config.browser, options=options)
    feta.set_selenium_timeout(config.selenium_timeout)


def open_page(page_name):
    page = getattr(pages, page_name.replace(' ', ''))()
    feta.go_to(page.PAGE_URL)
    feta.wait_until_element_is_visible(page.header)


def happy_elements_should_be_visible(page_name):
    page = getattr(pages, page_name.replace(' ', ''))()
    for element in page.happy_elements:
        feta.element_should_be_visible(element)


def page_heading_should_be_visible(page_name):
    page = getattr(pages, page_name.replace(' ', ''))()
    heading = True if getattr(page, 'page_heading_text', '') else False
    subheading = True if getattr(page, 'page_subheading_text', '') else False
    if heading:
        feta.element_text_should_be(page.page_heading, page.page_heading_text)
    if subheading:
        feta.element_text_should_be(page.page_subheading, page.page_subheading_text)
