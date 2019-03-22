import unittest
from common.desired_caps import appium_desired
import logging
from time import sleep

class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info('=====setUp====')
        # case运行前 先连接服务
        self.driver=appium_desired()

    def tearDown(self):
        logging.info('====tearDown====')
        sleep(5)
        self.driver.close_app()