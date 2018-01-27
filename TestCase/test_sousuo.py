# @Time    : 2018/1/26 21:36
# @Author  : Dzreal
# @Site    : 
# @File    : test_sousuo.py
# @Software: PyCharm
import os

import unittest
from Util import HTMLTestRunner
from Util.basecase import BaseCase
from Util.report_maker import create_report



class TestSousuo(BaseCase):
    def test_01_input_max(self):
        print("输入最大长度")

    def test_02_input_none(self):
        print("输入空数据")

    def test_03_input_number(self):
        print("输入数字")

    @unittest.skip("Im Chinese")
    def test_04_input_english(self):
        print("输入英文")

    @unittest.skipIf(1, "if test01 run ,test05 do not run\n")
    def test_05_input_chinese(self):
        print("输入中文")

    def test_06_input_expect(self):
        print("输入特殊字符")

    def test_07_input_div0(self):
        num = 1/0
        print(num)
        print("臭傻逼")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestSousuo('test_06_input_expect'))
    suite.addTest(TestSousuo('test_02_input_none'))
    suite.addTest(TestSousuo('test_03_input_number'))
    suite.addTest(TestSousuo('test_01_input_max'))

    create_report(suite)
