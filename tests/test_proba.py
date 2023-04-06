import time

import configuration as config
from model import conduitPage
#
class TestConduit:
    def setup_method(self):
        self.page = conduitPage(driver=config.get_preconfigured_chrome_driver())
        self.page.open()

    def teardown_method(self):
        self.page.close()

    def test_signin(self):
        self.page.header_signin_btn().click()
        self.page.input_email().send_keys('erdei.zoltan@teszt.hu')
        self.page.input_password().send_keys('Teszt12345')
        self.page.sign_in_up_btn().click()
        assert self.page.header_logout_btn().is_displayed() == True

    def test_registration(self):
        self.page.header_signup_btn().click()
        self.page.input_username().send_keys('TesztUser')
        self.page.input_email().send_keys('teszt@teszt.hu')
        self.page.input_password().send_keys('Ez123456')
        self.page.sign_in_up_btn().click()
        self.page.registration_ok_btn().click()
        assert self.page.header_logout_btn().is_displayed() == True

    def test_logout(self):
        self.page.header_signin_btn().click()
        self.page.input_email().send_keys('erdei.zoltan@teszt.hu')
        self.page.input_password().send_keys('Teszt12345')
        self.page.sign_in_up_btn().click()
        self.page.header_logout_btn().click()
        assert self.page.header_signin_btn().is_displayed() == True

