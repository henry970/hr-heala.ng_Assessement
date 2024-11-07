from LocatorsPage.locators import ConsultationPageLocators, SymptomInformationLocators
import time
import logging
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure logging

class ConsultationPage:
    def __init__(self, driver):
        self.driver = driver

    def start_url(self, url):
        self.driver.get(url)
        time.sleep(6)

    def click_start_consultation_button(self):
        try:
            click_start_consultation_button = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(ConsultationPageLocators.CLICK_CONSULTATION_BUTTON))
            click_start_consultation_button.click()
            self.driver.refresh()
            time.sleep(200)
        except TimeoutException:
            logging.error('Timeout: The "Start Consultation" button is not clickable or visible.')
            # Take a screenshot if the button is not visible or the action fails
            self.take_screenshot('start_consultation_button_timeout')
        except Exception as e:
            logging.error(f'An unexpected error occurred: {str(e)}')
            # Take a screenshot for any other exceptions
            self.take_screenshot('start_consultation_button_error')

    def take_screenshot(self, failed):
        screenshot_path = f'./screenshots/{failed}.png'
        self.driver.get_screenshot_as_file(screenshot_path)
        logging.info(f'Screenshot saved at {screenshot_path}')
