import pytest
import os
from selenium import webdriver
from dotenv import load_dotenv
from selene import browser
from qa_guru_hw10_tests.utils import attach

RES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'resources'))


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def setup_browser():
    browser.config.base_url = 'https://demoqa.com'

    options = webdriver.ChromeOptions()
    options.browser_version = "100.0"

    options.set_capability = (
        "selenoid:options",
        {
            "enableVNC": True,
            "enableVideo": True,
            "enableLog": True,
        },
    )
    browser.config.driver_options = options
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    browser.config.driver_remote_url = (
        f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub"
    )
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()
