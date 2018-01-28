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

ele_dict = read_yconf('sousuo_ele_conf.yaml', catalog='ele')
data_dict = read_yconf('sousuo_data_conf.yaml', catalog='data')

class TestSousuo(BaseCase):
    input_box = ele_dict['input']
    submit_box = ele_dict['submit']
    url = data_dict['url']

    def setUp(self):
        self.driver = openUrl(self.driver, self.url)

    def tearDown(self):
        self.driver = openUrl(self.driver,self.url)

    def test_01_input_max(self):
        print("输入最大长度")
        ele = self.driver.find_elements_by_xpath(self.input_box)
        ele.clear()
        ele.send_keys(data_dict['keyword_max'])
        ele.send_keys(Keys.ENTER)


    def test_02_input_none(self):
        print("输入空数据")
        ele = self.driver.find_elements_by_xpath(self.input_box)
        ele.clear()
        ele.send_keys(data_dict['keyword_none'])
        ele.send_keys(Keys.ENTER)

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
