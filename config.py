# 自定义config
import os
import configparser


class Config(object):
    def __init__(self):
        cur_path = os.path.dirname(os.path.realpath(__file__))
        cfg_path = os.path.join(cur_path, "config.ini")

        cfg = configparser.ConfigParser()
        cfg.read(cfg_path, encoding='utf-8')
        self.drivers = dict(cfg['driver_path'])
        self.account = dict(cfg['baidu_account'])

    def get_username(self):
        return self.account.get('username')

    def get_password(self):
        return self.account.get('password')

    def get_chrome_driver_path(self):
        return self.drivers.get('chrome')

    def get_firefox_driver_path(self):
        return self.drivers.get('firefox')

    def get_edge_driver_path(self):
        return self.drivers.get('edge')
