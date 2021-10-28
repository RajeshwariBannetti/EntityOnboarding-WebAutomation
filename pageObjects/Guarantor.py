import self


class Guarantor:
    clickon_entitytoedit_xpath = "//tbody/tr[1]/td[1]"
    tab_PromotersandGuarantors_xpath = "//div[@id='mat-tab-label-0-1']"
    button_NewGuarantor_xpath = "//span[contains(text(),'Add New Guarantor')]"
    textbox_name_xpath = "//input[@id='en-sec-guarantor-info-name']"
    textbox_fathername_xpath = "//input[@id='en-sec-guarantor-info-fatherName']"
    textbox_mothername_xpath = "//input[@id='en-sec-guarantor-info-motherName']"
    dropdown_MS_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                        "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[2]/form[" \
                        "1]/jkf-element-builder[4]/anchors-wrapper-element[1]/anchors-select-input[1]/div[" \
                        "1]/mat-form-field[1]/div[1]/div[1]/div[3] "
    list_MS_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/mat-option[2]/span[1]"
    textbox_spouse_xpath = "//input[@id='en-sec-guarantor-info-spouseName']"
    textbox_DOB_xpath = "//input[@id='en-sec-guarantor-info-dob']"
    dropdown_Gender_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                            "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[2]/form[" \
                            "1]/jkf-element-builder[7]/anchors-wrapper-element[1]/anchors-select-input[1]/div[" \
                            "1]/mat-form-field[1]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_Gender_xpath = "//span[contains(text(),'Male')]"
    textbox_pancard_xpath = "//input[@id='en-sec-guarantor-info-kyc']"
    textbox_Aadhar_xpath = "//input[@id='en-sec-guarantor-info-uidNo']"
    textbox_email_xpath = "//input[@id='en-sec-guarantor-info-email']"
    textbox_phonenumber_xpath = "//input[@id='en-sec-guarantor-info-mobileNumber']"
    dropdown_JKAccess_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[" \
                              "1]/section[1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[" \
                              "2]/form[1]/jkf-element-builder[12]/anchors-wrapper-element[1]/anchors-select-input[" \
                              "1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3] "
    list_JKAccess_xpath = "//span[contains(text(),'Yes')]"
    dropdown_ISPrimary_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[" \
                               "1]/section[1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[" \
                               "2]/form[1]/jkf-element-builder[13]/anchors-wrapper-element[1]/anchors-select-input[" \
                               "1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_ISPrimary_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/mat-option[1]/span[1]"
    dropdown_Status_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                            "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[2]/form[" \
                            "1]/jkf-element-builder[14]/anchors-wrapper-element[1]/anchors-select-input[1]/div[" \
                            "1]/mat-form-field[1]/div[1]/div[1]/div[3] "
    list_Status_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/mat-option[1]/span[1]"
    button_SubmitPromoter_xpath = "//span[contains(text(),'Submit')]"
    linkEdit_xpath = "//body[1]/anchors-root[1]/anchors-anchors-container[1]/anchors-application-details[" \
                     "1]/div[1]/div[3]/div[1]/mat-tab-group[1]/div[1]/mat-tab-body[2]/div[1]/div[" \
                     "1]/anchors-section-renderer[1]/div[1]/anchors-content-decider[" \
                     "1]/anchors-member-details[1]/div[1]/anchors-table[1]/div[1]/div[3]/anchors-table-card[" \
                     "1]/mat-card[1]/mat-card-content[1]/div[1]/anchors-table-base[1]/div[1]/table[1]/tbody[" \
                     "1]/tr[1]/td[1] "

    # Guarantor AddressDetails
    button_EditAddress_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[" \
                               "1]/section[1]/anchors-member-section[2]/anchors-forms[1]/anchors-form-builder[1]/div[" \
                               "1]/div[1]/button[1] "
    textbox_Pincode_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[" \
                            "1]/section[1]/anchors-member-section[2]/anchors-forms[1]/anchors-form-builder[" \
                            "1]/div[1]/form[1]/jkf-element-builder[1]/anchors-wrapper-element[" \
                            "1]/anchors-number-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3]/input[1] "
    textbox_village_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[" \
                            "1]/section[1]/anchors-member-section[2]/anchors-forms[1]/anchors-form-builder[" \
                            "1]/div[1]/form[1]/jkf-element-builder[5]/anchors-wrapper-element[" \
                            "1]/anchors-text-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3]/input[1] "
    textbox_Landmark_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[" \
                             "1]/section[1]/anchors-member-section[2]/anchors-forms[1]/anchors-form-builder[" \
                             "1]/div[1]/form[1]/jkf-element-builder[6]/anchors-wrapper-element[" \
                             "1]/anchors-text-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3]/input[1] "
    textbox_Add1_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[" \
                         "1]/section[1]/anchors-member-section[2]/anchors-forms[1]/anchors-form-builder[" \
                         "1]/div[1]/form[1]/jkf-element-builder[7]/anchors-wrapper-element[" \
                         "1]/anchors-text-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3]/input[1] "
    textbox_Add2_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[" \
                         "1]/section[1]/anchors-member-section[2]/anchors-forms[1]/anchors-form-builder[" \
                         "1]/div[1]/form[1]/jkf-element-builder[8]/anchors-wrapper-element[" \
                         "1]/anchors-text-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3]/input[1] "
    dropdown_AddressType_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[" \
                                 "1]/anchors-member[1]/section[1]/anchors-member-section[2]/anchors-forms[" \
                                 "1]/anchors-form-builder[1]/div[1]/form[1]/jkf-element-builder[" \
                                 "9]/anchors-wrapper-element[1]/anchors-select-input[1]/div[" \
                                 "1]/mat-form-field[1]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[1] "
    list_AdressType_xpath = "//body/div[2]/div[4]/div[1]/div[1]/div[1]/mat-option[1]/span[1]"
    textbox_YearsInCurrentAddress = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[" \
                                    "1]/anchors-member[1]/section[1]/anchors-member-section[2]/anchors-forms[" \
                                    "1]/anchors-form-builder[1]/div[1]/form[1]/jkf-element-builder[" \
                                    "10]/anchors-wrapper-element[1]/anchors-number-input[1]/div[" \
                                    "1]/mat-form-field[1]/div[1]/div[1]/div[3]/input[1] "
    button_SubmitAddressDetails_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[" \
                                        "1]/anchors-member[1]/section[1]/anchors-member-section[" \
                                        "2]/anchors-forms[1]/anchors-form-builder[1]/div[1]/div[1]/button[1] "

    # button_guarantor_xpath = "//mat-tab-body/div[1]/div[1]/anchors-section-renderer[1]/div[" \
    #                          "1]/anchors-content-decider[2]/anchors-member-details[1]/div[1]/anchors-table[1]/div[" \
    #                          "1]/div[2]/div[3]/button[2] "

    def __init__(self, driver):
        self.driver = driver

    def clickonanyentity(self):
        self.driver.find_element_by_xpath(self.clickon_entitytoedit_xpath).click()

    def clickguarantorstab(self):
        self.driver.find_element_by_xpath(self.tab_PromotersandGuarantors_xpath).click()

    def clickaddnew(self):
        self.driver.find_element_by_xpath(self.button_NewGuarantor_xpath).click()

    def setGuarantorname(self, Guarantorname):
        self.driver.find_element_by_xpath(self.textbox_name_xpath).send_keys(Guarantorname)

    def setfathername(self, Guarantorfather):
        self.driver.find_element_by_xpath(self.textbox_fathername_xpath).send_keys(Guarantorfather)

    def setmothername(self, promotermothername):
        self.driver.find_element_by_xpath(self.textbox_mothername_xpath).send_keys(promotermothername)

    def clickMS(self):
        self.driver.find_element_by_xpath(self.dropdown_MS_xpath).click()

    def selectMS(self):
        self.driver.find_element_by_xpath(self.list_MS_xpath).click()

    def setspouse(self, spouse):
        self.driver.find_element_by_xpath(self.textbox_spouse_xpath).send_keys(spouse)

    def setDOB(self, DOB):
        self.driver.find_element_by_xpath(self.textbox_DOB_xpath).send_keys(DOB)

    def clickGender(self):
        self.driver.find_element_by_xpath(self.dropdown_Gender_xpath).click()

    def selectGender(self):
        self.driver.find_element_by_xpath(self.list_Gender_xpath).click()

    def setPancard(self, Pancard):
        self.driver.find_element_by_xpath(self.textbox_pancard_xpath).send_keys(Pancard)

    def setAadhar(self, Aadhar):
        self.driver.find_element_by_xpath(self.textbox_Aadhar_xpath).send_keys(Aadhar)

    def setEmail(self, Email):
        self.driver.find_element_by_xpath(self.textbox_email_xpath).send_keys(Email)

    def setPhoneNumber(self, PhoneNumber):
        self.driver.find_element_by_xpath(self.textbox_phonenumber_xpath).send_keys(PhoneNumber)

    def clickJKAccess(self):
        self.driver.find_element_by_xpath(self.dropdown_JKAccess_xpath).click()

    def selectJKAccess(self):
        self.driver.find_element_by_xpath(self.list_JKAccess_xpath).click()

    def clickISPrimary(self):
        self.driver.find_element_by_xpath(self.dropdown_ISPrimary_xpath).click()

    def selectISPrimary(self):
        self.driver.find_element_by_xpath(self.list_ISPrimary_xpath).click()

    def clickStatus(self):
        self.driver.find_element_by_xpath(self.dropdown_Status_xpath).click()

    def selectStatus(self):
        self.driver.find_element_by_xpath(self.list_Status_xpath).click()

    def ClickSubmitStatus(self):
        self.driver.find_element_by_xpath(self.button_SubmitPromoter_xpath).click()

    def clicktab(self):
        self.driver.find_element_by_xpath(self.tab_PromotersandGuarantors_xpath).click()

    def clicklinkEditEntity(self):
        self.driver.find_element_by_xpath(self.linkEdit_xpath).click()

    def clickEditAddress(self):
        self.driver.find_element_by_xpath(self.button_EditAddress_xpath).click()

    def setpincode(self, pincode):
        self.driver.find_element_by_xpath(self.textbox_Pincode_xpath).send_keys(pincode)

    def setvillage(self, village):
        self.driver.find_element_by_xpath(self.textbox_village_xpath).send_keys(village)

    def setlandmark(self, landmark):
        self.driver.find_element_by_xpath(self.textbox_Landmark_xpath).send_keys(landmark)

    def setAdd1(self, Add1):
        self.driver.find_element_by_xpath(self.textbox_Add1_xpath).send_keys(Add1)

    def setAdd2(self, Add2):
        self.driver.find_element_by_xpath(self.textbox_Add2_xpath).send_keys(Add2)

    def clickAddressType(self):
        self.driver.find_element_by_xpath(self.dropdown_AddressType_xpath).click()

    def selectAddressType(self):
        self.driver.find_element_by_xpath(self.list_AdressType_xpath).click()

    def setYICA(self, YICA):
        self.driver.find_element_by_xpath(self.textbox_YearsInCurrentAddress).send_keys(YICA)

    def clickupdate(self):
        self.driver.find_element_by_xpath(self.button_SubmitAddressDetails_xpath).click()
