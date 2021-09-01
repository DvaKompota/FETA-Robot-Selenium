from resources import pages
from resources.utils.create_data import generate_customer
from resources.utils.convert_str import sentence_to_snake
from resources.test_data.get_data import feta_data
from robot.libraries.BuiltIn import BuiltIn


def generate_test_customer_data():
    feta_data["customer"] = generate_customer()


def fill_field_with(element_name, input_text):
    page = pages.TextBoxPage()
    element_name = sentence_to_snake(element_name)
    locator = getattr(page, element_name)
    text = decode_text(input_text)
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


def output_field_should_not_be_visible(element_name):
    page = pages.TextBoxPage()
    element_name = sentence_to_snake(element_name)
    locator = getattr(page, element_name)
    page.selib.element_should_not_be_visible(locator)


def output_field_text_should_contain(element_name, output_text):
    page = pages.TextBoxPage()
    element_name = sentence_to_snake(element_name)
    locator = getattr(page, element_name)
    text = decode_text(output_text)
    page.selib.element_should_contain(locator, text)


def decode_text(text):
    customer = feta_data["customer"]
    if text.lower() == 'nothing':
        return ''
    elif text.lower() == 'customer name':
        return customer['full_name']
    elif text.lower() == 'customer email':
        return customer['email']
    elif text.lower() == 'invalid email':
        return customer['email'].replace('@', '')
    elif text.lower() == 'customer address':
        return customer['full_address']
    else:
        return text
