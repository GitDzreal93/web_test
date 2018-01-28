# @Time    : 2018/1/26 21:36
# @Author  : Dzreal
# @Site    : 
# @File    : test_sousuo.py
# @Software: PyCharm
from selenium.webdriver.common.keys import Keys
from Util.basecase import BaseCase
from Util.tools import *

# 获取当前测试用例名称
# casename = os.path.basename((__file__).strip('*.py'))

class TestSousuo(BaseCase):

    def test_01_input_max(self):
        print("请输入最大值")

    def test_02_input_none(self):
        print("输入空数据")

    @unittest.skip("no reason")
    def test_03_input_number(self):
        print("输入数字")

    @unittest.skip("no reason")
    def test_04_input_english(self):
        print("输入英文")

    @unittest.skip("no reason")
    def test_05_input_chinese(self):
        print("输入中文")
    @unittest.skip("no reason")
    def test_06_input_outher(self):
        print("输入特殊字符")
