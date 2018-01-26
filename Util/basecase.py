import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from Util import tools

Path = ''

class BaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        "Hook method for setting up the test fixture before exercising it."
        print('''
        1、开启浏览器
        2、请求URL
        3、获取句柄
              ''')

        # cls.ob = tools.openBrower('firefox')
        # cls.webdriver_handle = tools.openUrl(cls.ob,'www.baidu.com')


    @classmethod
    def tearDownClass(cls):
        "Hook method for deconstructing the test fixture after testing it."
        print("生成report")
        print("关闭浏览器")

