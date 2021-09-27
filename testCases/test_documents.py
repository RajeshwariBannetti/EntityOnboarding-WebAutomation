from pageObjects.Documents import Documents
from pageObjects.LoginPage import LoginPage
from pageObjects.Promoters import Promoters
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

from utilities import XLUtils
import time


class Test_documents:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    path = ".//TestData/Bank statement.pdf"
    logger = LogGen.loggen()

    def test_new_entity_login(self, setup):
        self.logger.info("************* Test_003_Filter **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(5)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        time.sleep(3)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.logger.info("************* Login successful **********")
        time.sleep(5)
        self.pg = Promoters(self.driver)
        self.pg.clickonanyentity()
        self.driver.refresh()
        time.sleep(5)
        self.dp = Documents(self.driver)
        self.dp.clickdocumentstab()
        time.sleep(5)
        self.dp.clicklink()
        self.driver.close()
