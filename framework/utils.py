# coding=utf-8
from framework.base_page import BasePage, logger
import sys
class Utils(BasePage):
    def util(self, driver, tables):
        self.driver = driver
        for i in range(len(tables)):
            row_list = tables[i]
            strTips = '行号：' + str(i + 1) + ',内容:['
            logger.info(strTips + ','.join("'" + str(element).decode('utf-8') + "'" for element in row_list) + ']')
            norun = row_list[4].decode('utf-8')
            # 如果表格中的第5列是 *，表示此行不运行，跳过。row_list[0]：要执行的动作值（如click）
            # row_list[1]:定位方式（如 xpath）
            # row_list[2]:定位值（如 //a[text()="保存"]）
            # row_list[3]:输入值或需要校验的值（如 请输入编码）
            # row_list[4]:此行是否运行 * 不运行，否则运行
            # row_list[5]：备注信息
            if norun == "*":
                continue
            elif row_list[0] == "click":
                # if row_list[3] is not None:
                self.click(row_list[1], row_list[2], row_list[3], row_list[5])
                # self.sleep(2000)
            elif row_list[0] == "input":
                strTel = str(row_list[3])
                self.input(row_list[1], row_list[2], strTel, row_list[5])
            elif row_list[0] == "mousemove":
                self.mouse_move(row_list[1], row_list[2], row_list[5])
            elif row_list[0] == "select":
                self.select(row_list[1], row_list[2], str(row_list[3]), row_list[5])
            elif row_list[0] == "wait":
                self.sleep(row_list[3])
            elif row_list[0] == "checkpoint":
                self.checkpoint(row_list[1], row_list[2], row_list[3], row_list[5])
            elif row_list[0] == "contentclick":
                self.context_click(row_list[1], row_list[2], row_list[5])
            elif row_list[0] == "key":
                key_list = tables[i - 1]
                self.key(key_list[1], key_list[2], row_list[3],row_list[5])
            elif row_list[0] == "back":
                self.back()
                self.sleep(2000)