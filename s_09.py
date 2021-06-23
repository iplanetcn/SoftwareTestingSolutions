# 九、写测试日志脚本（10分），Python中有一个logging模块来支持我们自定义封装一个新日志类。日志格式自拟。
import unittest
from s_09_logs import Logs

# 初始化log
log = Logs()


class TestSomething(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('execute setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('execute tearDownClass')

    def setUp(self):
        log.d('execute setUp')

    def tearDown(self):
        log.d('execute tearDown')

    def test_case(self):
        """ This test should be skipped. """
        log.e('error日志')
        log.d('debug日志')
        log.i('info日志')
        log.w('warning日志')


if __name__ == '__main__':
    unittest.main()
