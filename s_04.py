# 四、定位到百度首页-设置-搜索设置，进行搜索设置功能的测试。
# 1、定位到百度首页-设置-搜索设置
# 2、编写测试用例进行测试

import unittest

from time import sleep
from selenium import webdriver

from config import Config


class TestSearchSettings(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('execute setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('execute tearDownClass')

    def setUp(self):
        print('execute setUp')
        config = Config()
        url = 'https://www.baidu.com/'
        self.browser = webdriver.Chrome(config.get_chrome_driver_path())
        self.browser.get(url)
        # self.browser.maximize_window()

    def tearDown(self):
        print('execute tearDown')
        self.browser.close()

    def test_search_settings(self):
        sleep(2)
        # 1、定位到百度首页 - 设置 - 搜索设置
        self.browser.find_element_by_id('s-usersetting-top').click()
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="s-user-setting-menu"]/div/a[1]').click()
        sleep(1)

        # 2.1、搜索框提示：是否希望在搜索时显示搜索框提示
        # 单选-不显示
        self.browser.find_element_by_xpath('//*[@id="se-settting-1"]/span[2]/label').click()
        sleep(1)
        # 单选-显示
        self.browser.find_element_by_xpath('//*[@id="se-settting-1"]/span[1]/label').click()
        sleep(1)

        # 2.2、搜索语言范围：设定您所要搜索的网页内容的语言
        # 单选-仅繁体中文
        self.browser.find_element_by_xpath('//*[@id="se-settting-2"]/span[3]/label').click()
        sleep(1)
        # 单选-仅简体中文
        self.browser.find_element_by_xpath('//*[@id="se-settting-2"]/span[2]/label').click()
        sleep(1)
        # 单选-全部语音
        self.browser.find_element_by_xpath('//*[@id="se-settting-2"]/span[1]/label').click()
        sleep(1)

        # 2.3、搜索结果显示条数：设定您希望搜索结果显示的条数
        # 单选-每页50条
        self.browser.find_element_by_xpath('//*[@id="se-setting-3"]/span[3]/label').click()
        sleep(1)
        # 单选-每页20条
        self.browser.find_element_by_xpath('//*[@id="se-setting-3"]/span[2]/label').click()
        sleep(1)
        # 单选-每页10条
        self.browser.find_element_by_xpath('//*[@id="se-setting-3"]/span[1]/label').click()
        sleep(1)

        # 2.4、实时预测功能：是否希望在您输入时实时展现搜索结果
        # 单选-关闭
        self.browser.find_element_by_xpath('//*[@id="general"]/form/div/ul/li[4]/span[2]/span[2]/label').click()
        sleep(1)
        # 单选-开启
        self.browser.find_element_by_xpath('//*[@id="general"]/form/div/ul/li[4]/span[2]/span[1]/label').click()
        sleep(1)

        # 2.5、搜索历史记录：是否希望在搜索时显示您的搜索历史
        # 单选-不显示
        self.browser.find_element_by_xpath('//*[@id="se-setting-5"]/span[2]/label').click()
        sleep(1)
        # 单选-显示
        self.browser.find_element_by_xpath('//*[@id="se-setting-5"]/span[1]/label').click()
        sleep(1)

        # 3、保存设置
        self.browser.find_element_by_xpath('//*[@id="se-setting-7"]/a[2]').click()
        sleep(2)
        # 定位到弹窗，并关闭弹窗
        alert = self.browser.switch_to.alert
        alert.accept()
        sleep(3)
        # 4、搜索关键字，并检查是否有搜索提示
        self.browser.find_element_by_xpath('//*[@id="kw"]').send_keys("中国")
        self.browser.find_element_by_xpath('//*[@id="su"]').click()
        sleep(3)


if __name__ == '__main__':
    unittest.main()
