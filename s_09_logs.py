# 自定义Logs

import logging
import logging.handlers
import os
import time


class Logs(object):
    def __init__(self, logger=None):
        self.logger = logging.getLogger("")
        # 创建文件目录
        logs_dir = "s_09_logs"
        if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
            pass
        else:
            os.mkdir(logs_dir)

        # 修改log保存位置
        timestamp = time.strftime("%Y-%m-%d", time.localtime())
        log_filename = '%s.txt' % timestamp
        log_filepath = os.path.join(logs_dir, log_filename)
        rotating_file_handler = logging.handlers.RotatingFileHandler(filename=log_filepath,
                                                                     maxBytes=1024 * 1024 * 50,
                                                                     backupCount=5)
        # 设置输出格式[]
        # %(levelno)s: 打印日志级别的数值
        # %(levelname)s: 打印日志级别名称
        # %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
        # %(filename)s: 打印当前执行程序名
        # %(funcName)s: 打印日志的当前函数
        # %(lineno)d: 打印日志的当前行号
        # %(asctime)s: 打印日志的时间
        # %(thread)d: 打印线程ID
        # %(threadName)s: 打印线程名称
        # %(process)d: 打印进程ID
        # %(message)s: 打印日志信息
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        rotating_file_handler.setFormatter(formatter)
        # 控制台句柄
        console = logging.StreamHandler()
        console.setLevel(logging.NOTSET)
        console.setFormatter(formatter)
        # 添加内容到日志句柄中
        self.logger.addHandler(rotating_file_handler)
        self.logger.addHandler(console)
        self.logger.setLevel(logging.NOTSET)

    # info
    def i(self, message):
        self.logger.info(message)

    # debug
    def d(self, message):
        self.logger.debug(message)

    # warning
    def w(self, message):
        self.logger.warning(message)

    # error
    def e(self, message):
        self.logger.error(message)

    def get_log(self):
        return self.logger
