from appium import webdriver


def init_driver():
    # 定义一个desired_caps,是一个字典
    desired_caps = {}
    # 系统
    desired_caps['platformName'] = 'Android'
    # 版本
    desired_caps['platformVersion'] = '5.0'
    # 设备号
    desired_caps['deviceName'] = '192.168.202.101:5555'
    # 包名
    desired_caps['appPackage'] = 'com.android.contacts'
    # 启动名
    desired_caps['appActivity'] = '.activities.PeopleActivity'
    # 中文输入允许
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    # 声明手机驱对象
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver

