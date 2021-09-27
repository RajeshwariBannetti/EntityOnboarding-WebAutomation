import random
import string
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.Promoters import Promoters
from pageObjects.SPOC import SPOC
from testCases.test_new_entity import random_generator
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def generate_random_number(length=9):
    return int(''.join([str(random.randint(6, 9))]) + ''.join([str(random.randint(0, 9)) for _ in range(length)]))


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
        self.sp = SPOC(self.driver)
        self.sp.clickspoctab()
        time.sleep(5)
        self.sp.clickaddnewspoc()
        time.sleep(5)
        self.sp.setspocname("rajeshwari b")
        self.spocemail = random_generator() + "@gmail.com"
        self.sp.setspocemail(self.spocemail)
        self.spocmobile = generate_random_number()
        self.sp.setspocmobile(self.spocmobile)
        self.sp.clickdepartment()
        self.sp.selectdepartment()
        self.sp.clickIsprimary()
        self.sp.selectISprimary()
        self.sp.clickstatus()
        self.sp.selectstatus()
        self.sp.clickspocsubmit()
        time.sleep(10)
        self.driver.refresh()
        time.sleep(5)
        self.sp = SPOC(self.driver)
        self.sp.clickspoctab()
        time.sleep(5)
        self.driver.close()
