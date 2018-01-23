# -*- coding:utf-8 -*-
import ConfigParser
import os.path
from selenium import webdriver
from framework.logger import Logger
from selenium.webdriver import Remote
logger = Logger(logger="BrowserEngine").getlog()
lists = {'http://10.11.117.32:5555/wd/hub': 'chrome',
         # 'http://127.0.0.1:5555/wd/hub': 'firefox',
         # 'http://127.0.0.1:5556/wd/hub': 'internet explorer'
        }

class BrowserEngine(object):
    # dir = os.path.dirname(os.path.abspath('.'))  # 注意相对路径获取方法
    # chrome_driver_path = 'D:\\PycharmProjects\\AutoTestEinvoice\\tools\\chromedriver.exe'
    # ie_driver_path = 'D:\\PycharmProjects\\AutoTestEinvoice\\tools\\IEDriverServer.exe'

    def __init__(self, driver):
        self.driver = driver

        # read the browser type from config.ini file, return the driver

    def open_browser(self, driver):
        config = ConfigParser.ConfigParser()
        # file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
        file_path = "D:\\PycharmProjects\\AutoTestEinvoice\\config\\config.ini"
        config.read(file_path)
        url = config.get("testServer", "URL")
        logger.info("The test server url is: %s" % url)
        for host, browser in lists.items():
            driver = Remote(command_executor=host,
                            desired_capabilities={'platform': 'ANY',
                                                  'browserName': browser,
                                                  'version': '',
                                                  'javascriptEnabled': True
                                                  }
                            )
            driver.get(url)
            logger.info("Open url: %s" % url)
            driver.maximize_window()
            logger.info("Maximize the current window.")
            driver.implicitly_wait(10)
            logger.info("Set implicitly wait 10 seconds.")
            return driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()