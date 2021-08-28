from resources import pages
from resources.utils.create_data import generate_customer
from resources.utils.convert_str import sentence_to_snake
from robot.libraries.BuiltIn import BuiltIn


def fill_field_with(element_name, input_text):
    page = pages.TextBoxPage()
    element_name = sentence_to_snake(element_name)
    locator = getattr(page, element_name)
    if input_text == 'Customer Name':
        text = generate_customer()['full_name']
    else:
        text = 'Default Text'
    page.selib.input_text(locator, text)


def push_button(element_name):
    page = pages.TextBoxPage()
    element_name = sentence_to_snake(element_name)
    locator = getattr(page, element_name)
    page.click(locator)


def output_field_should_be_visible(element_name):
    page = pages.TextBoxPage()
    element_name = sentence_to_snake(element_name)
    locator = getattr(page, element_name)
    page.selib.element_should_be_visible(locator)


def output_field_text_should_contain(element_name, output_text):
    page = pages.TextBoxPage()
    element_name = sentence_to_snake(element_name)
    locator = getattr(page, element_name)
    if output_text == 'Customer Name':
        text = generate_customer()['full_name']
    else:
        text = 'Default Text'
    page.selib.element_should_contain(locator, text)
