# coding=utf-8
from framework import HTMLTestRunner
import os
import unittest
import time

# 设置报告文件保存路径
report_path = os.path.join(os.getcwd(), "test_report")
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式
HtmlFile = report_path + "\\" + now + "HTMLtemplate.html"
fp = file(HtmlFile, "wb")

# 用例路径
case_path = os.path.join(os.getcwd(), "testsuites")
# case_path = os.path.join(os.getcwd(), "testdemos")
# case_path = os.path.join(os.getcwd(), "demo")

# 构建suite
suite = unittest.TestLoader().discover(case_path, pattern="test_*.py", top_level_dir=None)

if __name__ == '__main__':
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"用友税务服务云自动化测试报告", description=u"")
    # 开始执行测试套件
    runner.run(suite)

