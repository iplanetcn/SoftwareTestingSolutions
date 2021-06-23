import unittest
from time import sleep
from selenium import webdriver

from config import Config


class TestBaidu(unittest.TestCase):
    def setUp(self):
        print('setUp')
        config = Config()
        self.browser = webdriver.Chrome(config.get_chrome_driver_path())
        self.browser.get('https://www.baidu.com/')
        self.browser.implicitly_wait(5)

    def tearDown(self):
        print('tearDown')
        self.browser.close()
        self.browser.quit()

    def test_search(self):
        # try:
            sleep(2)
            self.browser.find_element_by_id('s-usersetting-top').click()
            sleep(3)
            # print("测试通过")
        # except Exception as e:
        #     print("测试失败", format(e))


if __name__ == '__main__':
    unittest.main()
