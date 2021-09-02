from resources import pages
from resources.utils.create_data import generate_customer
from resources.utils.convert_str import sentence_to_snake
from resources.test_data.get_data import feta_data
from robot.libraries.BuiltIn import BuiltIn


def generate_test_customer_data():
    feta_data["customer"] = generate_customer()


def fill_field_with(element_name, input_text):
    page = pages.RegisterPage()
    element_name = sentence_to_snake(element_name)
    locator = getattr(page, element_name)
    text = decode_text(input_text)
    page.selib.input_text(locator, text)


def check_captcha():
    page = pages.RegisterPage()
    if page.selib.get_element_count(page.captcha_iframe):
        page.selib.select_frame(page.captcha_iframe)
        page.click(page.captcha)
        page.selib.unselect_frame()


def captcha_verification_message_should_be_visible():
    page = pages.RegisterPage()
    page.selib.element_should_be_visible(page.captcha_verification_output)


def captcha_verification_text_should_be_correct():
    page = pages.RegisterPage()
    page.selib.element_text_should_be(page.captcha_verification_output, page.captcha_verification_text)


def push_button(element_name):
    page = pages.RegisterPage()
    element_name = sentence_to_snake(element_name)
    locator = getattr(page, element_name)
    page.click(locator)


def decode_text(text):
    customer = feta_data["customer"]
    if text.lower() == 'nothing':
        return ''
    elif text.lower() == 'customer first name' or text.lower() == 'first name':
        return customer['first_name']
    elif text.lower() == 'customer last name' or text.lower() == 'last name':
        return customer['last_name']
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
