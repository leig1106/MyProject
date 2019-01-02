# coding=utf-8

import os,configparser

class Get_Config_Value(object):
    """
    传入section和option，获取该配置项的值
    """

    def __init__(self):
        """
        读取配置文件
        """
        file = os.path.dirname(os.path.abspath('.')) + '\config\config.ini'
        self.conf = configparser.ConfigParser()
        self.conf.read(file)

    def get_options(self,section):
        return self.conf.options(section)


    def get_value(self,section,option):
        return self.conf.get(section,option)


