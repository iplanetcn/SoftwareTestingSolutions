# 二、根据获得的excel文件，观察链接的url地址规则，根据链接前缀或后缀或关键字字符来进行链接正确性测试，写脚本。
# 1.打开excel文件，并导入url地址
# 2.通过前缀、后缀、关键字进行链接正确性测试
import unittest
from openpyxl import load_workbook
import re


# 方法：通过正则表达式进行判断，正则表达式中前缀为http(s),后缀为.com .cn, 关键字为://
def check_url_is_valid(_url):
    # language=regexp :正则表达式
    regex_rules = "^((https|http)?://)[^\s]+(com|cn)+"

    regex = re.compile(regex_rules, re.IGNORECASE)

    return regex.match(_url)


def read_urls_from_xlsx():
    workbook = load_workbook('s_01_result.xlsx')
    sheet = workbook['Sheet1']
    # 创建一个空数组，稍后将读取到的url地址放入其中
    r_urls = []
    for row in sheet.rows:
        r_urls.append(row[1].value)
    workbook.close()
    return r_urls


class TestUrls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("execute setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("execute tearDownClass")

    def setUp(self):
        print("execute setUp")

    def tearDown(self):
        print("execute tearDown")

    # 测试链接是否满足正则表达式
    def test_url_is_valid(self):
        for t_url in read_urls_from_xlsx():
            t_result = check_url_is_valid(t_url)
            self.assertTrue(t_result, f"{t_url} 为无效链接")


if __name__ == '__main__':
    # 1.打开excel文件，并导入url地址
    urls = read_urls_from_xlsx()
    # 2.通过前缀、后缀、关键字进行链接正确性测试
    for url in urls:
        if check_url_is_valid(url):
            print(f"{url} : 有效链接")
        else:
            print(f"{url} : 无效链接")

    # 可选：单元测试
    # unittest.main()
