import unittest
from TestCase import *

if __name__ == "__main__":
    # 实例化测试套件
    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner()
    runner.run(suite)