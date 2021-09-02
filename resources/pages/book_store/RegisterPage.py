from resources.pages.BasePage import BasePage


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
    captcha = '//span[@id="recaptcha-anchor"]'
    register_button = '//button[@id="register"]'
    back_to_login_button = '//button[@id="gotologin"]'

    def __init__(self):
        super().__init__()
        self.PAGE_URL = f'{super().PAGE_URL}{self.uri}'
        self.happy_elements = super().happy_elements + [self.page_heading, self.page_subheading, self.first_name_field,
                                                        self.last_name_field, self.username_field, self.password_field,
                                                        self.register_button, self.back_to_login_button]
