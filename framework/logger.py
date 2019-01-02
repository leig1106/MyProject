# -*- coding:utf-8 -*-
import logging,time,os
from config.get_config_value import Get_Config_Value

write_log_to_file = Get_Config_Value().get_value('configuration','IS_WRITE_LOG_TO_FILE')
write_log_to_stream = Get_Config_Value().get_value('configuration','IS_WRITE_LOG_TO_STREAM')

class Logger(object):

    def __init__(self,logger):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志存入到指定的文件中
        :param logger:
        """
        #创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s')

        if write_log_to_file == 'True':
            #创建一个handler,用于写入日志文件
            timestamp = time.strftime('%Y%m%d%H%M',time.localtime())
            filename = os.path.dirname(os.getcwd())+'\\logs\\'+timestamp+'.log'
            fh = logging.FileHandler(filename,mode='a')
            fh.setLevel(logging.INFO)
            fh.setFormatter(formatter)
            # 给logger添加handler
            self.logger.addHandler(fh)

        if write_log_to_stream == 'True':
            #创建一个handler,用于输出到控制台
            sh = logging.StreamHandler()
            sh.setLevel(logging.INFO)
            sh.setFormatter(formatter)
            #给logger添加handler
            self.logger.addHandler(sh)

    def get_logger(self):
        return self.logger

