# 五、要求百度登录后，再定位到百度首页-设置-高级设置-首页设置，进行首页设置功能的测试。

import unittest

from time import sleep
from selenium import webdriver

from config import Config


class TestAdvancedSearchSettingsAfterLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('execute setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('execute tearDownClass')

    def setUp(self):
        print('execute setUp')
        config = Config()
        self.username = config.get_username()
        self.password = config.get_password()

        url = 'https://www.baidu.com/'
        self.browser = webdriver.Chrome(config.get_chrome_driver_path())
        self.browser.get(url)
        self.browser.maximize_window()

    def tearDown(self):
        print('execute tearDown')
        self.browser.close()

    def test_search_settings(self):
        sleep(1)
        # 点击登录按钮
        self.browser.find_element_by_id('s-top-loginbtn').click()
        sleep(2)
        # 切换至用户名密码登录
        self.browser.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        sleep(1)
        self.browser.find_element_by_id('TANGRAM__PSP_11__userName').send_keys(self.username)
        sleep(2)
        self.browser.find_element_by_id('TANGRAM__PSP_11__password').send_keys(self.password)
        sleep(2)
        # 点击登录按钮
        self.browser.find_element_by_id('TANGRAM__PSP_11__submit').submit()
        sleep(10)
        # 打开高级搜索
        self.browser.find_element_by_xpath('//*[@id="s-usersetting-top"]').click()
        sleep(3)
        self.browser.find_element_by_xpath('//*[@id="s-user-setting-menu"]/div/a[2]').click()
        sleep(2)
        self.browser.find_element_by_xpath('/html/body/div/div[6]/div/div/ul/li[3]').click()
        sleep(2)

        # 天气模块：是否展示天气预报
        self.browser.find_element_by_xpath('//*[@id="frontpage"]/div/ul/li[1]/span[2]/div/span[1]/label').click()
        sleep(2)
        # 搜索结果：搜索结果是否在新窗口打开
        self.browser.find_element_by_xpath('//*[@id="frontpage"]/div/ul/li[2]/span[2]/div/span[1]/label').click()
        sleep(2)
        # 换肤活动：是否开启换肤活动提醒
        self.browser.find_element_by_xpath('//*[@id="frontpage"]/div/ul/li[3]/span[2]/div/span[1]/label').click()
        sleep(2)

        self.browser.find_element_by_xpath('//*[@id="s_setting_savebtn"]').click()
        sleep(3)
        # 定位到弹窗，并关闭弹窗
        alert = self.browser.switch_to.alert
        alert.accept()
        sleep(3)
        # 搜索关键字，并检查是否有搜索提示
        self.browser.find_element_by_xpath('//*[@id="kw"]').send_keys("中国")
        self.browser.find_element_by_xpath('//*[@id="su"]').click()
        sleep(3)


if __name__ == '__main__':
    unittest.main()
