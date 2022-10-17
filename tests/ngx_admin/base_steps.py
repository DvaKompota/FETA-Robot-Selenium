from resources.ngx_admin.page_objects import components
from resources.ngx_admin.page_objects import pages
from tests.common.common_steps import setup_browser, robot_log, log_info, log_debug, log_warning


def open_page(page_name):
    page = getattr(pages, page_name.replace(' ', ''))()
    page.selib.go_to(page.PAGE_URL)
    page.selib.wait_until_element_is_visible(components.TopPanel.logo)


def validate_url(page_name):
    page = getattr(pages, page_name.replace(' ', ''))()
    page.selib.location_should_be(page.PAGE_URL)
