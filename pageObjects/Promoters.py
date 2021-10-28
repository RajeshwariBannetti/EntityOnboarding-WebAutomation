class Promoters:
    clickon_entitytoedit_xpath = "//tbody/tr[1]/td[1]"
    tab_PromotersandGuarantors_xpath = "//div[contains(text(),'Promoters / Guarantors')]"
    button_NewPromoter_xpath = "/html[1]/body[1]/anchors-root[1]/anchors-anchors-container[" \
                               "1]/anchors-application-details[1]/div[1]/div[3]/div[1]/mat-tab-group[1]/div[" \
                               "1]/mat-tab-body[2]/div[1]/div[1]/anchors-section-renderer[1]/div[" \
                               "1]/anchors-content-decider[1]/anchors-member-details[1]/div[1]/anchors-table[1]/div[" \
                               "1]/div[2]/div[3]/button[2]/span[1] "
    textbox_promotername_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[" \
                                 "1]/section[1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[" \
                                 "1]/div[2]/form[1]/jkf-element-builder[1]/anchors-wrapper-element[" \
                                 "1]/anchors-text-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3]/input[1] "
    textbox_name_xpath = "//input[@id='en-sec-key-personnel-info-name']"
    textbox_fathername_xpath = "//input[@id='en-sec-key-personnel-info-fatherName']"
    textbox_mothername_xpath = "//input[@id='en-sec-key-personnel-info-motherName']"
    dropdown_MS_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                        "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[2]/form[" \
                        "1]/jkf-element-builder[4]/anchors-wrapper-element[1]/anchors-select-input[1]/div[" \
                        "1]/mat-form-field[1]/div[1]/div[1]/div[3] "
    list_MS_xpath = "//span[contains(text(),'Unmarried')]"
    textbox_DOB_xpath = "//input[@id='en-sec-key-personnel-info-dob']"
    dropdown_Gender_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                            "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[2]/form[" \
                            "1]/jkf-element-builder[7]/anchors-wrapper-element[1]/anchors-select-input[1]/div[" \
                            "1]/mat-form-field[1]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_Gender_xpath = "//span[contains(text(),'Female')]"
    textbox_pancard_xpath = "//input[@id='en-sec-key-personnel-info-kyc']"
    textbox_Aadhar_xpath = "//input[@id='en-sec-key-personnel-info-uidNo']"
    textbox_email_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                          "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[2]/form[" \
                          "1]/jkf-element-builder[10]/anchors-wrapper-element[1]/anchors-text-input[1]/div[" \
                          "1]/mat-form-field[1]/div[1]/div[1]/div[3]/input[1] "
    textbox_phonenumber_xpath = "//input[@id='en-sec-key-personnel-info-mobileNumber']"
    dropdown_JKAccess_xpath = "//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                              "1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[1]/div[2]/form[" \
                              "1]/jkf-element-builder[12]/anchors-wrapper-element[1]/anchors-select-input[1]/div[" \
                              "1]/mat-form-field[1]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_JKAccess_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/mat-option[1]/span[1]"
    dropdown_ISPrimaryPromoter_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[" \
                                       "1]/section[1]/anchors-member-section[1]/anchors-forms[" \
                                       "1]/anchors-form-builder[1]/div[2]/form[1]/jkf-element-builder[" \
                                       "13]/anchors-wrapper-element[1]/anchors-select-input[1]/div[1]/mat-form-field[" \
                                       "1]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_ISPrimaryPromoterYES_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/mat-option[1]/span[1]"
    text_ISPrimaryPromoter_xpath = "//span[contains(text(),'Only a Single Promoter can be marked as Primary.')]"
    list_ISPrimaryPromoterNO_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/mat-option[2]/span[1]"
    dropdown_PromoterStatus_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[" \
                                    "1]/section[1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[" \
                                    "1]/div[2]/form[1]/jkf-element-builder[14]/anchors-wrapper-element[" \
                                    "1]/anchors-select-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[" \
                                    "3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_PromoterStatusActive_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/mat-option[1]/span[1]"
    list_PromoterStatusInactive_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/mat-option[" \
                                        "2]/span[1] "
    button_SubmitPromoter_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[" \
                                  "1]/section[1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[" \
                                  "1]/div[2]/div[1]/button[1] "
    linkPromoterEdit_xpath = "//div[contains(text(),'Test B')]"

    # Promoter AddressDetails
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
    button_editcurrentAdd_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[" \
                                  "1]/section[1]/anchors-member-section[3]/anchors-forms[1]/anchors-form-builder[" \
                                  "1]/div[1]/div[1]/button[1]/span[1] "
    toggle_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[1]/section[" \
                   "1]/anchors-member-section[3]/anchors-forms[1]/anchors-form-builder[1]/div[1]/mat-slide-toggle[" \
                   "1]/label[1]/div[1] "
    button_update_xpath = "//span[contains(text(),'Update')]"

    # button_guarantor_xpath = "//mat-tab-body/div[1]/div[1]/anchors-section-renderer[1]/div[" \
    #                          "1]/anchors-content-decider[2]/anchors-member-details[1]/div[1]/anchors-table[1]/div[" \
    #                          "1]/div[2]/div[3]/button[2] "

    # Documents
    upload_doc_photo_id = "Profile Photo"
    upload_doc_aadharFront_id = "Aadhar Card Front"
    upload_doc_aadharBack_id = "Aadhar Card Back"
    upload_doc_adressProof_id = "Address Proof"
    upload_doc_KYCDoc_id = "KYC Doc"
    upload_doc_CACertifiedNetWorth_id = "CA Certified NetWorth"
    upload_save_xpath = "//span[contains(text(),'Save')]"

    # Bank Details
    button_addBankAccount_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/anchors-member[" \
                                  "1]/section[1]/anchors-member-section[5]/anchors-member-details[1]/div[" \
                                  "1]/anchors-table[1]/div[1]/div[2]/div[3]/button[2]/span[1] "
    textbox_AccNumber_xpath = "//input[@id='en-sec-promoters-acc-info-accNumber']"
    textbox_ConfirmAccNumber_xpath = "//input[@id='en-sec-promoters-acc-info-accNumberC']"
    textbox_AccholderName_xpath = "//input[@id='en-sec-promoters-acc-info-accountHolderName']"
    textbox_IFSC_xpath = "//input[@id='en-sec-promoters-acc-info-ifsc']"
    dropdown_AccountType_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/mat-dialog-container[1]/anchors-member[" \
                                 "1]/section[1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[" \
                                 "1]/div[1]/form[1]/jkf-element-builder[8]/anchors-wrapper-element[" \
                                 "1]/anchors-select-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[" \
                                 "3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_AccountTypeCurr_xpath = "/html[1]/body[1]/div[2]/div[6]/div[1]/div[1]/div[1]/mat-option[1]/span[1]"
    list_AccountTypeSaving_xpath = "/html[1]/body[1]/div[2]/div[6]/div[1]/div[1]/div[1]/mat-option[2]/span[1]"
    textbox_Mobilenumber_xpath = "//input[@id='en-sec-promoters-acc-info-mobileNumber']"
    dropdown_ISPrimaryAcc_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/mat-dialog-container[1]/anchors-member[" \
                                  "1]/section[1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[" \
                                  "1]/div[1]/form[1]/jkf-element-builder[10]/anchors-wrapper-element[" \
                                  "1]/anchors-select-input[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[" \
                                  "3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_ISPrimaryAccYes_xpath = "/html[1]/body[1]/div[2]/div[6]/div[1]/div[1]/div[1]/mat-option[1]/span[1]"
    list_ISPrimaryAccNo_xpath = "/html[1]/body[1]/div[2]/div[6]/div[1]/div[1]/div[1]/mat-option[2]/span[1]"
    dropdown_ISPrimaryAccStatus_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/mat-dialog-container[" \
                                        "1]/anchors-member[1]/section[1]/anchors-member-section[1]/anchors-forms[" \
                                        "1]/anchors-form-builder[1]/div[1]/form[1]/jkf-element-builder[" \
                                        "11]/anchors-wrapper-element[1]/anchors-select-input[1]/div[" \
                                        "1]/mat-form-field[1]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[1]/span[1] "
    list_ISPrimaryAccStatusActive_xpath = "/html[1]/body[1]/div[2]/div[6]/div[1]/div[1]/div[1]/mat-option[1]/span[1]"
    list_ISPrimaryAccStatusInactive_xpath = "/html[1]/body[1]/div[2]/div[6]/div[1]/div[1]/div[1]/mat-option[2]/span[1]"
    button_SubmitBankAccount_xpath = "/html[1]/body[1]/div[2]/div[4]/div[1]/mat-dialog-container[1]/anchors-member[" \
                                     "1]/section[1]/anchors-member-section[1]/anchors-forms[1]/anchors-form-builder[" \
                                     "1]/div[1]/div[1]/button[1]/span[1] "

    def __init__(self, driver):
        self.driver = driver

    def clickonanyentity(self):
        self.driver.find_element_by_xpath(self.clickon_entitytoedit_xpath).click()

    def clickPromoterguarantorstab(self):
        self.driver.find_element_by_xpath(self.tab_PromotersandGuarantors_xpath).click()

    def clickaddnewpromoter(self):
        self.driver.find_element_by_xpath(self.button_NewPromoter_xpath).click()

    def setpromotername(self, promotername):
        self.driver.find_element_by_xpath(self.textbox_name_xpath).send_keys(promotername)

    def setpromoterfathername(self, promoterfamathername):
        self.driver.find_element_by_xpath(self.textbox_fathername_xpath).send_keys(promoterfamathername)

    def setpromotermothername(self, promotermothername):
        self.driver.find_element_by_xpath(self.textbox_mothername_xpath).send_keys(promotermothername)

    def clickMS(self):
        self.driver.find_element_by_xpath(self.dropdown_MS_xpath).click()

    def selectMS(self):
        self.driver.find_element_by_xpath(self.list_MS_xpath).click()

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

    def clickISPrimaryPromoter(self):
        self.driver.find_element_by_xpath(self.dropdown_ISPrimaryPromoter_xpath).click()

    def selectISPrimaryPromoterYES(self):
        self.driver.find_element_by_xpath(self.list_ISPrimaryPromoterYES_xpath).click()

    def selectISPrimaryPromoterNO(self):
        self.driver.find_element_by_xpath(self.list_ISPrimaryPromoterNO_xpath).click()

    def textISPrimaryPromoter(self):
        TextPromoter = self.driver.find_element_by_xpath(self.text_ISPrimaryPromoter_xpath).click()
        print(TextPromoter)
        return TextPromoter

    def clickPromoterStatus(self):
        self.driver.find_element_by_xpath(self.dropdown_PromoterStatus_xpath).click()

    def selectPromoterStatusActive(self):
        self.driver.find_element_by_xpath(self.list_PromoterStatusActive_xpath).click()

    def selectPromoterStatusInactive(self):
        self.driver.find_element_by_xpath(self.list_PromoterStatusInactive_xpath).click()

    def ClickSubmitPromoterStatus(self):
        self.driver.find_element_by_xpath(self.button_SubmitPromoter_xpath).click()

    def clicklinkEditEntity(self):
        self.driver.find_element_by_xpath(self.linkPromoterEdit_xpath).click()

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

    def clickcurr(self):
        self.driver.find_element_by_xpath(self.button_editcurrentAdd_xpath).click()

    def click(self):
        self.driver.find_element_by_xpath(self.toggle_xpath).click()

    def update(self):
        self.driver.find_element_by_xpath(self.button_update_xpath).click()

    def uploadsave(self):
        self.driver.find_element_by_xpath(self.upload_save_xpath).click()

    def uploadphoto(self, photo):
        self.driver.find_element_by_id(self.upload_doc_photo_id).send_keys(photo)

    def uploadaadharfront(self, aadharfront):
        self.driver.find_element_by_id(self.upload_doc_aadharFront_id).send_keys(aadharfront)

    def uploadaadharback(self, aadharback):
        self.driver.find_element_by_id(self.upload_doc_aadharBack_id).send_keys(aadharback)

    def uploadaddressproof(self, addressproof):
        self.driver.find_element_by_id(self.upload_doc_adressProof_id).send_keys(addressproof)

    def uploadKYCDoc(self, KYCDoc):
        self.driver.find_element_by_id(self.upload_doc_KYCDoc_id).send_keys(KYCDoc)

    def uploadCACertifiedNetWorth(self, CACertifiedNetWorth):
        self.driver.find_element_by_id(self.upload_doc_CACertifiedNetWorth_id).send_keys(CACertifiedNetWorth)

    def ClickAddBankDetails(self):
        self.driver.find_element_by_xpath(self.button_addBankAccount_xpath).click()

    def setAccNumber(self, AccNumber):
        self.driver.find_element_by_xpath(self.textbox_AccNumber_xpath).send_keys(AccNumber)

    def setConfirmAccNumber(self, ConfirmAccNumber):
        self.driver.find_element_by_xpath(self.textbox_ConfirmAccNumber_xpath).send_keys(ConfirmAccNumber)

    def setAccHolderName(self, AccHolderName):
        self.driver.find_element_by_xpath(self.textbox_AccholderName_xpath).send_keys(AccHolderName)

    def setIFSC(self, IFSC):
        self.driver.find_element_by_xpath(self.textbox_IFSC_xpath).send_keys(IFSC)

    def clickAccType(self):
        self.driver.find_element_by_xpath(self.dropdown_AccountType_xpath).click()

    def selectAccTypeCurr(self):
        self.driver.find_element_by_xpath(self.list_AccountTypeCurr_xpath).click()

    def selectAccTypeSaving(self):
        self.driver.find_element_by_xpath(self.list_AccountTypeSaving_xpath).click()

    def SetMobileNumber(self, MobileNumber):
        self.driver.find_element_by_xpath(self.textbox_Mobilenumber_xpath).send_keys(MobileNumber)

    def clickISPrimayAcc(self):
        self.driver.find_element_by_xpath(self.dropdown_ISPrimaryAcc_xpath).click()

    def selectISPrimaryAccYes(self):
        self.driver.find_element_by_xpath(self.list_ISPrimaryAccYes_xpath).click()

    def selectISPrimaryAccNo(self):
        self.driver.find_element_by_xpath(self.list_ISPrimaryAccNo_xpath).click()

    def clickISPrimaryAccStatus(self):
        self.driver.find_element_by_xpath(self.dropdown_ISPrimaryAccStatus_xpath).click()

    def selectISPrimaryAccStatusActive(self):
        self.driver.find_element_by_xpath(self.list_ISPrimaryAccStatusActive_xpath).click()

    def selectISPrimaryAccStatusInactive(self):
        self.driver.find_element_by_xpath(self.list_ISPrimaryAccStatusInactive_xpath).click()

    def submitBankAccount(self):
        self.driver.find_element_by_xpath(self.button_SubmitBankAccount_xpath).click()
