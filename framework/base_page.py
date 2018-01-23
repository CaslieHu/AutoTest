# coding=utf-8
import time
from datetime import datetime

from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
import os.path
from selenium.webdriver.common.by import By
from framework.logger import Logger
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC, ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import unittest
import sys

# create a logger instance
logger = Logger(logger="BasePage").getlog()


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类，以后每个POM中的页面类，都继承这个基类，这样每个页面类都有基类的方法
    """

    def __init__(self, driver):
        self.driver = driver

        # quit browser and end testing

    def quit_browser(self):
        self.driver.quit()

        # 浏览器前进操作

    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")

        # 浏览器后退操作

    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")

        # 隐式等待

    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds." % seconds)

        # 点击关闭当前窗口

    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")
        except NameError as e:
            logger.error("Failed to quit the browser with %s" % e)

            # 保存图片

    def get_windows_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        # file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        file_path = "D:\\PycharmProjects\\AutoTestEinvoice\\screenshots\\"
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            print (screen_name)
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()

    def find_element(self, selector_by, selector_value, info):
        # selector_by表示定位方式，selector_value表示定位值
        the_element = self.is_element_present(selector_by, selector_value)
        if the_element:
            if selector_by == 'xpath':
                element = self.driver.find_element_by_xpath(selector_value)
            elif selector_by == 'cssSelector':
                element = self.driver.find_element_by_css_selector(selector_value)
            elif selector_by == 'id':
                element = self.driver.find_element_by_id(selector_value)
            else:
                raise NameError("定位方式不存在，请检查")
        else:
            self.get_windows_img()
            raise NoSuchElementException("定位方式为%s,定位值为%s的元素%s未找到" % (selector_by, selector_value, info))
        return element

    def check_element(self, selector_by, selector_value, info):
        # selector_by表示定位方式，selector_value表示定位值
        the_element = self.is_element_present(selector_by, selector_value)
        if the_element:
            if selector_by == 'xpath':
                element = self.driver.find_element_by_xpath(selector_value)
            elif selector_by == 'cssSelector':
                element = self.driver.find_element_by_css_selector(selector_value)
            elif selector_by == 'id':
                element = self.driver.find_element_by_id(selector_value)
            else:
                raise NameError("定位方式不存在，请检查")
        else:
            raise NoSuchElementException("定位方式为%s,定位值为%s的元素%s未找到" % (selector_by, selector_value, info))
        return element

    # 定位元素方法
    def find_element2(self, selector_by, selector_value):
        # selector_by表示定位方式，selector_value表示定位值
        element = ''
        if selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
            except Exception as e:
                self.get_windows_img()
                logger.error("无法定位 %s" % e)
        elif selector_by == 'cssSelector':
            try:
                element = self.driver.find_element_by_css_selector(selector_value)
            except Exception as e:
                self.get_windows_img()
                logger.error("无法定位 %s" % e)
        elif selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
            except Exception as e:
                logger.error("无法定位: %s" % e)
                self.get_windows_img()  # take screenshot
        elif selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == 'className':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == 'linkText':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == 'partialLinkText':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == 'tagName':
            element = self.driver.find_element_by_tag_name(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")
        return element

    # 判断元素是否存在
    def is_element_present(self, selector_by, selector_value):
        if selector_by == 'xpath':
            element = (By.XPATH, selector_value)
        elif selector_by == 'cssSelector':
            element = (By.CSS_SELECTOR, selector_value)
        elif selector_by == 'id':
            element = (By.ID, selector_value)
        else:
            raise NameError(u"元素定位方式不正确")
        try:
            # WebDriverWait(driver, 10).until(EC.presence_of_element_located(element))
            ui.WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element))
            flag = True
        except Exception as e:
            logger.error(u"异常原因：元素不存在，请检查定位方式或定位值，详细异常信息%s" % e)
            flag = False
        if flag is False:
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(element))
                flag = True
            except Exception as e:
                logger.error(u"异常原因：元素不存在，请检查定位方式或定位值，详细异常信息%s" % e)
                flag = False
        return flag

        # 输入

    def input(self, selector_by, selector_value, text, info):
        el = self.find_element(selector_by, selector_value, info)
        flag = True
        """
        try:
            el.clear()
            t = text.decode('utf-8')
            el.send_keys(t)
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img()
        """
        try:
            el.clear()
            t = text.decode('utf-8')
            el.send_keys(t)
        except Exception as e:
            flag = False
            pass
        if not flag:
            try:
                t = text.decode('utf-8')
                el.send_keys(t)
                logger.info("Had type \' %s \' in inputBox" % text)
            except NameError as e:
                logger.error("Failed to type in input box with %s" % e)
                self.get_windows_img()
                print ("无法定位" + "text" % e)

    # 清除文本框
    def clear(self, selector_by, selector_value):

        el = self.find_element(selector_by, selector_value)
        try:
            el.clear()
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()

            # 点击元素

    def click(self, selector_by, selector_value, Offset, info):
        el = self.find_element(selector_by, selector_value, info)
        flag = True
        try:
            if Offset.strip() == '':
                el.click()
            else:
                str1 = str(Offset)
                strlist = str1.split(',')
                x = strlist[0]
                y = strlist[1]
                ActionChains(self.driver).move_to_element_with_offset(el, x, y).click().perform()
        except WebDriverException as e:
            time.sleep(1)
            self.click(selector_by, selector_value, Offset, info)
        except Exception as e:
            self.get_windows_img()
            raise Exception(u"%s 点击失败,详细信息：" % [info, e])
            # logger.error("Failed to click the element with %s" % e)

    # 点击提交,此点击操作用于提交表单
    def submit(self, selector_by, selector_value):
        el = self.find_element(selector_by, selector_value)
        try:
            el.submit()
        except NameError as e:
            self.get_windows_img()
            logger.error("Failed to submit the element with %s" % e)

            # 鼠标右击操作

    def context_click(self, selector_by, selector_value, info):
        el = self.find_element(selector_by, selector_value)
        try:
            ActionChains(self.driver).context_click(el).perform()
        except NameError as e:
            self.get_windows_img()
            logger.error("Failed to right click the element with %s" % e)

            # 鼠标悬停

    def mouse_move(self, selector_by, selector_value, info):
        el = self.find_element(selector_by, selector_value, info)
        try:
            ActionChains(self.driver).move_to_element(el).perform()
        except NameError:
            self.get_windows_img()
            logger.error("Failed to mouse_move the element with %s" % info)

            # 鼠标双击操作

    def double_click(self, selector_by, selector_value):
        el = self.find_element(selector_by, selector_value)
        try:
            ActionChains(self.driver).double_click(el).perform()
        except NameError as e:
            self.get_windows_img()
            logger.error("Failed to double_click the element with %s" % e)

            # 鼠标拖放操作

    def drag_and_drop(self, selector_by, selector_value, target):
        el = self.find_element(selector_by, selector_value)
        target = self.find_element(target)
        try:
            ActionChains(self.driver).drag_and_drop(el, target).perform()
        except NameError as e:
            self.get_windows_img()
            logger.error("Failed to drag_and_drop the element with %s" % e)

            # 选择下拉框

    def select(self, selector_by, selector_value, value, info):
        el = Select(self.find_element(selector_by, selector_value, info))
        try:
            el.select_by_visible_text(value)
            # el.select_by_value(value)
        except NameError as e:
            logger.error("Failed to select the element with %s" % e)
            self.get_windows_img()

    # 检查点,当检查点有值是判断是否与预期text相等;当检查点无值时则判断该元素是否存在,text表示,remark表示备注信息
    def checkpoint(self, selector_by, selector_value, text2, remark):
        text = str(text2)
        if text == '':
            try:
                flag = self.is_element_present(selector_by, selector_value)
                assert flag is True
            except AssertionError as e:
                logger.error("断言失败，检查点元素不存在，请检查定位方式或定位值，详细信息：%s" % e)
        else:
            try:
                el = self.check_element(selector_by, selector_value, remark)
                # el.text == ''当元素为input时，el.text获取不到页面值，因此为空，需要用get_attribute()属性来获得
                if el.text == '':
                    elText = str(el.get_attribute("value"))
                    assert text == elText
                else:
                    self.textAssert(selector_by, selector_value, text2)
            except Exception as e:
                logger.error(u"断言失败，检查点元素不存在，请检查定位方式或定位值，详细信息：%s" % e)

    # 检查点,当检查点有值是判断是否与预期text相等;当检查点无值时则判断该元素是否存在,text表示,remark表示备注信息
    def checkpoint2(self, selector_by, selector_value, text2, remark):
        text = str(text2)
        if text == '':
            try:
                if selector_by == 'xpath':
                    try:
                        self.driver.find_element_by_xpath(selector_value)
                    except Exception as e:
                        self.driver.find_elements_by_xpath(selector_value)
                        pass
                elif selector_by == 'cssSelector':
                    self.driver.find_element_by_css_selector(selector_value)
            except Exception as e:
                logger.error('检查点校验失败:%s', format(e))
                pass
        else:
            # self.assertEqual(el.text, text, msg="该检查点校验失败，请查看检查点的值是否正确")
            try:
                if selector_by == 'xpath':
                    try:
                        el = self.driver.find_element_by_xpath(selector_value)
                        # 判断元素是否为输入框
                        if el.text == "":
                            elText = str(el.get_attribute("value"))
                            assert text == elText
                        else:
                            elText = str(el.text)
                            if self.textAssert(text, elText) is False:
                                ele = Select(self.find_element(selector_by, selector_value))
                                elText = str(ele.first_selected_option.text)
                                print (elText)
                                assert text == elText
                    except Exception as e:
                        els = self.driver.find_elements_by_xpath(selector_value)
                        for i in els:
                            assert text == i.text
                        pass
                elif selector_by == 'cssSelector':
                    el = self.driver.find_element_by_css_selector(selector_value)
                    if el.text == "":
                        elText = str(el.get_attribute("value"))
                        assert text == elText
                    else:
                        elText = str(el.text)
                        assert text == elText
            except Exception as e:
                logger.error('检查点校验失败:%s', format(e))
                self.get_windows_img()
                pass

    # 一直等待某元素可见，默认超时10秒
    def is_visible(self, locator, timeout=10):
        try:
            ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False

    # 断言事件
    def textAssert(self, selector_by, selector_value, text2):
        global isEqual
        try:
            if selector_by == 'xpath':
                elValue = str(selector_value)
                if elValue.__contains__("/tr/"):
                    els = self.driver.find_elements_by_xpath(selector_value)
                    for i in els:
                        assert text2 == i.text
                    isEqual = True
                else:
                    time.sleep(1)
                    els = self.driver.find_element_by_xpath(selector_value)
                    assert text2 == els.text
                    isEqual = True
            elif selector_by == 'cssSelector':
                elValue = str(selector_value)
                if elValue.__contains__("/tr/"):
                    els = self.driver.find_elements_by_css_selector(selector_value)
                    for i in els:
                        assert text2 == i.text
                        isEqual = True
                else:
                    els = self.driver.find_element_by_css_selector(selector_value)
                    assert text2 == els.text
                    isEqual = True
            else:
                logger.error(u"定位方式不正确.")
                isEqual = False
        except:
            logger.error("断言失败，预期值与实际值不一致")
            isEqual = False
        return isEqual

    # 键盘事件
    def key(self, selector_by, selector_value, keyValue, info):
        try:
            el = self.find_element(selector_by, selector_value, info)
            t = keyValue
            if t == 'Enter':
                el.send_keys(Keys.ENTER)
            else:
                logger.info("暂不支持 %s" % t)
            logger.info("Had key \' %s \' clicked" % keyValue)
        except NameError as e:
            logger.error("Failed to %s" % keyValue)
            self.get_windows_img()

    # 获取网页标题
    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        waitTime = seconds / 1000
        time.sleep(waitTime)

    def assertEqual(self, text, text1, msg):
        if text == text1:
            flag = True
        else:
            flag = False
            logger.error(msg)
        return flag
