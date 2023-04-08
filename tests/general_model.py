from selenium import webdriver
from datetime import datetime

class GeneralPage:

    def __init__(self, browser: webdriver.Chrome, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
        # self.browser.maximize_window()

    def close(self):
        self.browser.close()

    def quit(self):
        self.browser.quit()

    def refresh(self):
        self.browser.refresh()

    def save_screen(self, path):
        filename = f'{self.browser.title}-{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.png'
        print(f'Screenshot attempt: {path}\\{filename}') # path\filename.png --> C:\screenshots\filename.png
        if not self.browser.save_screenshot(f'{path}\\{filename}'):
            print('Screenshot failed.')


