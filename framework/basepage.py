# coding=utf-8
import os,time
from selenium.common.exceptions import NoSuchElementException
from framework.get_time import GetTime
from framework.logger import Logger

mylog = Logger('basepage').get_logger()

class BasePage(object):
    '''
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    '''

    def __init__(self,driver):
        """
        写一个构造函数，有一个参数driver
        :param driver:
        """
        self.driver = driver

    def back(self):
        """
        浏览器后退按钮
        :return:none
        """
        self.driver.back()
        mylog.info('页面后退')

    def forward(self):
        """
        浏览器前进按钮
        :return:none
        """
        self.driver.forward()
        mylog.info('页面前进')

    def wait(self,seconds):
        """
        设置等待时间
        :param seconds:
        :return:
        """
        self.driver.implicitly_wait(seconds)
        mylog.info('等待%d秒' % seconds)

    def open_url(self,url):
        """
        打开url站点
        :param url:
        :return:
        """
        self.driver.get(url)
        mylog.info('打开网页')

    def quit_browser(self):
        """
        退出浏览器
        :return:none
        """
        self.driver.quit()
        mylog.info('退出浏览器')

    def get_windows_img(self):
        """
        截图并保存在根目录下的Screenshots文件夹下
        :param:
        """
        timestamp = GetTime().get_timestamp()
        path = os.path.dirname(os.getcwd())+'\\Screenshots\\'
        filename = path+timestamp+'.png'

        try:
            self.driver.get_screenshot_as_file(filename)
            mylog.info('开始截图并保存')
        except Exception as e:
            mylog.error('截图失败',exc_info=True)

    def __find_element(self,selector):
        """
        参数采用"id=>xx"或"xpath=>xxxxx"的格式填写定位元素
        :param selector:
        :return:
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_type = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_type == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                mylog.info('找到该元素')
            except NoSuchElementException as e:
                mylog.error('NoSuchElementException:%s' % e)
                self.get_windows_img()
        elif selector_type == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_type == 'class_name':
            element = self.driver.find_element_by_classname(selector_value)
        elif selector_type == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_type == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_type == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_type == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                mylog.info('找到该元素')
            except NoSuchElementException as e:
                mylog.error('NoSuchElementException:%s' % e)
                self.get_windows_img()
        else:
            raise NameError("请按照要求格式输入定位元素")

        return element

    def type(self,selector,text):
        """
        在定位的元素中输入text内容
        :param selector:
        :param text:
        :return:
        """
        ele = self.__find_element(selector)
        ele.clear()
        ele.send_keys(text)

    def clear(self,selector):
        """
        清空元素内值
        :param selector:
        :return:
        """
        ele = self.__find_element(selector)
        ele.clear()

    def click(self,selector):
        """
        点击该元素
        :param selector:
        :return:
        """
        ele = self.__find_element(selector)
        ele.click()

    def get_page_title(self):
        return self.driver.title

    def switch_to_window(self):
        cur_win = self.driver.current_window_handle
        wins = self.driver.window_handles
        for window in wins:
            if window != cur_win:
                self.driver.switch_to.window(window)

    def scroll_to_view(self,selector):
        """
        将页面下拉到target控件处
        :param target:
        :return:
        """
        ele = self.__find_element(selector)
        js = 'arguments[0].scrollIntoView();'
        self.driver.execute_script(js,ele)

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
