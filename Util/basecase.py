from Util.tools import *


class BaseCase(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        "Hook method for setting up the Testcode fixture before exercising it."
        cls.driver = openBrower('chrome')
        openUrl(cls.driver,'http://www.baidu.com')

    @classmethod
    def tearDownClass(cls):
        "Hook method for deconstructing the Testcode fixture after testing it."
        cls.driver.quit()
