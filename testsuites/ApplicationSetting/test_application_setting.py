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
    u'''应用设置'''
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

    def test_aorg_management(self):
        u'''测试组织管理'''
        excel = excelHandle()
        logger.info("开始回放脚本组织管理")
        filename = r'D:\PycharmProjects\AutoTestEinvoice\script\税务云-正式环境fapiao\3.应用设置\组织管理-正.xlsx'
        sheetname = 'Sheet1'
        tables = excel.read_excel(unicode(filename, "utf-8"), sheetname)
        # 公共部分，读取表格
        util = Utils(BasePage)
        util.util(self.driver, tables)
        logger.info("结束回放脚本组织管理")
        logger.info("结束回放脚本组织管理")
        logger.info("结束回放脚本组织管理")
        logger.info("结束回放脚本组织管理")

    def test_brole_management(self):
        u'''测试角色管理'''
        excel = excelHandle()
        logger.info("开始回放脚本角色管理")
        filename = r'D:\PycharmProjects\AutoTestEinvoice\script\税务云-正式环境fapiao\3.应用设置\角色管理-正.xlsx'
        sheetname = 'Sheet1'
        tables = excel.read_excel(unicode(filename, "utf-8"), sheetname)
        # 公共部分，读取表格
        util = Utils(BasePage)
        util.util(self.driver, tables)
        logger.info("结束回放脚本角色管理")
        logger.info("结束回放脚本角色管理")
        logger.info("结束回放脚本角色管理")
        logger.info("结束回放脚本角色管理")

    def test_cuser_management(self):
        u'''测试用户管理'''
        excel = excelHandle()
        logger.info("开始回放脚本用户管理")
        filename = r'D:\PycharmProjects\AutoTestEinvoice\script\税务云-正式环境fapiao\3.应用设置\用户管理-正.xlsx'
        sheetname = 'Sheet1'
        tables = excel.read_excel(unicode(filename, "utf-8"), sheetname)
        # 公共部分，读取表格
        util = Utils(BasePage)
        util.util(self.driver, tables)
        logger.info("结束回放脚本用户管理")
        logger.info("结束回放脚本用户管理")
        logger.info("结束回放脚本用户管理")
        logger.info("结束回放脚本用户管理")

    def test_dstaff_management(self):
        u'''测试员工管理'''
        excel = excelHandle()
        logger.info("开始回放脚本员工管理")
        filename = r'D:\PycharmProjects\AutoTestEinvoice\script\税务云-正式环境fapiao\3.应用设置\员工管理-正.xlsx'
        sheetname = 'Sheet1'
        tables = excel.read_excel(unicode(filename, "utf-8"), sheetname)
        # 公共部分，读取表格
        util = Utils(BasePage)
        util.util(self.driver, tables)
        logger.info("结束回放脚本员工管理")
        logger.info("结束回放脚本员工管理")
        logger.info("结束回放脚本员工管理")
        logger.info("结束回放脚本员工管理")

    def test_espda_management(self):
        u'''测试商品档案'''
        excel = excelHandle()
        logger.info("开始回放脚本商品档案")
        filename = r'D:\PycharmProjects\AutoTestEinvoice\script\税务云-正式环境fapiao\3.应用设置\商品档案-正.xlsx'
        sheetname = 'Sheet1'
        tables = excel.read_excel(unicode(filename, "utf-8"), sheetname)
        # 公共部分，读取表格
        util = Utils(BasePage)
        util.util(self.driver, tables)
        logger.info("结束回放脚本商品档案")
        logger.info("结束回放脚本商品档案")
        logger.info("结束回放脚本商品档案")
        logger.info("结束回放脚本商品档案")

    def test_fkhda_management(self):
        u'''测试客户档案'''
        excel = excelHandle()
        logger.info("开始回放脚本客户档案")
        # filename = r'D:\PycharmProjects\AutoTestEinvoice\script\税务云-正式环境fapiao\3.应用设置\客户档案-正.xlsx'
        filename = r'C:\Users\Administrator\Desktop\Demo.xlsx'
        sheetname = 'Sheet1'
        tables = excel.read_excel(unicode(filename, "utf-8"), sheetname)
        # 公共部分，读取表格
        util = Utils(BasePage)
        util.util(self.driver, tables)
        logger.info("结束回放脚本客户档案")
        logger.info("结束回放脚本客户档案")
        logger.info("结束回放脚本客户档案")
        logger.info("结束回放脚本客户档案")

    def test_gskpgl_management(self):
        u'''测试税控盘管理'''
        excel = excelHandle()
        logger.info("开始回放脚本税控盘管理")
        filename = r'D:\PycharmProjects\AutoTestEinvoice\script\税务云-正式环境fapiao\3.应用设置\税盘管理-正.xlsx'
        sheetname = 'Sheet1'
        tables = excel.read_excel(unicode(filename, "utf-8"), sheetname)
        # 公共部分，读取表格
        util = Utils(BasePage)
        util.util(self.driver, tables)
        logger.info("结束回放脚本税控盘管理")
        logger.info("结束回放脚本税控盘管理")
        logger.info("结束回放脚本税控盘管理")
        logger.info("结束回放脚本税控盘管理")

    def test_hparaSet_management(self):
        u'''测试参数设置'''
        excel = excelHandle()
        logger.info("开始回放脚本参数设置")
        filename = r'D:\PycharmProjects\AutoTestEinvoice\script\税务云-正式环境fapiao\3.应用设置\参数设置-正.xlsx'
        sheetname = 'Sheet1'
        tables = excel.read_excel(unicode(filename, "utf-8"), sheetname)
        # 公共部分，读取表格
        util = Utils(BasePage)
        util.util(self.driver, tables)
        logger.info("结束回放脚本参数设置")
        logger.info("结束回放脚本参数设置")
        logger.info("结束回放脚本参数设置")
        logger.info("结束回放脚本参数设置")


if __name__ == '__main__':
    unittest.main()