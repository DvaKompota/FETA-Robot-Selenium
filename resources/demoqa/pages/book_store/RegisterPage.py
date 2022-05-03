from resources.demoqa.pages.BasePage import BasePage


class RegisterPage(BasePage):
    uri = "/register"
    page_heading_text = 'Register'
    user_form = '//form[@id="userForm"]'
    page_subheading = f'{user_form}//h4'
    page_subheading_text = 'Register to Book Store'
    first_name_field = '//input[@id="firstname"]'
    last_name_field = '//input[@id="lastname"]'
    username_field = '//input[@id="userName"]'
    password_field = '//input[@id="password"]'
    captcha_iframe = '//iframe[@title="reCAPTCHA"]'
    captcha = '//span[@id="recaptcha-anchor"]'
    captcha_verification_output = '//*[@id="output"]//*[@id="name"]'
    captcha_verification_text = 'Please verify reCaptcha to register!'
    register_button = '//button[@id="register"]'
    back_to_login_button = '//button[@id="gotologin"]'
    register_happy_elements = [page_subheading, first_name_field, last_name_field, username_field, password_field,
                               register_button, back_to_login_button]

    def __init__(self):
        super().__init__()
        self.PAGE_URL = f'{super().PAGE_URL}{self.uri}'
        self.happy_elements = super().happy_elements + [self.page_heading] + self.register_happy_elements
