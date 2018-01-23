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

class PersonalOperation(unittest.TestCase, BasePage):
    u'''个人账户操作'''
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
        # 正式环境个人登录
        cls.driver.find_element_by_xpath("//*[@id='public-clouds']/span[2]").click()
        time.sleep(2)
        cls.driver.find_element_by_id("username").clear()
        cls.driver.find_element_by_id("username").send_keys("13581701532")
        cls.driver.find_element_by_id("password").clear()
        cls.driver.find_element_by_id("password").send_keys("111111a")
        cls.driver.find_element_by_id("submit_btn_login").click()
        time.sleep(2)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    def test_bmy_receipt(self):
        u'''测试我的发票'''
        excel = excelHandle()
        logger.info("开始回放脚本我的发票")
        logger.info("开始回放脚本我的发票")
        filename = r'D:\PycharmProjects\AutoTestEinvoice\script\税务云-正式环境fapiao\11.个人用户操作\我的发票-正.xlsx'
        sheetname = 'Sheet1'
        tables = excel.read_excel(unicode(filename, "utf-8"), sheetname)
        # 公共部分，读取表格
        util = Utils(BasePage)
        util.util(self.driver, tables)
        logger.info("结束回放脚本我的发票")
        logger.info("结束回放脚本我的发票")
        logger.info("结束回放脚本我的发票")
        logger.info("结束回放脚本我的发票")

    def test_aupload(self):
        u'''测试上传归集'''
        excel = excelHandle()
        logger.info("开始回放脚本上传归集")
        logger.info("开始回放脚本上传归集")
        filename = r'D:\PycharmProjects\AutoTestEinvoice\script\税务云-正式环境fapiao\11.个人用户操作\上传归集-正.xlsx'
        sheetname = 'Sheet1'
        tables = excel.read_excel(unicode(filename, "utf-8"), sheetname)
        # 公共部分，读取表格
        util = Utils(BasePage)
        util.util(self.driver, tables)
        logger.info("结束回放脚本上传归集")
        logger.info("结束回放脚本上传归集")
        logger.info("结束回放脚本上传归集")
        logger.info("结束回放脚本上传归集")

    def test_cmy_tag(self):
        u'''测试我的标签'''
        excel = excelHandle()
        logger.info("开始回放脚本我的标签")
        logger.info("开始回放脚本我的标签")
        filename = r'D:\PycharmProjects\AutoTestEinvoice\script\税务云-正式环境fapiao\11.个人用户操作\我的标签-正.xlsx'
        sheetname = 'Sheet1'
        tables = excel.read_excel(unicode(filename, "utf-8"), sheetname)
        # 公共部分，读取表格
        util = Utils(BasePage)
        util.util(self.driver, tables)
        logger.info("结束回放脚本我的标签")
        logger.info("结束回放脚本我的标签")
        logger.info("结束回放脚本我的标签")
        logger.info("结束回放脚本我的标签")

    def test_dpersonal_center(self):
        u'''测试个人中心'''
        excel = excelHandle()
        logger.info("开始回放脚本个人中心")
        logger.info("开始回放脚本个人中心")
        filename = r'D:\PycharmProjects\AutoTestEinvoice\script\税务云-正式环境fapiao\11.个人用户操作\个人中心-正.xlsx'
        sheetname = 'Sheet1'
        tables = excel.read_excel(unicode(filename, "utf-8"), sheetname)
        # 公共部分，读取表格
        util = Utils(BasePage)
        util.util(self.driver, tables)
        logger.info("结束回放脚本个人中心")
        logger.info("结束回放脚本个人中心")
        logger.info("结束回放脚本个人中心")
        logger.info("结束回放脚本个人中心")


if __name__ == '__main__':
    unittest.main()