from Page.Page_Obj import Page_Obj

class Re_Page_Obj():
    def __init__(self,driver):
        self.driver = driver

    def add_contacter(self):
        return Page_Obj(self.driver)

