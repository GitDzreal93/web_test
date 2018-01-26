import unittest
from test_case import *

if __name__ == "__main__":
    # 实例化测试套件
    suite = unittest.TestSuite()
    # 将测试用例加载到测试套件中
    # 行顺序是安装加载顺序：
    # 先执行Test('test_One')，再执行Test1('test_One')

    # suite.addTest(test('test_05'))
    # suite.addTest(TestCase01('test_06'))

    # 实例化TextTestRunner类
    # 使用run()方法运行测试套件（即运行测试套件中的所有用例）
    runner = unittest.TextTestRunner()
    runner.run(suite)