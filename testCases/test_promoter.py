import time

from pageObjects.Documents import Documents
from pageObjects.Entity import Entity
from pageObjects.LoginPage import LoginPage
from pageObjects.Promoters import Promoters
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_004_New_entity:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

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
        self.dp.clicklink()
        time.sleep(5)
        # self.pg.clickPromoterguarantorstab()
        # time.sleep(5)
        # self.pg.clickaddnewpromoter()
        # time.sleep(5)
        # self.pg.setpromotername("rajeshwari B")
        # self.pg.setpromoterfathername("A B")
        self.driver.close()
