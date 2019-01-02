#-*- coding:utf-8 -*-
from selenium import webdriver
from config.get_config_value import Get_Config_Value
from framework.logger import Logger

mylogger = Logger('BrowserEngine').get_logger()

class BrowserEngine(object):
    """
    定义一个浏览器引擎类，根据browser_type的值去，控制启动不同的浏览器，这里主要是IE，Firefox, Chrome
    """

    def get_browser(self):
        """
        通过if语句，来控制初始化不同浏览器的启动，默认是启动Chrome
        :return: driver
        """
        browsertype = Get_Config_Value().get_value('browserType','browserName')
        mylogger.info('你选择了%s浏览器' % browsertype)

        if browsertype == 'FireFox':
            driver = webdriver.Firefox()
            mylogger.info('启动Firefox浏览器')
        elif browsertype == 'Chrome':
            driver = webdriver.Chrome()
            mylogger.info('启动Chrome浏览器')
        elif browsertype == 'IE':
            driver = webdriver.Ie()
            mylogger.info('启动IE浏览器')
        else:
            driver = webdriver.Chrome()
            mylogger.info('启动Chrome浏览器')

        driver.maximize_window()
        mylogger.info('最大化浏览器')
        driver.implicitly_wait(5)
        mylogger.info('等待5秒')
        return driver