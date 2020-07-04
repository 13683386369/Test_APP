import pytest,sys,os
sys.path.append(".")
from Base.Init_Driver import init_driver
from Page.Page import Re_Page_Obj
from Base.Read_data import read_data
import allure

# 获取yaml文件内容
def read_yml_data():
    # 定义一个空列表
    data_list = []
    data = read_data("Test_data").get("User")
    for i in data.keys():
        data_list.append((i,data.get(i).get("name"),data.get(i).get("tel"),data.get(i).get("except")))
    return data_list

@allure.feature("新增联系人")
@allure.story("测试用例集")

class Test_Add_Contacter():
    def setup_class(self):
        self.driver = init_driver()
        self.Add_obj = Re_Page_Obj(self.driver).add_contacter()


    def teardown_class(self):
        self.driver.quit()

    @allure.severity("normal")
    @allure.testcase("http://www.baidu.com")
    @allure.issue("http://www.163.com")
    @pytest.fixture()
    def add_user_btn(self):
        # 点击添加联系人按钮
        self.Add_obj.add_button()

    @allure.severity("blocker")
    @pytest.mark.usefixtures("add_user_btn")
    @pytest.mark.parametrize("case_num,name,phone,expt",read_yml_data())
    def test_add(self,case_num,name,phone,expt):
        print("用例编号：", case_num)
        self.Add_obj.input_people(name,phone)
        # 断言
        if case_num == "test_user_001":
            assert expt not in self.Add_obj.get_user_list()
        else:
            assert expt in self.Add_obj.get_user_list()



