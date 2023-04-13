import time
import csv
import allure

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

    @allure.id('TC-1')
    @allure.title('Adatkezelési nyilatkozat')
    @allure.description('Adatkezelési nyilatkozat elutasítása')
    def test_cookies_decline(self):
        self.browser.footer_decline_btn().click()
        cookie_decline = self.browser.get_cookies()

        assert cookie_decline["value"] == "decline"

    @allure.id('TC-2')
    @allure.title('Adatkezelési nyilatkozat')
    @allure.description('Adatkezelési nyilatkozat elfogadása')
    def test_cookies_accept(self):
        self.browser.footer_accept_btn().click()
        cookie_decline = self.browser.get_cookies()

        assert cookie_decline["value"] == "accept"

    @allure.id('TC-3')
    @allure.title('Regisztráció')
    @allure.description('Regisztráció invalid adatokkal')
    def test_registration_invalid(self):
        self.browser.header_signup_btn().click()
        self.browser.input_email().send_keys(testuser['email'])
        self.browser.input_password().send_keys(testuser['password'])
        self.browser.sign_in_up_btn().click()

        assert self.browser.registration_login_fail_text() == 'Registration failed!'

    @allure.id('TC-4')
    @allure.title('Regisztráció')
    @allure.description('Regisztráció valid adatokkal')
    def test_registration_valid(self):
        self.browser.header_signup_btn().click()
        self.browser.input_username().send_keys(testuser['name'])
        self.browser.input_email().send_keys(testuser['email'])
        self.browser.input_password().send_keys(testuser['password'])
        self.browser.sign_in_up_btn().click()
        self.browser.registration_ok_btn().click()

        assert self.browser.header_logout_btn().is_displayed() == True

    @allure.id('TC-5')
    @allure.title('Bejelentkezés')
    @allure.description('Bejelentkezés invalid adatokkal')
    def test_sign_in_invalid(self):
        self.browser.header_signin_btn().click()
        self.browser.input_email().send_keys(testuser['invalid_email'])
        self.browser.input_password().send_keys(testuser['password'])
        self.browser.sign_in_up_btn().click()

        assert self.browser.header_signin_btn().is_displayed() == True

    @allure.id('TC-6')
    @allure.title('Bejelentkezés')
    @allure.description('Bejelentkezés valid adatokkal')
    def test_signin_valid(self):
        self.browser.sign_in()

        assert self.browser.header_logout_btn().is_displayed() == True

    @allure.id('TC-7')
    @allure.title('Kijelentkezés')
    @allure.description('Kijelentkezés')
    def test_logout(self):
        self.browser.sign_in()
        self.browser.header_logout_btn().click()

        assert self.browser.header_signin_btn().is_displayed() == True

    @allure.id('TC-8')
    @allure.title('Adatok listázása')
    @allure.description('Címkék bejárása')
    def test_tag_list(self):
        self.browser.sign_in()
        num_of_tag_list = 0
        tags_list_side_bar = []
        tags_list_feed_toggle = []
        for tag in self.browser.side_bar_tag_list():
            self.browser.side_bar_tag_list()[num_of_tag_list].click()
            tags_list_side_bar.append(tag.text)
            tags_list_feed_toggle.append(self.browser.tag_list().text)
            num_of_tag_list += 1

        assert tags_list_side_bar == tags_list_feed_toggle

    @allure.id('TC-9')
    @allure.title('Új adat bevitel')
    @allure.description('Új cikk létrehozása')
    def test_new_article(self):
        self.browser.sign_in()
        self.browser.header_new_article_btn().click()
        self.browser.article_title().send_keys(test_article['article'])
        self.browser.article_about().send_keys(test_article['about'])
        self.browser.article_text().send_keys(test_article['article_text'])
        self.browser.article_tag().send_keys(test_article['tag'])
        self.browser.article_submit_btn().click()

        assert self.browser.edit_article_btn().is_displayed() == True
        assert self.browser.del_article_btn().is_displayed() == True
        assert self.browser.my_article_paragraph().text == test_article['article_text']

    @allure.id('TC-10')
    @allure.title('Meglévő adat módosítás')
    @allure.description('Saját cikkem megmódosítása')
    def test_my_article_mod(self):
        self.browser.sign_in()
        self.browser.my_article().click()
        self.browser.edit_article_btn().click()
        self.browser.article_text().clear()
        self.browser.article_text().send_keys(test_article['article_text_mod'])
        self.browser.article_tag().send_keys(test_article['tag'])
        self.browser.article_submit_btn().click()

        assert self.browser.my_article_paragraph().text == test_article['article_text_mod']

    @allure.id('TC-11')
    @allure.title('Több oldalas lista bejárása')
    @allure.description('Az alkalmazás oldalainak bejárása')
    def test_all_page(self):
        self.browser.sign_in()
        pages = []
        for link in self.browser.page_links():
            link.click()
            pages.append(link)

        assert len(pages) == len(self.browser.page_links())

    @allure.id('TC-12')
    @allure.title('Adat vagy adatok törlése')
    @allure.description('Saját cikkem törlése')
    def test_del_my_article(self):
        self.browser.sign_in()
        articles = []
        for link in self.browser.all_article():
            articles.append(link.text)
        self.browser.my_article().click()
        self.browser.del_article_btn().click()
        self.browser.refresh()
        self.browser.header_home_btn().click()
        articles_after_del = []
        for link in self.browser.all_article():
            articles_after_del.append(link.text)

        assert len(articles) == len(articles_after_del) + 1

    @allure.id('TC-13')
    @allure.title('Adatok lementése felületről')
    @allure.description('TestUser1 cikkeinek lementése')
    def test_save_datas(self):
        self.browser.sign_in()
        self.browser.testuser1().click()
        time.sleep(0.5)
        user1 = 0
        article_title = []
        article_content = []
        for article in self.browser.all_article():
            time.sleep(0.7)
            self.browser.test_user_articles()[user1].click()
            time.sleep(0.7)
            article_title.append(self.browser.article().text)
            article_content.append(self.browser.article_content().text)
            time.sleep(0.5)
            user1 += 1
            self.browser.back()
            time.sleep(0.5)

        with open('tests/saved_article.csv', 'w', encoding="utf8") as file:
            writer = csv.writer(file)
            writer.writerow(article_title)
            writer.writerow(article_content)

        with open('tests/saved_article.csv', 'r', encoding="utf8") as file:
            reader = csv.reader(file)
            file_list = []
            for row in reader:
                file_list.append(row)

        assert file_list[0][0] == article_title[0]


    @allure.id('TC-14')
    @allure.title('Ismételt és sorozatos adatbevitel adatforrásból')
    @allure.description('Cikkek létrehozása')
    def test_upload_datas(self):
        with open('tests/import_article.csv', 'r', encoding="utf8") as file:
            reader = csv.reader(file, delimiter=',')

            articles = []
            for row in reader:
                articles.append(row)

        self.browser.sign_in()

        len_loop = len(articles[0])
        for art in range(len_loop):
            self.browser.header_new_article_btn().click()
            self.browser.article_title().send_keys(articles[0][art-1])
            self.browser.article_text().send_keys(articles[1][art-1])
            self.browser.article_submit_btn().click()
            assert self.browser.my_article_paragraph().text == articles[1][art-1]
            self.browser.refresh()
