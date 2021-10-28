class Documents:
    tab_documents_xpath = "//div[@id='mat-tab-label-0-2']"
    doc_CertificateofIncorporation_id = "Certificate of Incorporation"
    doc_gstdocs_id = "GST Certificate"
    doc_CompanyPANCard_id = "Company PAN Card"
    doc_Memorandum_id = "Memorandum of Association"
    text_Memorandum_xpath = "//mat-tab-body/div[1]/div[1]/anchors-section-renderer[1]/div[1]/anchors-content-decider[" \
                            "1]/anchors-documents[1]/section[1]/div[3]/anchors-document[4]/div[1]/div[1] "
    doc_Articles_id = "Articles of Association"
    text_Articles_xpath = "/html[1]/body[1]/anchors-root[1]/anchors-anchors-container[1]/anchors-application-details[" \
                          "1]/div[1]/div[3]/div[1]/mat-tab-group[1]/div[1]/mat-tab-body[3]/div[1]/div[" \
                          "1]/anchors-section-renderer[1]/div[1]/anchors-content-decider[1]/anchors-documents[" \
                          "1]/section[1]/div[3]/anchors-document[5]/div[1]/div[1] "
    doc_GSTBill12months_id = "GST Bill 12 months"
    doc_AuditedFinancials3Years_id = "Audited Financials 3 Years"
    doc_LedgersUpload_id = "Ledgers Upload"
    doc_Agreement_id = "Agreement"
    doc_UdyogAadhaar_id = "Udyog Aadhaar"
    doc_ShopActLicense_id = "Shop Act License"
    doc_ChannelLogo_id = "Channel Logo"
    doc_AuditReport_id = "Audit Report"
    doc_ITRDocuments_id = "ITR Documents"
    doc_BoardResolutionDocument_id = "Board Resolution Document"
    doc_DealershipCertificate_id = "Dealership Certificate"
    doc_save_xpath = "//span[contains(text(),'Save')]"
    button_AddDoc_xpath = "/html[1]/body[1]/anchors-root[1]/anchors-anchors-container[1]/anchors-application-details[" \
                          "1]/div[1]/div[3]/div[1]/mat-tab-group[1]/div[1]/mat-tab-body[3]/div[1]/div[" \
                          "1]/anchors-section-renderer[1]/div[1]/anchors-content-decider[1]/anchors-documents[" \
                          "1]/section[1]/div[2]/button[1] "

    def __init__(self, driver):
        self.driver = driver

    def clickdocumentstab(self):
        self.driver.find_element_by_xpath(self.tab_documents_xpath).click()

    def clickAddDoc(self):
        self.driver.find_element_by_xpath(self.button_AddDoc_xpath).click()

    def uploadCertificateofIncorporation(self, Certificate):
        self.driver.find_element_by_id(self.doc_CertificateofIncorporation_id).send_keys(Certificate)

    def uploadgst(self, gst):
        self.driver.find_element_by_id(self.doc_gstdocs_id).send_keys(gst)

    def uploadgst1(self, gst1):
        self.driver.find_element_by_id(self.doc_gstdocs_id).send_keys(gst1)

    def uploadCompanyPANCard(self, PANCard):
        self.driver.find_element_by_id(self.doc_CompanyPANCard_id).send_keys(PANCard)

    def MemorandumText(self):
        Text = self.driver.find_element_by_xpath(self.text_Memorandum_xpath).text
        print(Text)
        return Text

    def uploadMemorandum(self, Memorandum):
        self.driver.find_element_by_id(self.doc_Memorandum_id).send_keys(Memorandum)

    def ArticlesText(self):
        Text = self.driver.find_element_by_xpath(self.text_Articles_xpath).text
        print(Text)
        return Text

    def upoadArticles(self, Articles):
        self.driver.find_element_by_id(self.doc_Articles_id).send_keys(Articles)

    def uploadGSTBill12months(self, GST):
        self.driver.find_element_by_id(self.doc_GSTBill12months_id).send_keys(GST)

    def uploadAuditedFinancials3Years(self, AuditedFinancials3Years):
        self.driver.find_element_by_id(self.doc_AuditedFinancials3Years_id).send_keys(AuditedFinancials3Years)

    def uploadLenders(self, Ledgers):
        self.driver.find_element_by_id(self.doc_LedgersUpload_id).send_keys(Ledgers)

    def uploadAgreement(self, Agreement):
        self.driver.find_element_by_id(self.doc_Agreement_id).send_keys(Agreement)

    def uploadUdyogAadhaar(self, UdyogAadhaar):
        self.driver.find_element_by_id(self.doc_UdyogAadhaar_id).send_keys(UdyogAadhaar)

    def uploadShopActLicense(self, ShopActLicense):
        self.driver.find_element_by_id(self.doc_ShopActLicense_id).send_keys(ShopActLicense)

    def uploadChannelLogo(self, ChannelLogo):
        self.driver.find_element_by_id(self.doc_ChannelLogo_id).send_keys(ChannelLogo)

    def uploadAuditReport(self, AuditReport):
        self.driver.find_element_by_id(self.doc_AuditReport_id).send_keys(AuditReport)

    def uploadITRDocuments(self, ITRDocuments):
        self.driver.find_element_by_id(self.doc_ITRDocuments_id).send_keys(ITRDocuments)

    def uploadBoardResolutionDocument(self, BoardResolutionDocument):
        self.driver.find_element_by_id(self.doc_BoardResolutionDocument_id).send_keys(BoardResolutionDocument)

    def uploadDealershipCertificate(self, DealershipCertificate):
        self.driver.find_element_by_id(self.doc_DealershipCertificate_id).send_keys(DealershipCertificate)

    # def clickgstdoc(self, GSTCertificate):
    #     self.driver.find_element_by_xpath(self.link_gstdocs_xpath).send_keys(GSTCertificate)

    def docSave(self):
        self.driver.find_element_by_xpath(self.doc_save_xpath).click()
