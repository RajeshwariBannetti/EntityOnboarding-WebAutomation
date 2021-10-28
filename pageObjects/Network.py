class Network:
    tab_network_xpath = "//div[@id='mat-tab-label-0-4']"
    button_addNewNetwork_xpath = "//mat-tab-body/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                                 "1]/anchors-content-decider[1]/anchors-member-details[1]/div[1]/anchors-table[" \
                                 "1]/div[1]/div[2]/div[3]/button[2] "
    dropdown_Name_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                          "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[1]/form[" \
                          "1]/jkf-element-builder[1]/anchors-wrapper-element[1]/anchors-select-input[1]/div[" \
                          "1]/mat-form-field[1]/div[1]/div[1] "
    list_name_xpath = "//span[contains(text(),'Bharat Petroleum Corporation Limited')]"
    dropdown_NetworkType_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                                 "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[1]/form[" \
                                 "1]/jkf-element-builder[2]/anchors-wrapper-element[1]/anchors-select-input[1]/div[" \
                                 "1]/mat-form-field[1]/div[1]/div[1]/div[3] "
    list_NetworkTpe_xpath = "//span[contains(text(),'Seller')]"
    dropdown_Status_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                            "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[1]/form[" \
                            "1]/jkf-element-builder[3]/anchors-wrapper-element[1]/anchors-select-input[1]/div[" \
                            "1]/mat-form-field[1]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_Status_xpath = "//body/div[2]/div[4]/div[1]/div[1]/div[1]/mat-option[1]/span[1]"
    button_submitnetwork_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                                 "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[1]/div[" \
                                 "1]/button[1] "
    button_Addnewstore_xpath = "//span[contains(text(),'Add New Store')]"
    textbox_storename_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[" \
                              "1]/section[1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[" \
                              "1]/form[1]/jkf-element-builder[1]/anchors-wrapper-element[1]/anchors-text-input[" \
                              "1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3]/input[1] "
    dropdown_storeType_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[" \
                               "1]/section[1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[" \
                               "1]/form[1]/jkf-element-builder[2]/anchors-wrapper-element[1]/anchors-select-input[" \
                               "1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_storetype_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/mat-option[1]/span[1]"
    dropdownstorestatus_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[" \
                                "1]/section[1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[" \
                                "1]/div[1]/form[1]/jkf-element-builder[3]/anchors-wrapper-element[" \
                                "1]/anchors-select-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3]/mat-select[" \
                                "1]/div[1]/div[1]/span[1] "
    list_storestatus_xpath = "//span[contains(text(),'Active')]"
    button_submitStore_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[" \
                               "1]/section[1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[" \
                               "1]/div[1]/button[1] "
    link_ToEditStorename_xpath = "//body[1]/anchors-root[1]/anchors-anchors-container[1]/anchors-application-details[" \
                                 "1]/div[1]/div[3]/div[1]/mat-tab-group[1]/div[1]/mat-tab-body[5]/div[1]/div[" \
                                 "1]/anchors-section-renderer[1]/div[1]/anchors-content-decider[" \
                                 "2]/anchors-member-details[1]/div[1]/anchors-table[1]/div[1]/div[" \
                                 "3]/anchors-table-card[1]/mat-card[1]/mat-card-content[1]/div[1]/anchors-table-base[" \
                                 "1]/div[1]/table[1]/tbody[1]/tr[1]/td[1] "
    button_editCAdd_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                            "1]/anchors-member-section[2]/anchors-forms[1]/anchors-form-builder[1]/div[1]/div[" \
                            "1]/button[1] "
    textbox_pincode_xpath = "//input[@id='mat-input-3']"
    # button_pincode_xpath = "//span[contains(text(),'OK')]"
    textbox_ra_EnterState_xpath = "//input[@id='mat-input-4']"
    textbox_ra_EnterDistrict_xpath = "//input[@id='mat-input-5']"
    textbox_ra_EnterTaluka_xpath = "//input[@id='mat-input-6']"
    textbox_village_xpath = "//input[@id='mat-input-7']"
    textbox_Landmark_xpath = "//input[@id='mat-input-8']"
    textbox_streetaddress1_xpath = "//input[@id='mat-input-9']"
    textbox_streetaddress2_xpath = "//input[@id='mat-input-10']"
    dropdownlist_Addresstype_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                                     "1]/anchors-member-section[2]/anchors-forms[1]/anchors-form-builder[1]/div[" \
                                     "1]/form[1]/jkf-element-builder[9]/anchors-wrapper-element[" \
                                     "1]/anchors-select-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[" \
                                     "3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_addresstype_rented_xpath = "//span[contains(text(),'Rented')]"
    textbox_YearsInCurrentAdd_xpath = "//input[@id='mat-input-11']"
    # textbox_latitude_xpath = ""
    # textbox_longitude_xpath = ""
    button_UpdateCurrentadd_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                                    "1]/anchors-member-section[2]/anchors-forms[1]/anchors-form-builder[1]/div[" \
                                    "1]/div[1]/button[1] "

    def __init__(self, driver):
        self.driver = driver

    def clickNetworkstab(self):
        self.driver.find_element_by_xpath(self.tab_network_xpath).click()

    def clickaddnewnetwork(self):
        self.driver.find_element_by_xpath(self.button_addNewNetwork_xpath).click()

    def clickname(self):
        self.driver.find_element_by_xpath(self.dropdown_Name_xpath).click()

    def selectname(self):
        self.driver.find_element_by_xpath(self.list_name_xpath).click()

    def clickNetworkType(self):
        self.driver.find_element_by_xpath(self.dropdown_NetworkType_xpath).click()

    def selectNetworkType(self):
        self.driver.find_element_by_xpath(self.list_NetworkTpe_xpath).click()

    def clickstatus(self):
        self.driver.find_element_by_xpath(self.dropdown_Status_xpath).click()

    def selectstatus(self):
        self.driver.find_element_by_xpath(self.list_Status_xpath).click()

    def clicknetworksubmit(self):
        self.driver.find_element_by_xpath(self.button_submitnetwork_xpath).click()

    def clickaddnewstore(self):
        self.driver.find_element_by_xpath(self.button_Addnewstore_xpath).click()

    def setstorename(self, storename):
        self.driver.find_element_by_xpath(self.textbox_storename_xpath).send_keys(storename)

    def clickstoretype(self):
        self.driver.find_element_by_xpath(self.dropdown_storeType_xpath).click()

    def selectstoretype(self):
        self.driver.find_element_by_xpath(self.list_storetype_xpath).click()

    def clickstorestatus(self):
        self.driver.find_element_by_xpath(self.dropdownstorestatus_xpath).click()

    def selectStorestatus(self):
        self.driver.find_element_by_xpath(self.list_storestatus_xpath).click()

    def clicksubmitStore(self):
        self.driver.find_element_by_xpath(self.button_submitStore_xpath).click()

    def clickstoreEdit(self):
        self.driver.find_element_by_xpath(self.link_ToEditStorename_xpath).click()

    def clickEditCAdd(self):
        self.driver.find_element_by_xpath(self.button_editCAdd_xpath).click()

    def setPincode(self, pincode):
        self.driver.find_element_by_xpath(self.textbox_pincode_xpath).send_keys(pincode)

    # def clickpincodeok(self):
    #     self.driver.find_element_by_xpath(self.button_pincode_xpath).click()

    def setState(self, State):
        self.driver.find_element_by_xpath(self.textbox_ra_EnterState_xpath).send_keys(State)

    def setDistrict(self, District):
        self.driver.find_element_by_xpath(self.textbox_ra_EnterDistrict_xpath).send_keys(District)

    def setTaluk(self, Taluk):
        self.driver.find_element_by_xpath(self.textbox_ra_EnterTaluka_xpath).send_keys(Taluk)

    def setvillage(self, village):
        self.driver.find_element_by_xpath(self.textbox_village_xpath).send_keys(village)

    def setlandmark(self, landmark):
        self.driver.find_element_by_xpath(self.textbox_Landmark_xpath).send_keys(landmark)

    def setstreetaddress1(self, streetaddress1):
        self.driver.find_element_by_xpath(self.textbox_streetaddress1_xpath).send_keys(streetaddress1)

    def setstreetaddress2(self, streetaddress2):
        self.driver.find_element_by_xpath(self.textbox_streetaddress2_xpath).send_keys(streetaddress2)

    def clickaddresstype(self):
        self.driver.find_element_by_xpath(self.dropdownlist_Addresstype_xpath).click()

    def selectaddresstype(self):
        self.driver.find_element_by_xpath(self.list_addresstype_rented_xpath).click()

    def UpdateCurrentdadd(self):
        self.driver.find_element_by_xpath(self.button_UpdateCurrentadd_xpath).click()
