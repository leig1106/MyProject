# coding=utf-8

import os,configparser

class Get_Config_Value(object):
    """
    传入section和option，获取该配置项的值
    """

    def __init__(self,section,option):
        self.section = section
        self.option = option

    def get_value(self):
        file = os.path.dirname(os.path.abspath('.'))+'\config\config.ini'
        conf = configparser.ConfigParser()
        conf.read(file)
        value = conf.get(self.section,self.option)
        return value

