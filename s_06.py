# 六、对百度站点针对浏览器兼容性方面的测试。思路：浏览器的种类写在配置文件里。

import unittest

from time import sleep
from selenium import webdriver
from config import Config


def compatibilityTest(_browser: webdriver):
    url = 'https://www.baidu.com/'
    _browser.get(url)
    _browser.maximize_window()
    sleep(3)
    # 搜索关键字，并检查是否有搜索提示
    _browser.find_element_by_xpath('//*[@id="kw"]').send_keys("中国")
    _browser.find_element_by_xpath('//*[@id="su"]').click()
    sleep(3)


class TestBrowserCompatibility(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('execute setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('execute tearDownClass')

    def setUp(self):
        print('execute setUp')
        self.config = Config()

    def tearDown(self):
        print('execute tearDown')
        self.browser.close()

    def test_with_chrome(self):
        self.browser = webdriver.Chrome(self.config.get_chrome_driver_path())
        compatibilityTest(self.browser)

    def test_with_firefox(self):
        self.browser = webdriver.Firefox(self.config.get_firefox_driver_path())
        compatibilityTest(self.browser)

    def test_with_edge(self):
        self.browser = webdriver.Edge(self.config.get_edge_driver_path())
        compatibilityTest(self.browser)


if __name__ == '__main__':
    unittest.main()
