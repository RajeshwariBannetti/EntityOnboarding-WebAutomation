import random
import string
import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.Network import Network
from pageObjects.Promoters import Promoters
from testCases.test_A_new_entity import random_generator
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def generate_random_number(length=9):
    return int(''.join([str(random.randint(6, 9))]) + ''.join([str(random.randint(0, 9)) for _ in range(length)]))


class Test_network:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    path = ".//TestData/Bank statement.pdf"
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_new_entity_login(self, setup):
        self.logger.info("************* Test_network **********")
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
        self.np = Network(self.driver)
        self.np.clickNetworkstab()
        time.sleep(5)
        self.np.clickaddnewnetwork()
        time.sleep(5)
        self.np.clickname()
        time.sleep(5)
        self.np.selectname()
        self.np.clickNetworkType()
        time.sleep(5)
        self.np.selectNetworkType()
        self.np.clickstatus()
        time.sleep(5)
        self.np.selectstatus()
        self.np.clicknetworksubmit()
        self.logger.info("************* New Network Added Successfully **********")
        self.driver.refresh()
        time.sleep(5)
        self.np.clickNetworkstab()
        time.sleep(5)
        self.np.clickaddnewstore()
        time.sleep(5)
        self.np.setstorename("Testing Two")
        self.np.clickstoretype()
        self.np.selectstoretype()
        self.np.clickstorestatus()
        self.np.selectStorestatus()
        time.sleep(3)
        self.np.clicksubmitStore()
        self.driver.refresh()
        time.sleep(5)
        self.np.clickNetworkstab()
        time.sleep(3)
        # self.driver.close()
        # self.driver.refresh()
        # time.sleep(5)
        # self.np.clickNetworkstab()
        # self.np.clickstoreEdit()
        # time.sleep(5)
        # self.np.clickEditCAdd()
        # time.sleep(5)
        # self.np.setPincode("560037")
        # time.sleep(5)
        # self.np.setState("Karnataka")
        # time.sleep(5)
        # self.np.setDistrict("Bangluru")
        # self.np.setTaluk("Bangalore South")
        # # self.np.clickpincodeok()
        # time.sleep(10)
        # self.np.setvillage("kodihalli")
        # self.np.setlandmark("Junction near")
        # self.np.setstreetaddress1("Home Bangalore")
        # self.np.setstreetaddress2("next to home")
        # self.np.clickaddresstype()
        # self.np.selectaddresstype()
        # self.np.UpdateCurrentdadd()
        # self.driver.refresh()
        # time.sleep(10)
        self.logger.info("************* New Store Details  Added Successfully **********")
        self.driver.close()
