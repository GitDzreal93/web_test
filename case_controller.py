import unittest
from test_case import *

test_case_conf = {}

class TestInsert(unittest.TestSuite):
    # 读取test_cases配置
    def read_case(self,test_cases):


    def insert_case(self):
        for case_name, case_step in test_cases.items():
            self.addTest(case_name(''.format()))
