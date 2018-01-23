# coding=utf-8
import unittest

import os

import time

from framework.utils import Utils
from framework.browser_engine import BrowserEngine
from framework.excelhandle import excelHandle
from framework.base_page import BasePage, logger
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class ApplicationSetting(unittest.TestCase, BasePage):
    global flag

    def test_dstaff_management(self):
        a = 10
        b = 0
        try:
            print (a/b)
        except Exception as e:
            logger.error("Failed to click the element with %s" % e)
            self.flag = False
            return
        print a * b

    def test_hparaSet_management(self):
        self.test_dstaff_management()
        if self.flag is False:
            return
        a = 10
        b = 1
        try:
            print (a / b)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)
        print a * b

if __name__ == '__main__':
    unittest.main()