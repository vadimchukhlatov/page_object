import logging
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, browser, wait=3):
        self.browser = browser
        self.wait = WebDriverWait(browser, wait)
        self.actions = ActionChains(browser)
        # self.__config_logger()

    # def __config_logger(self, to_file=False):
    #     self.logger = logging.getLogger(type(self).__name__)
    #     os.makedirs("logs", exist_ok=True)
    #     if to_file:
    #         self.logger.addHandler(logging.FileHandler(f"logs/{self.browser.test_name}.log"))
    #     self.logger.setLevel(level=self.browser.log_level)

    def _open_page(self, url):
        # self.logger.info(f"Open {url}")
        self.browser.get(url)

    def _text_xpath(self, text):
        return f"//*[text()='{text}']"

    def get_element(self, locator: tuple):
        # self.logger.info(f"Find element {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))

    def get_elements(self, locator: tuple):
        # self.logger.info(f"Find all elements {locator}")
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator: tuple):
        # self.logger.info(f"Click {locator}")
        self.actions.move_to_element(self.get_element(locator)).pause(0.3).click().perform()

    def input_value(self, locator: tuple, text: str):
        # self.logger.info(f"Input value {locator=}, {text=}")
        self.get_element(locator).click()
        self.get_element(locator).clear()
        for l in text:
            self.get_element(locator).send_keys(l)

    def get_alert_accept(self):
        # self.logger.info(f"Click warning accept")
        self.wait.until(EC.alert_is_present()).accept()
