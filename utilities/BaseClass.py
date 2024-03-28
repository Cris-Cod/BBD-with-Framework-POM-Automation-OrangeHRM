import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


@pytest.mark.usefixtures("setup")
class BaseClass:


    def loggen(self):
        logger = logging.getLogger()
        fileHandler = logging.FileHandler('./Logs/logfile.log', mode='w')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.setLevel(logging.ERROR)

        return logger

    def selectOptionByText(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))