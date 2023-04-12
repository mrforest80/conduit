

from general_model import GeneralPage
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from datas import *


class conduitPage(GeneralPage):
    def __init__(self, browser: Chrome):
        super().__init__(browser, url='http://localhost:1667/#/')

    # Sign in function
    def sing_in(self):
        signin_btn = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
        signin_btn.click()
        email = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Email"]')))
        email.send_keys(testuser['email'])
        password = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]')))
        password.send_keys(testuser['password'])
        login_btn = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')))
        login_btn.click()



    # Header elements
    def header_home_btn(self) -> WebElement:
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.LINK_TEXT, 'conduit')))

    def header_home_btn_2(self) -> WebElement:
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.LINK_TEXT, 'Home')))

    def header_signin_btn(self) -> WebElement:
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))

    def header_signup_btn(self) -> WebElement:
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Sign up")))

    def header_logout_btn(self) -> WebElement:
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))

    def header_new_article_btn(self) -> WebElement:
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "New Article")))

    def header_settings_btn(self) -> WebElement:
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Settings")))

    # Login - Registration elements
    def input_username(self) -> WebElement:
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Username"]')))

    def input_email(self) -> WebElement:
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Email"]')))

    def input_password(self) -> WebElement:
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]')))

    def sign_in_up_btn(self) -> WebElement:
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')))

    def registration_ok_btn(self) -> WebElement:
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//button[@class="swal-button swal-button--confirm"]')))

    def registration_text(self) -> WebElement:
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Your registration was successful!")))

    def registration_login_fail_text(self) -> WebElement:
        fail_text = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'swal-title')))
        return fail_text.text

    # cookies - footer elements
    def footer_learn_more(self) -> WebElement:
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Learn More...")))

    def footer_accept_btn(self) -> WebElement:
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//button[@class="cookie__bar__buttons__button cookie__bar__buttons__button--accept"]')))

    def footer_decline_btn(self) -> WebElement:
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//button[@class="cookie__bar__buttons__button cookie__bar__buttons__button--decline"]')))

    def get_cookies(self):
        return self.browser.get_cookie("vue-cookie-accept-decline-cookie-policy-panel")

    # new article elements
    def article_title(self) -> WebElement:
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Article Title"]')))

    def article_about(self) -> WebElement:
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//input[contains(@placeholder, "this article about?")]')))

    def article_text(self) -> WebElement:
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//textarea[@placeholder="Write your article (in markdown)"]')))

    def article_tag(self) -> WebElement:
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Enter tags"]')))

    def article_submit_btn(self) -> WebElement:
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))

    def edit_article_btn(self) -> WebElement:
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//i[@class="ion-edit"]')))

    def del_article_btn(self) -> WebElement:
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//i[@class="ion-trash-a"]')))

    # article elements
    def my_article(self) -> WebElement:
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, f'//h1[contains(text(), "{test_article["article"]}")]')))

    def my_article_paragraph(self) -> WebElement:
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'p')))

    def all_article(self):
        return WebDriverWait(self.browser, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//a[@class="preview-link"]/h1')))

    # page link
    def page_links(self):
        return WebDriverWait(self.browser, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//a[@class="page-link"]')))

    # tag list
    def side_bar_tag_list(self):
        return WebDriverWait(self.browser, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="sidebar"]/div[@class="tag-list"]/a')))

    def tag_list(self) -> WebElement:
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, f'//div[@class="feed-toggle"]/ul/li[3]/a')))