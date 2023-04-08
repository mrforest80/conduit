
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



def get_preconfigured_chrome_driver() -> webdriver.Chrome:
    service = Service(executable_path=ChromeDriverManager().install())
    option = Options()
    option.add_experimental_option('detach', True)
    option.add_argument("--lang=hu")
    option.add_argument('--headless')
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-dev-shm-usage')

    return webdriver.Chrome(service=service, options=option)
