import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ActionPage.Action import ConsultationPage
from Config.config import Config


@pytest.fixture(scope="module")
def driver_setup():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(40)
    driver.maximize_window()
    yield driver
    driver.quit()



@pytest.fixture(scope="module")
def start(driver_setup):
    driver = driver_setup
    lunch_page = ConsultationPage(driver)
    lunch_page.start_url(Config.BaseUrl)
    return lunch_page


def test_Consultation_website(start):
    start.click_start_consultation_button()

