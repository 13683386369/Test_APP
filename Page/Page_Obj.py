from Base.Base import Base
import Page
import time,allure

class Page_Obj(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def add_button(self):
        # 添加联系人按钮
        self.click_element(Page.add_btn)

    def get_user_list(self):
        # 获取联系人列表
        user_data = self.find_elements(Page.user_text)
        return [i.text for i in user_data]

    def input_people(self,name,phone):
        # 姓名
        allure.attach("描述", "输入姓名")
        self.input_elements_1(Page.add_name,name)
        # 电话
        allure.attach("描述", "输入手机号")
        self.input_elements_2(Page.add_tel,phone)
        # 保存
        #
        allure.attach("描述","点击添加页的返回按钮")
        self.click_element(Page.save_btn)
        # 判断姓名、电话不为空后点击返回
        if name != "" or phone !="":
            time.sleep(4)
            allure.attach("描述", "点击手机的返回按钮")
            self.driver.keyevent(4)




