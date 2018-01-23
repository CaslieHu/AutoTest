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


class QiYeOpen(unittest.TestCase, BasePage):
    u'''企业开票'''

    @classmethod
    def setUp(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
        """
        # 测试环境登录
        cls.driver.find_element_by_id("username").clear()
        cls.driver.find_element_by_id("username").send_keys("gyr00")
        cls.driver.find_element_by_id("password").clear()
        cls.driver.find_element_by_id("password").send_keys("1qaz2wsx")
        cls.driver.find_element_by_id("submit_btn_login").click()
        """
        # 正式环境登录
        cls.driver.find_element_by_id("yhtusername").clear()
        cls.driver.find_element_by_id("yhtusername").send_keys("shy1002")
        cls.driver.find_element_by_id("yhtpassword").clear()
        cls.driver.find_element_by_id("yhtpassword").send_keys("123456")
        cls.driver.find_element_by_xpath("//*[@id='fm4']//input[@class='btn-submit']").click()
        time.sleep(2)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    def test_ablue_open(self):
        u'''测试开具蓝票'''
        excel = excelHandle()
        logger.info("开始回放脚本开具蓝票")
        logger.info("开始回放脚本开具蓝票")
        filename = r'D:\PycharmProjects\AutoTestEinvoice\script\税务云-正式环境fapiao\4.企业开票\开具蓝票-正.xlsx'
        sheetname = 'Sheet1'
        tables = excel.read_excel(unicode(filename, "utf-8"), sheetname)
        # 公共部分，读取表格
        util = Utils(BasePage)
        util.util(self.driver, tables)
        logger.info("结束回放脚本开具蓝票")
        logger.info("结束回放脚本开具蓝票")
        logger.info("结束回放脚本开具蓝票")
        logger.info("结束回放脚本开具蓝票")

    # 由于红冲操作不可回退，因此只能在上线时测一次，并且测试完要重新准备数据(电票+)
    def test_bred_open(self):
        u'''测试开具红票'''
        excel = excelHandle()
        logger.info("开始回放脚本开具红票")
        logger.info("开始回放脚本开具红票")
        filename = r'D:\PycharmProjects\AutoTestEinvoice\script\税务云-正式环境fapiao\4.企业开票\开具红票-正.xlsx'
        sheetname = 'Sheet1'
        tables = excel.read_excel(unicode(filename, "utf-8"), sheetname)
        # 公共部分，读取表格
        util = Utils(BasePage)
        util.util(self.driver, tables)
        logger.info("结束回放脚本开具红票")
        logger.info("结束回放脚本开具红票")
        logger.info("结束回放脚本开具红票")
        logger.info("结束回放脚本开具红票")

    def test_code_open(self):
        u'''码上开票'''
        excel = excelHandle()
        logger.info("开始回放脚本码上开票")
        logger.info("开始回放脚本码上开票")
        filename = r'D:\PycharmProjects\AutoTestEinvoice\script\税务云-正式环境fapiao\4.企业开票\码上开票-正.xlsx'
        sheetname = 'Sheet1'
        tables = excel.read_excel(unicode(filename, "utf-8"), sheetname)
        # 公共部分，读取表格
        util = Utils(BasePage)
        util.util(self.driver, tables)
        logger.info("结束回放脚本码上开票")
        logger.info("结束回放脚本码上开票")
        logger.info("结束回放脚本码上开票")
        logger.info("结束回放脚本码上开票")

    def test_dnot_open(self):
        u'''未开票'''
        excel = excelHandle()
        logger.info("开始回放脚本未开票")
        logger.info("开始回放脚本未开票")
        filename = r'D:\PycharmProjects\AutoTestEinvoice\script\税务云-正式环境fapiao\4.企业开票\未开票-正.xlsx'
        # filename = r'C:\Users\Administrator\Desktop\Demo.xlsx'
        sheetname = 'Sheet1'
        tables = excel.read_excel(unicode(filename, "utf-8"), sheetname)
        # 公共部分，读取表格
        util = Utils(BasePage)
        util.util(self.driver, tables)
        logger.info("结束回放脚本未开票")
        logger.info("结束回放脚本未开票")
        logger.info("结束回放脚本未开票")
        logger.info("结束回放脚本未开票")

    # 由于红冲操作不可回退，因此只能在上线时测一次，并且测试完要重新准备数据（需要做红冲操作的票）
    def test_ehad_open(self):
        u'''已开票'''
        excel = excelHandle()
        logger.info("开始回放脚本已开票")
        logger.info("开始回放脚本已开票")
        filename = r'D:\PycharmProjects\AutoTestEinvoice\script\税务云-正式环境fapiao\4.企业开票\已开票-正.xlsx'
        # filename = r'C:\Users\Administrator\Desktop\Demo.xlsx'
        sheetname = 'Sheet1'
        tables = excel.read_excel(unicode(filename, "utf-8"), sheetname)
        # 公共部分，读取表格
        util = Utils(BasePage)
        util.util(self.driver, tables)
        logger.info("结束回放脚本已开票")
        logger.info("结束回放脚本已开票")
        logger.info("结束回放脚本已开票")
        logger.info("结束回放脚本已开票")


if __name__ == '__main__':
    unittest.main()
