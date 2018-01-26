import unittest

case_path = ".\\TestCase"


def Creatsuite():
    # 定义单元测试容器
    testunit = unittest.TestSuite()

    # 定搜索用例文件的方法
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test_*.py', top_level_dir=None)

    # 将测试用例加入测试容器中
    for test_suite in discover:
        for casename in test_suite:
            testunit.addTest(casename)
        print(testunit)
    return testunit


if __name__ == "__main__":
    pass
