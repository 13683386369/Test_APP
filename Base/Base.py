from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self,driver):
        self.driver = driver

    def find_element(self,loc,timeout=10,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x: x.find_element(*loc))


    def find_elements(self,loc,timeout=10,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x: x.find_elements(*loc))

    # 输入
    def input_element(self,loc,text):
        self.find_element(loc).send_keys(text)

    # 点击
    def click_element(self,loc):
        self.find_element(loc).click()

    def input_elements_1(self,loc,text1):
        ele = self.find_elements(loc)[0]
        ele.clear()
        ele.send_keys(text1)


    def input_elements_2(self,loc,text2):
        ele = self.find_elements(loc)[1]
        ele.clear()
        ele.send_keys(text2)