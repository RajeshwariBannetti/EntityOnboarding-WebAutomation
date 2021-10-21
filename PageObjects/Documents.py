class Documents:
    tab_documents_xpath = "//div[@id='mat-tab-label-0-2']"
    link_gstdocs_id = "GST Certificate"
    docuploadgst_xpath = "//span[contains(text(),'Save')]"

    def __init__(self, driver):
        self.driver = driver

    def clickdocumentstab(self):
        self.driver.find_element_by_xpath(self.tab_documents_xpath).click()

    def clickgstdoc(self, gst):
        self.driver.find_element_by_id(self.link_gstdocs_id).send_keys(gst)

    def uploadgst(self):
        self.driver.find_element_by_xpath(self.docuploadgst_xpath).click()

    # def clickgstdoc(self, GSTCertificate):
    #     self.driver.find_element_by_xpath(self.link_gstdocs_xpath).send_keys(GSTCertificate)

    def clickpandoc(self):
        self.driver.find_element_by_xpath(self)
