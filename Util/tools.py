# @Time    : 2018/1/25 13:22
# @Author  : Dzreal
# @Site    : 
# @File    : tools.py
# @Software: PyCharm
import yaml
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from settings import *
from Util import HTMLTestRunner


def read_yconf(cfname, catalog='data'):
    '''
    读取yaml文件
    :param cfname: yaml文件名称
    :param catalog: yaml文件所在目录别名，可选data（测试数据配置）或ele（测试控件的对象-元素映射表）
    :return:
    '''
    if catalog is 'data':
        yconf = os.path.join(DATA_DIR, cfname).replace('\\', '/')
    elif catalog is 'ele':
        yconf = os.path.join(ELE_DIR, cfname).replace('\\', '/')
    else:
        raise UserWarning('请选择正确的yaml配置文件目录，可选项catalog=data,或catalog=ele')

    try:
        with open(yconf) as fp:
            ym = yaml.load(fp)
            return ym
    except:
        raise UserWarning('oops,读取yaml_conf时，出现一些异常')


def get_ele_times(driver, times, func):
    '''
    等待函数进行完再进行下一操作（延时函数）
    :param driver: 浏览器句柄
    :param times: 等待时间（s）
    :param func: 方法名
    :return: 调用WebDriverWait去进行延时处理
    '''
    return WebDriverWait(driver, times).until(func)

def openBrower(browser):
    '''
    打开浏览器
    :param browser:浏览器名称（str）
    :return: 相应浏览器的句柄
    '''
    driver = None
    if browser is 'firefox':
        driver = webdriver.Firefox(executable_path=GECKODRIVER_PATH)
    elif browser is 'chrome':
        driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
    elif browser is 'ie':
        print('this is IE!')
        return 0
    else:
        print('there is no such browser!')

    return driver


def openUrl(driver, url):
    '''
    打开url
    :param driver: 浏览器句柄
    :param url: url
    '''
    driver.get(url)
    driver.maximize_window()

def createSuite():
    '''
    创建测试suite
    :return: 返回suite对象
    '''
    # 定义单元测试容器
    testunit = unittest.TestSuite()

    # 判断TCR目录下是否存在测试用例
    suite_list = os.listdir(TCR_DIR)
    suite_list.remove('__pycache__')

    if suite_list:
        for suit in suite_list:
            suit_suffix = suit.split('.')[1]
            if not suit_suffix == 'py':
                raise UserWarning('TCR中的case不合法')
            else:
                pass
    else:
        raise UserWarning('当前TCR没有存放任何case')

    # 定义搜索用例文件的方法

    discover = unittest.defaultTestLoader.discover(TCR_DIR, pattern='test_*.py', top_level_dir=None)
    if discover:
        pass
    else:
        raise UserWarning("TCR中的case不合法")

    # 将测试用例加入测试容器中
    for test_suite in discover:
        for case in test_suite:
            testunit.addTest(case)
    return testunit


def createReport(operator, suite):
    '''
    创建html测试报告
    :param casename:用例名称
    :param suite: 测试用例套件
    '''
    if os.path.exists(REPORT_DIR):
        filename = os.path.abspath(os.path.join(REPORT_DIR, '{}_{}_report.html'.format(operator, NOW)))
        with open(filename, 'wb') as fp:
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行详情：')
            runner.run(suite)
    else:
        os.mkdir(REPORT_DIR)
        filename = os.path.abspath(os.path.join(REPORT_DIR, '{}_{}_report.html'.format(operator, NOW)))
        with open(filename, 'wb') as fp:
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行详情：')
            runner.run(suite)


def sendMail():
    # TODO: 生成报告后自动发邮件
    pass


def cleanTCR():
    '''
    清空TestCaseRuntime下的所有case
    '''

    files = os.listdir(TCR_DIR)

    if not files:
        raise UserWarning("当前TCR没有存放任何case")

    else:
        for file in files:
            path = os.path.join(TCR_DIR, file).replace("\\", "/")
            os.remove(path)


if __name__ == '__main__':
    createSuite()
#
#
# # 填写表单数据函数
# def sendVals(eletuple, arg):
#     '''
#     ele tuple
#     account : uname, pwd
#     '''
#     listkey = ['uname', 'pwd']
#     i = 0
#     for key in listkey:
#         print(type(eletuple))
#         eletuple[i].send_keys('')
#         eletuple[i].clear()
#         time.sleep(1)
#         eletuple[i].send_keys(arg[key])
#         time.sleep(1)
#         i += 1
#         # if i==2:
#         #     eletuple[2].click()
#
#     eletuple[2].click()
#
#
# # 错误检查函数
# def checkResult(d, err_id, arg, log):
#     result = False
#     time.sleep(2)  # 服务器是有响应的过程，不加休眠，就会提示报错（假如账号密码正确，也打印出err的日志）
#
#     try:
#         err = d.find_element_by_id(err_id)
#         print("Account And Pwd Error!")
#         # msg = 'uname=%s pwd=%s:error:%s\n'%(arg['uname'], arg['pwd'], err.text)   #打印TXT日志，则将这两句注释去掉
#         # log.log_write(msg)
#         log.log_write(arg['uname'], arg['pwd'], 'Error', err.text)
#
#     except:
#         print("Account And Pwd Right!")
#         # msg = 'uname=%s pwd=%s:pass\n' % (arg['uname'], arg['pwd'])
#         # log.log_write(msg)
#         log.log_write(arg['uname'], arg['pwd'], 'Pass')
#         result = True
#     return result
#
#
# # 注销登录函数
# def logout(d, ele_dict):
#     ele = d.find_element_by_class_name(ele_dict['usermenu'])
#     ActionChains(d).move_to_element(ele).perform()
#     d.find_element_by_link_text(ele_dict['logout']).click()
#
#
# # 登录操作函数
# def login_test(ele_dict, user_list):
#     d = openBrower()
#     log = Xlloginfo()
#     log.log_init('sheet1', 'uname', 'pwd', 'result', 'msg')
#     openUrl(d, ele_dict['url'])
#     ele_tuple = findElement(d, ele_dict)
#     for arg in user_list:
#         sendVals(ele_tuple, arg)  # arg是user_list列表中的其中一个字典
#         result = checkResult(d, ele_dict['err_id'], arg, log)
#         if result:
#             # logout注销
#             logout(d, ele_dict)
#             # login重新登陆
#             ele_tuple = findElement(d, ele_dict)
#     log.log_close()
