import os

from Util import HTMLTestRunner
from settings import *

def create_report(suite):
    if os.path.exists(REPORT_DIR):
        filename = os.path.abspath(os.path.join(REPORT_DIR, '{}_report.html'.format(NOW)))
        with open(filename, 'wb') as fp:
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行详情：')
            runner.run(suite)
    else:
        os.mkdir(REPORT_DIR)
        filename = os.path.abspath(os.path.join(REPORT_DIR, '{}_report.html'.format(NOW)))
        with open(filename, 'wb') as fp:
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行详情：')
            runner.run(suite)