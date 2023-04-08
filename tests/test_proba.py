import time
import configuration as config
from model import *
from datas import *

class TestConduit:
    def setup_method(self):
        self.browser = conduitPage(browser=config.get_preconfigured_chrome_driver())
        self.browser.open()

    def teardown_method(self):
        self.browser.quit()
        pass


    def test_cookies_decline(self):
        self.browser.footer_decline_btn().click()
        cookie_decline = self.browser.get_cookies()
        assert cookie_decline["value"] == "decline"

    def test_cookies_accept(self):
        self.browser.footer_accept_btn().click()
        cookie_decline = self.browser.get_cookies()
        assert cookie_decline["value"] == "accept"

    def test_registration_invalid(self):
        self.browser.header_signup_btn().click()
        self.browser.input_email().send_keys(testuser['email'])
        self.browser.input_password().send_keys(testuser['password'])
        self.browser.sign_in_up_btn().click()
        assert self.browser.registration_login_fail_text() == 'Registration failed!'

    def test_registration_valid(self):
        self.browser.header_signup_btn().click()
        self.browser.input_username().send_keys(testuser['name'])
        self.browser.input_email().send_keys(testuser['email'])
        self.browser.input_password().send_keys(testuser['password'])
        self.browser.sign_in_up_btn().click()
        self.browser.registration_ok_btn().click()
        assert self.browser.header_logout_btn().is_displayed() == True

    def test_signin_invalid(self):
        self.browser.header_signin_btn().click()
        self.browser.input_email().send_keys('teszt@teszt.com')
        self.browser.input_password().send_keys(testuser['password'])
        self.browser.sign_in_up_btn().click()
        assert self.browser.registration_login_fail_text() == 'Login failed!'

    def test_signin_valid(self):
        self.browser.sing_in()
        assert self.browser.header_logout_btn().is_displayed() == True

    def test_logout(self):
        self.browser.sing_in()
        self.browser.header_logout_btn().click()
        assert self.browser.header_signin_btn().is_displayed() == True

    def test_new_article(self):
        self.browser.sing_in()
        self.browser.header_new_article_btn().click()
        self.browser.article_title().send_keys(test_article['article'])
        self.browser.article_about().send_keys(test_article['about'])
        self.browser.article_text().send_keys(test_article['article_text'])
        self.browser.article_tag().send_keys(test_article['tag'])
        self.browser.article_submit_btn().click()
        assert self.browser.edit_article_btn().is_displayed() == True
        assert self.browser.del_article_btn().is_displayed() == True

    def test_my_article_mod(self):
        self.browser.sing_in()
        self.browser.my_article().click()
        self.browser.edit_article_btn().click()
        self.browser.article_text().clear()
        self.browser.article_text().send_keys(test_article['article_text_mod'])
        self.browser.article_submit_btn().click()
        assert self.browser.my_article_paragraph().text == test_article['article_text_mod']

    def test_del_my_article(self):
        self.browser.sing_in()
        self.browser.my_article().click()
        self.browser.del_article_btn().click()
        assert not self.browser.my_article().is_displayed() == False

