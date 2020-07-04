from selenium.webdriver.common.by import By

"""
  通讯录元素信息

"""
# 添加联系人按钮
add_btn = (By.ID, "com.android.contacts:id/floating_action_button")
# 姓名
add_name = (By.CLASS_NAME, "android.widget.EditText")
# 电话
add_tel = (By.CLASS_NAME, "android.widget.EditText")
# 保存按钮
save_btn = (By.ID, "com.android.contacts:id/save_menu_item")
# 用户text
user_text = (By.ID, "com.android.contacts:id/cliv_name_textview")