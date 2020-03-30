import pytest
import inspect
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

@pytest.mark.usefixtures("setup")
class BaseClass:
    def verifyLinkPresence(self,linkName,time):
        wait = WebDriverWait(self.driver, time)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, linkName)))

    def selectOptionByText(self,text,locator):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def get_logger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('../reports/logfile.log')
        formatting = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatting)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger