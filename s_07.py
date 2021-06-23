# 七、要求对测试结果进行html格式报告输出，输出内容包括测试标题、测试项、测试时间、测试结果、测试截图等。可以采用HtmlTestRunner模块。
import os
import time
import unittest

from config import Config
from time import sleep
from selenium import webdriver
from HwTestReport import HTMLTestReport


class TestCaseBaidu(unittest.TestCase):
    def setUp(self):
        self.imgs = []
        self.config = Config()
        self.url = 'https://www.baidu.com'
        self.browser = webdriver.Chrome(self.config.get_chrome_driver_path())
        self.browser.get(self.url)

    def tearDown(self):
        self.browser.quit()

    def get_screenshot(self):
        self.imgs.append(self.browser.get_screenshot_as_base64())
        return True

    # 打开百度搜索，并截图
    def test_open_baidu(self):
        # 打开百度首页
        self.get_screenshot()
        sleep(3)
        # 搜索关键字，并检查是否有搜索提示
        self.browser.find_element_by_xpath('//*[@id="kw"]').send_keys("中国")
        self.browser.find_element_by_xpath('//*[@id="su"]').click()
        self.get_screenshot()
        sleep(2)
        timestamp = time.strftime('%Y%m%d_%H.%M.%S')
        img_path = os.path.join('./s_07_reports/images', '%s.png' % str(timestamp))
        self.browser.save_screenshot(img_path)
        self.get_screenshot()
        sleep(3)


if __name__ == '__main__':
    suit_01 = unittest.TestLoader().loadTestsFromTestCase(TestCaseBaidu)
    suites = unittest.TestSuite()
    suites.addTest(suit_01)

    with open('./s_07_reports/test_report.html', 'wb') as report:
        runner = HTMLTestReport(stream=report,
                                verbosity=2,
                                images=True,
                                title='HtmlTestReport自动化测试',
                                description='使用python+selenium进行自动化测试：输出内容包括测试标题、测试项、测试时间、测试结果、测试截图等。',
                                tester='测试人员')
        runner.run(suites)

    # unittest.main(
    #     testRunner=HTMLTestRunner.HTMLTestRunner(
    #         title='自动化单元测试报告',
    #         report_name='test_report',
    #         open_in_browser=True,
    #         output='s_07_reports',
    #         description='使用python+selenium进行自动化测试：输出内容包括测试标题、测试项、测试时间、测试结果、测试截图等。'))
