import random
import string
import time
from pageObjects.Entity import Entity
from pageObjects.LoginPage import LoginPage
from pageObjects.Promoters import Promoters
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def id_generator(size=15, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


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
        self.logger.info("************ Edit entity **************")
        self.ep = Entity(self.driver)
        self.ep.clickentity()
        time.sleep(5)
        self.ep.setspocname("rajeshwari BB")
        time.sleep(5)
        self.spocemail = random_generator() + "@gmail.com"
        self.ep.setspocemail(self.spocemail)
        self.ep.setspocmobilenumber("9090909089")
        self.ep.clickspocdepartment()
        self.ep.selectspocdepartment()
        self.ep.clickIsPrimaryspoc()
        self.ep.selectIsPrimaryspoc()
        self.ep.submitspoc()
        time.sleep(5)
        # self.msg = self.driver.find_element_by_tag_name("body").text
        self.logger.info("************Created New Entity **************")
        time.sleep(10)
        self.logger.info("************Add Business details **************")
        self.ep.clickeditbusinessbutton()
        time.sleep(5)
        self.ep.clickfirmtype()
        self.ep.selectfirmtype()
        self.ep.clickEntitytype()
        self.ep.selectentitytype()
        time.sleep(5)
        self.ep.setgst("23AARFV8464A1ZY")
        # self.gst = id_generator()
        # self.ep.setgst(self.gst)
        self.ep.clickokgst()
        time.sleep(10)
        self.ep.setpan("TVRPT2971P")
        self.ep.setcin("U32109KA2008PTC047065")
        self.ep.setLegalname("Rajeshwari")
        self.ep.submitbasicinfo()
        time.sleep(10)
        self.driver.refresh()
        time.sleep(10)
        self.ep.clickeditbuttonadditionaldetails()
        time.sleep(5)
        self.ep.clickoperatingmode()
        self.ep.selectoperatingmode()
        self.ep.setavgbalance("200000")
        self.ep.setmontlyincome("1000")
        self.ep.setannualincome("20000")
        self.ep.submitadditionalinfo()
        self.driver.refresh()
        time.sleep(10)
        self.ep.submitregisteredadd()
        self.ep.clickeditregadd()
        time.sleep(10)
        self.ep.setpincode("560037")
        self.ep.clickpincodeok()
        self.ep.setvillage("kodihalli")
        self.ep.setlandmark("Junction")
        self.ep.setstreetaddress1("Home")
        self.ep.setstreetaddress2("next to home")
        self.ep.clickaddresstype()
        self.ep.selectaddresstype()
        self.ep.submitregisteredadd()
        self.driver.refresh()
        time.sleep(10)
        self.ep.clickaddbankaccount()
        self.ep.setaccountnumber("123456787")
        time.sleep(5)
        self.ep.setconfirmaccountnumber("123456787")
        self.ep.setaccountholdername("Rajeshwari b")
        self.ep.setifsccode("SBIN0000813")
        time.sleep(10)
        self.ep.clickaccounttype()
        self.ep.selectaccounttype()
        self.ep.setmobilenumber("9080908080")
        self.ep.clickISPrimaryPromotor()
        self.ep.selectISParimaryPromotor()
        self.driver.refresh()
        self.pg = Promoters(self.driver)
        self.pg.clickPromoterguarantorstab()
        self.pg.clickaddnewpromoter()
        time.sleep(5)
        self.pg.setpromotername("rajeshwari B")
        self.pg.setpromoterfathername("A B")

        self.driver.close()
