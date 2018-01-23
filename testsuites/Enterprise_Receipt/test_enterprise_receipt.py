# coding=utf-8
import unittest
import time
from framework.browser_engine import BrowserEngine
from framework.excelhandle import excelHandle
from framework.base_page import BasePage, logger
from framework.utils import Utils
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Enterprise_Receipt(unittest.TestCase, BasePage):
    u'''企业受票'''
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
    def test_abaoxiao_account(self):
        u'''报销台账'''
        excel = excelHandle()
        logger.info("开始回放脚本报销台账")
        logger.info("开始回放脚本报销台账")
        filename = r'D:\PycharmProjects\AutoTestEinvoice\script\税务云-正式环境fapiao\5.企业受票\报销台账-正.xlsx'
        # filename = r'C:\Users\Administrator\Desktop\Demo.xlsx'
        sheetname = 'Sheet1'
        tables = excel.read_excel(unicode(filename, "utf-8"), sheetname)
        # 公共部分，读取表格
        util = Utils(BasePage)
        util.util(self.driver, tables)
        logger.info("结束回放脚本报销台账")
        logger.info("结束回放脚本报销台账")
        logger.info("结束回放脚本报销台账")
        logger.info("结束回放脚本报销台账")

    def test_bquestion_ticket_management(self):
        u'''疑票管理'''
        excel = excelHandle()
        logger.info("开始回放脚本疑票管理")
        logger.info("开始回放脚本疑票管理")
        filename = r'D:\PycharmProjects\AutoTestEinvoice\script\税务云-正式环境fapiao\5.企业受票\疑票管理-正.xlsx'
        sheetname = 'Sheet1'
        tables = excel.read_excel(unicode(filename, "utf-8"), sheetname)
        # 公共部分，读取表格
        util = Utils(BasePage)
        util.util(self.driver, tables)
        logger.info("结束回放脚本疑票管理")
        logger.info("结束回放脚本疑票管理")
        logger.info("结束回放脚本疑票管理")
        logger.info("结束回放脚本疑票管理")

    def test_caigou_account(self):
        u'''采购台账'''
        excel = excelHandle()
        logger.info("开始回放脚本采购台账")
        logger.info("开始回放脚本采购台账")
        filename = r'D:\PycharmProjects\AutoTestEinvoice\script\税务云-正式环境fapiao\5.企业受票\采购台账-正.xlsx'
        sheetname = 'Sheet1'
        tables = excel.read_excel(unicode(filename, "utf-8"), sheetname)
        # 公共部分，读取表格
        util = Utils(BasePage)
        util.util(self.driver, tables)
        logger.info("结束回放脚本采购台账")
        logger.info("结束回放脚本采购台账")
        logger.info("结束回放脚本采购台账")
        logger.info("结束回放脚本采购台账")

    def test_dhistorical_records(self):
        u'''查验历史记录'''
        excel = excelHandle()
        logger.info("开始回放脚本查验历史记录")
        logger.info("开始回放脚本查验历史记录")
        filename = r'D:\PycharmProjects\AutoTestEinvoice\script\税务云-正式环境fapiao\5.企业受票\查验历史记录-正.xlsx'
        sheetname = 'Sheet1'
        tables = excel.read_excel(unicode(filename, "utf-8"), sheetname)
        # 公共部分，读取表格
        util = Utils(BasePage)
        util.util(self.driver, tables)
        logger.info("结束回放脚本查验历史记录")
        logger.info("结束回放脚本查验历史记录")


if __name__ == '__main__':
    unittest.main()