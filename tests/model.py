from general_model import GeneralPage
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class conduitPage(GeneralPage):
    def __init__(self, driver: Chrome):
        super().__init__(driver, url='http://localhost:1667/#/')

    # Header elements
    def header_home_btn(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, 'conduit')))
    def header_home_btn_2(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, 'Home')))
    def header_signin_btn(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
    def header_signup_btn(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Sign up")))
    def header_logout_btn(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))
    def header_new_article_btn(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "New Article")))
    def header_settings_btn(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Settings")))


    # Login - Registration elements
    def input_username(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Username"]')))
    def input_email(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Email"]')))
    def input_password(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]')))
    def sign_in_up_btn(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')))
    def registration_ok_btn(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//button[@class="swal-button swal-button--confirm"]')))
    def registration_text(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Your registration was successful!")))

    # cookies - footer
    def footer_learn_more(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Learn More...")))
    def footer_accept_btn(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "I accept")))


