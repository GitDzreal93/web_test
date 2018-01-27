import unittest
from settings import *
from TestCase import test_sousuo

case_path = CASE_DIR

def Creatsuite():
    # 定义单元测试容器
    testunit = unittest.TestSuite()

    # 定搜索用例文件的方法
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test_*.py', top_level_dir=None)
    print(type(discover))
    print(discover)

    # 将测试用例加入测试容器中
    for test_suite in discover:
        for casename in test_suite:
            testunit.addTest(casename)
    return testunit


if __name__ == "__main__":
    A = unittest.TestSuite()
    B = A.addTest(test_sousuo.TestSousuo('test_06_input_expect'))
    print(B)


