from chromedriver_binary import add_chromedriver_to_path
from resources.common.CommonPage import CommonPage
from SeleniumLibrary.base import LibraryComponent
from robot.libraries.BuiltIn import BuiltIn
import config


def robot_log(message):
    BuiltIn().log(message)


def setup_browser():
    add_chromedriver_to_path()
    feta = CommonPage().selib
    options = ''
    options += 'add_argument("--headless")' if config.headless else ''
    options += '; ' if options and config.maximized else ''
    options += 'add_argument("--start-maximized")' if config.maximized else ''
    options += '; ' if options and config.fixed_size else ''
    options += f'add_argument("--window-size={config.horizontal},{config.vertical}")' if config.fixed_size else ''
    feta.open_browser(browser=config.browser, options=options)
    feta.set_selenium_timeout(config.selenium_timeout)


def log_info(message) -> None:
    LibraryComponent(CommonPage().selib).info(message)


def log_debug(message) -> None:
    LibraryComponent(CommonPage().selib).debug(message)


def log_warning(message) -> None:
    LibraryComponent(CommonPage().selib).warn(message)
