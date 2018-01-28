from Util.tools import *


class BaseCase(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        "Hook method for setting up the test fixture before exercising it."
        cls.driver = openBrower('chrome')


    @classmethod
    def tearDownClass(cls):
        "Hook method for deconstructing the test fixture after testing it."
        cls.driver.quit()
