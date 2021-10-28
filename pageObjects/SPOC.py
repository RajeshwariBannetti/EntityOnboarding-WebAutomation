class SPOC:

    tab_spoc_xpath = "//div[@id='mat-tab-label-0-3']"
    button_addnewspoc_xpath = "//mat-tab-body/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                              "1]/anchors-content-decider[1]/anchors-member-details[1]/div[1]/anchors-table[1]/div[" \
                              "1]/div[2]/div[3]/button[2] "
    textbox_spocname_xpath = "//input[@id='mat-input-1'] "
    textbox_spocemail_xpath = "//input[@id='mat-input-2']"
    textbox_spocmobile_xpath = "//input[@id='mat-input-3']"
    dropdown_department_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                                "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[1]/form[" \
                                "1]/jkf-element-builder[4]/anchors-wrapper-element[1]/anchors-select-input[1]/div[" \
                                "1]/mat-form-field[1]/div[1]/div[1] "
    list_department_xpath = "//span[contains(text(),'Sales - West')]"
    dropdown_ISPrimarySpoc_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                                   "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[" \
                                   "1]/form[1]/jkf-element-builder[5]/anchors-wrapper-element[" \
                                   "1]/anchors-select-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3] "
    list_ISPrimarySpoc_xpath = "//span[contains(text(),'No')]"
    dropdown_Status_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                            "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[1]/form[" \
                            "1]/jkf-element-builder[6]/anchors-wrapper-element[1]/anchors-select-input[1]/div[" \
                            "1]/mat-form-field[1]/div[1]/div[1]/div[3] "
    list_status_xpath = "//span[contains(text(),'Active')]"
    button_submitspoc_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                              "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[1]/div[" \
                              "1]/button[1] "

    def __init__(self, driver):
        self.driver = driver

    def clickspoctab(self):
        self.driver.find_element_by_xpath(self.tab_spoc_xpath).click()

    def clickaddnewspoc(self):
        self.driver.find_element_by_xpath(self.button_addnewspoc_xpath).click()

    def setspocname(self, spocname):
        self.driver.find_element_by_xpath(self.textbox_spocname_xpath).send_keys(spocname)

    def setspocemail(self, spocemail):
        self.driver.find_element_by_xpath(self.textbox_spocemail_xpath).send_keys(spocemail)

    def setspocmobile(self, spocmobile):
        self.driver.find_element_by_xpath(self.textbox_spocmobile_xpath).send_keys(spocmobile)

    def clickdepartment(self):
        self.driver.find_element_by_xpath(self.dropdown_department_xpath).click()

    def selectdepartment(self):
        self.driver.find_element_by_xpath(self.list_department_xpath).click()

    def clickIsprimary(self):
        self.driver.find_element_by_xpath(self.dropdown_ISPrimarySpoc_xpath).click()

    def selectISprimary(self):
        self.driver.find_element_by_xpath(self.list_ISPrimarySpoc_xpath).click()

    def clickstatus(self):
        self.driver.find_element_by_xpath(self.dropdown_Status_xpath).click()

    def selectstatus(self):
        self.driver.find_element_by_xpath(self.list_status_xpath).click()

    def clickspocsubmit(self):
        self.driver.find_element_by_xpath(self.button_submitspoc_xpath).click()
    #
    # def (self):
    #     self.driver.find_element_by_xpath()
