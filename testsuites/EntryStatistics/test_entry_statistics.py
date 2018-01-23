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

class Entry_Statistics(unittest.TestCase, BasePage):
    u'''进项统计'''
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
    """
    @classmethod
    def tearDown(cls):
        cls.driver.quit()
    """
    def test_purchase_statistics(self):
        u'''测试采购统计表'''
        excel = excelHandle()
        logger.info("开始回放脚本采购统计表")
        logger.info("开始回放脚本采购统计表")
        filename = r'D:\PycharmProjects\AutoTestEinvoice\script\税务云-正式环境fapiao\7.进项统计\采购统计表-正.xlsx'
        sheetname = 'Sheet1'
        tables = excel.read_excel(unicode(filename, "utf-8"), sheetname)
        # 公共部分，读取表格
        util = Utils(BasePage)
        util.util(self.driver, tables)
        logger.info("结束回放脚本采购统计表")
        logger.info("结束回放脚本采购统计表")
        logger.info("结束回放脚本采购统计表")
        logger.info("结束回放脚本采购统计表")

    def test_reimbursement_statistics(self):
        u'''测试报销统计表'''
        excel = excelHandle()
        logger.info("开始回放脚本报销统计表")
        logger.info("开始回放脚本报销统计表")
        filename = r'D:\PycharmProjects\AutoTestEinvoice\script\税务云-正式环境fapiao\7.进项统计\报销统计表-正.xlsx'
        sheetname = 'Sheet1'
        tables = excel.read_excel(unicode(filename, "utf-8"), sheetname)
        # 公共部分，读取表格
        util = Utils(BasePage)
        util.util(self.driver, tables)
        logger.info("结束回放脚本报销统计表")
        logger.info("结束回放脚本报销统计表")
        logger.info("结束回放脚本报销统计表")
        logger.info("结束回放脚本报销统计表")


if __name__ == '__main__':
    unittest.main()