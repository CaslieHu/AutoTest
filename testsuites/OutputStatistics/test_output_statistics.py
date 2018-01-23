# coding=utf-8
import unittest

import os

import time

from framework.browser_engine import BrowserEngine
from framework.excelhandle import excelHandle
from framework.base_page import BasePage, logger
from framework.utils import Utils
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class OutputStatistics(unittest.TestCase, BasePage):
    u'''销项统计'''
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

    def test_sales_invoice_summary(self):
        u'''测试销项发票汇总表'''
        excel = excelHandle()
        filename = r'D:\PycharmProjects\AutoTestEinvoice\script\税务云-正式环境fapiao\6.销项统计\销项发票汇总表-正.xlsx'
        sheetname = 'Sheet1'
        tables = excel.read_excel(unicode(filename, "utf-8"), sheetname)
        # 公共部分，读取表格
        util = Utils(BasePage)
        util.util(self.driver, tables)

    def test_invoice_packing_list(self):
        u'''测试销项发票明细表'''
        excel = excelHandle()
        filename = r'D:\PycharmProjects\AutoTestEinvoice\script\税务云-正式环境fapiao\6.销项统计\销项发票明细表-正.xlsx'
        sheetname = 'Sheet1'
        tables = excel.read_excel(unicode(filename, "utf-8"), sheetname)
        # 公共部分，读取表格
        util = Utils(BasePage)
        util.util(self.driver, tables)

    def test_sales_statistics(self):
        u'''测试销售统计表'''
        excel = excelHandle()
        logger.info("开始回放脚本销售统计表")
        logger.info("开始回放脚本销售统计表")
        filename = r'D:\PycharmProjects\AutoTestEinvoice\script\税务云-正式环境fapiao\6.销项统计\销售统计表-正.xlsx'
        sheetname = 'Sheet1'
        tables = excel.read_excel(unicode(filename, "utf-8"), sheetname)
        # 公共部分，读取表格
        util = Utils(BasePage)
        util.util(self.driver, tables)
        logger.info("结束回放脚本销售统计表")
        logger.info("结束回放脚本销售统计表")
        logger.info("结束回放脚本销售统计表")
        logger.info("结束回放脚本销售统计表")


if __name__ == '__main__':
    unittest.main()