class SPOC:
    tab_spoc_xpath = "//div[@id='mat-tab-label-0-3']"
    button_addnewspoc_xpath = "/html[1]/body[1]/anchors-root[1]/anchors-anchors-container[" \
                              "1]/anchors-application-details[1]/div[1]/div[3]/div[1]/mat-tab-group[1]/div[" \
                              "1]/mat-tab-body[4]/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                              "1]/anchors-content-decider[1]/anchors-member-details[1]/div[1]/anchors-table[1]/div[" \
                              "1]/div[2]/div[3]/button[2] "
    textbox_spocname_xpath = "//input[@id='en-sec-spoc-fullName']"
    textbox_spocemail_xpath = "//input[@id='en-sec-spoc-email']"
    textbox_spocmobile_xpath = "//input[@id='en-sec-spoc-mobileNumber']"
    dropdown_department_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[" \
                                "1]/section[1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[" \
                                "1]/div[1]/form[1]/jkf-element-builder[4]/anchors-wrapper-element[" \
                                "1]/anchors-select-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3]/mat-select[" \
                                "1]/div[1]/div[1] "
    list_department_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/mat-option[2]/span[1]"
    dropdown_ISPrimarySpoc_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[" \
                                   "1]/section[1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[" \
                                   "1]/div[1]/form[1]/jkf-element-builder[5]/anchors-wrapper-element[" \
                                   "1]/anchors-select-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[" \
                                   "3]/mat-select[1]/div[1]/div[1] "
    list_IsPrimarySpocYes_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/mat-option[1]/span[1]"
    list_ISPrimarySpocNo_xpath = "//span[contains(text(),'No')]"
    text_ISPrimarySpoc_xpath = "/html[1]/body[1]/div[2]/div[3]/div[1]/snack-bar-container[1]/simple-snack-bar[" \
                               "1]/span[1] "
    dropdown_Status_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                            "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[1]/form[" \
                            "1]/jkf-element-builder[6]/anchors-wrapper-element[1]/anchors-select-input[1]/div[" \
                            "1]/mat-form-field[1]/div[1]/div[1]/div[3] "
    list_status_xpath = "//span[contains(text(),'Active')]"
    button_submitspoc_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                              "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[1]/div[" \
                              "1]/button[1] "
    edit_spoc_xpath = "/html[1]/body[1]/anchors-root[1]/anchors-anchors-container[1]/anchors-application-details[" \
                      "1]/div[1]/div[3]/div[1]/mat-tab-group[1]/div[1]/mat-tab-body[4]/div[1]/div[" \
                      "1]/anchors-section-renderer[1]/div[1]/anchors-content-decider[1]/anchors-member-details[" \
                      "1]/div[1]/anchors-table[1]/div[1]/div[3]/anchors-table-card[1]/mat-card[1]/mat-card-content[" \
                      "1]/div[1]/anchors-table-base[1]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/div[1]/div[1] "

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

    def selectISprimaryYes(self):
        self.driver.find_element_by_xpath(self.list_IsPrimarySpocYes_xpath).click()

    def selectISprimaryNo(self):
        self.driver.find_element_by_xpath(self.list_ISPrimarySpocNo_xpath).click()

    def textISprimary(self):
        Textspoc = self.driver.find_element_by_xpath(self.text_ISPrimarySpoc_xpath).text
        print(Textspoc)
        return Textspoc

    def clickstatus(self):
        self.driver.find_element_by_xpath(self.dropdown_Status_xpath).click()

    def selectstatus(self):
        self.driver.find_element_by_xpath(self.list_status_xpath).click()

    def clickspocsubmit(self):
        self.driver.find_element_by_xpath(self.button_submitspoc_xpath).click()

    def editspoc(self):
        self.driver.find_element_by_xpath(self.edit_spoc_xpath).click()
    #
    # def (self):
    #     self.driver.find_element_by_xpath()
