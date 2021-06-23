# 三、定位到百度首页-登录，测试登录功能，注意多种登录方式。如有图文验证码，可设置足够长的等待时间，手动输入验证码来解决问题。 同一种登录方式全部用例应该是通过一次触发脚本就全部完成。建议采用unittest单元测试框架来组织脚本。
# 1、定位到百度首页登录
# 2、将登录方式区分成独立的测试，并编写不同的登录脚本
import time
import unittest

from selenium import webdriver
from config import Config


class TestLogin(unittest.TestCase):
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
        # 打开百度首页
        url = 'https://www.baidu.com'
        self.browser = webdriver.Chrome(config.get_chrome_driver_path())
        self.browser.get(url)
        self.browser.maximize_window()

    def tearDown(self):
        print('execute tearDown')
        self.browser.close()

    # 扫描登录
    def test_login_by_scan_qrcode(self):
        time.sleep(2)
        # 点击登录按钮
        self.browser.find_element_by_id('s-top-loginbtn').click()
        time.sleep(2)
        # 切换至扫码登录
        # self.browser.find_element_by_id('TANGRAM__PSP_11__footerQrcodeBtn').click()
        time.sleep(15)
        # 测试是否登录成功（判断是否包含用户菜单，注：用户菜单仅在登录后才会显示）
        result = self.browser.find_element_by_id('s-user-name-menu')
        self.assertTrue(result)
        self.browser.implicitly_wait(30)

    # 用户名密码登录
    def test_login_by_username_password(self):
        time.sleep(1)
        # 点击登录按钮
        self.browser.find_element_by_id('s-top-loginbtn').click()
        time.sleep(2)
        # 切换至用户名密码登录
        self.browser.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        time.sleep(1)
        self.browser.find_element_by_id('TANGRAM__PSP_11__userName').send_keys(self.username)
        time.sleep(2)
        self.browser.find_element_by_id('TANGRAM__PSP_11__password').send_keys(self.password)
        time.sleep(2)
        # 点击登录按钮
        self.browser.find_element_by_id('TANGRAM__PSP_11__submit').submit()
        time.sleep(15)
        # 测试是否登录成功（判断是否包含用户菜单，注：用户菜单仅在登录后才会显示）
        result = self.browser.find_element_by_id('s-user-name-menu')
        self.assertTrue(result)
        self.browser.implicitly_wait(30)


if __name__ == '__main__':
    unittest.main()
