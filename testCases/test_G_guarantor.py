import random
import string
import time

import pytest

from pageObjects.Documents import Documents
from pageObjects.Entity import Entity
from pageObjects.Guarantor import Guarantor
from pageObjects.LoginPage import LoginPage
from pageObjects.Promoters import Promoters
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def random_generatorpan(size=9, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def generate_random_adharnumber(length=11):
    return int(''.join([str(random.randint(6, 9))]) + ''.join([str(random.randint(0, 9)) for _ in range(length)]))


def generate_random_number(length=9):
    return int(''.join([str(random.randint(6, 9))]) + ''.join([str(random.randint(0, 9)) for _ in range(length)]))


def generate_random_yearnumber(length=0):
    return int(''.join([str(random.randint(1, 9))]) + ''.join([str(random.randint(0, 9)) for _ in range(length)]))


def generate_random_Date(length=0):
    return int(''.join([str(random.randint(1, 9))]) + ''.join([str(random.randint(1, 9)) for _ in range(length)]))


class Test_promoter:
    baseURLDev = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_creating_newEntity(self, setup):
        self.logger.info("************* test_creating_newEntity **********")
        self.driver = setup
        self.driver.get(self.baseURLDev)
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
        self.gp = Guarantor(self.driver)
        self.gp.clickonanyentity()
        self.driver.refresh()
        time.sleep(5)
        # self.dp = Documents(self.driver)
        # self.dp.clickdocumentstab()
        # self.dp.clicklink()
        # time.sleep(5)
        self.gp.clickguarantorstab()
        time.sleep(5)
        self.gp.clickaddnew()
        time.sleep(5)
        self.gp.setGuarantorname("R B")
        time.sleep(3)
        self.gp.setfathername("A B")
        time.sleep(3)
        self.gp.setmothername("K B")
        time.sleep(3)
        self.gp.clickMS()
        time.sleep(3)
        self.gp.selectMS()
        time.sleep(3)
        self.gp.setspouse("S A")
        time.sleep(3)
        self.promoterDOB = generate_random_Date()
        self.gp.setDOB(self.promoterDOB)
        # self.pg.setDOB("7")
        time.sleep(3)
        self.gp.clickGender()
        time.sleep(3)
        self.gp.selectGender()
        time.sleep(3)
        self.promoterpan = random_generatorpan() + "P"
        self.gp.setPancard(self.promoterpan)
        # self.gp.setPancard("AACCS2650K")
        time.sleep(3)
        # self.gp.setAadhar("276794591146")
        self.promoteradhar = generate_random_adharnumber()
        self.gp.setAadhar(self.promoteradhar)
        time.sleep(3)
        # self.gp.setEmail("")
        # self.gp.setPhoneNumber("")
        self.promoteremail = random_generator() + "@gmail.com"
        self.gp.setEmail(self.promoteremail)
        time.sleep(3)
        self.promotermobile = generate_random_number()
        self.gp.setPhoneNumber(self.promotermobile)
        time.sleep(3)
        self.gp.clickJKAccess()
        self.gp.selectJKAccess()
        self.gp.clickISPrimary()
        time.sleep(3)
        self.gp.selectISPrimary()
        time.sleep(3)
        self.gp.clickStatus()
        self.gp.selectStatus()
        self.gp.ClickSubmitStatus()
        time.sleep(5)
        self.driver.refresh()
        time.sleep(5)
        self.gp.clickguarantorstab()
        time.sleep(5)
        # @pytest.mark.regression
        # @pytest.mark.sanity
        # def test_Adding_PromoterAddress(self, setup):
        self.gp.clicklinkEditEntity()
        time.sleep(3)
        self.gp.clickEditAddress()
        time.sleep(3)
        self.gp.setpincode("560037")
        time.sleep(5)
        self.gp.setvillage("Challakere")
        time.sleep(3)
        self.gp.setlandmark("Junction")
        time.sleep(3)
        self.gp.setAdd1("1 block")
        time.sleep(3)
        self.gp.setAdd2("Near Temple")
        time.sleep(3)
        self.gp.clickAddressType()
        time.sleep(3)
        self.gp.selectAddressType()
        time.sleep(3)
        # self.pg.setYICA()
        self.promoterYearincurrentAddress = generate_random_yearnumber()
        self.gp.setYICA(self.promoterYearincurrentAddress)
        time.sleep(3)
        self.gp.clickupdate()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(5)
        self.gp.clickguarantorstab()
        time.sleep(5)
        self.driver.close()
