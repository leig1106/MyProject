#coding:utf-8

import time,datetime

class GetTime(object):

    def get_current_time(self):
        # print(time.time())
        # print(time.localtime())
        now_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        return now_time

    def get_timestamp(self):
        timestamp = time.strftime('%Y%m%d%H%M%S',time.localtime())
        return timestamp


    def get_microsecond_time(self):
        now = datetime.datetime.now()
        now_time = now.strftime("%Y-%m-%d %H:%M:%S.%f")
        return now_time
