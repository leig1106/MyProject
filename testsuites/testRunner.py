#-*-coding:utf-8 -*-

import unittest,os
from framework.get_time import GetTime
import HTMLTestRunner
from testsuites.baidu_search import BaiduSearch

# suite = unittest.TestSuite()
# suite.addTest(BaiduSearch('test_check_search'))
# suite.addTest(BaiduSearch('test_check_nbalist'))
report_path = os.path.dirname(os.getcwd())+'\\test_report\\'
timestamp = GetTime().get_timestamp()
htmlfile = report_path + timestamp + 'report.html'
fp = open(htmlfile,'wb')


suite = unittest.TestLoader().discover("testsuites")



if __name__ == '__main__':
    #unittest.TextTestRunner(verbosity=2).run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title='baidu测试报告',description='用例测试情况')
    runner.run(suite)