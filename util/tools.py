# @Time    : 2018/1/25 13:22
# @Author  : Dzreal
# @Site    : 
# @File    : tools.py
# @Software: PyCharm

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

# 等待函数进行完再进行下一操作
def get_ele_times(driver, times, func):
    return WebDriverWait(driver,times).until(func)

# 打开浏览器
def openBrower(browser):
    '''
    return webdriver Handle
    '''
    webdriver_handle = None
    if browser == 'firefox':
        webdriver_handle = webdriver.Firefox()
    else:
        pass

    return webdriver_handle

# 打开URL
def openUrl(handle, url):
    '''
    load url
    '''
    handle.get(url)
    handle.maximize_window()

# 查找页面元素
def findElement(d, arg):
    '''
    arg must be dict
    1:text_id
    2:userid
    3:pwdid
    4:loginid
    return useEle, pwdEle, loginEle
    '''
    if 'text_id' in arg:
        ele_login = get_ele_times(d, 5, lambda d:d.find_element_by_link_text(arg['text_id']))
        ele_login.click()
    useEle = d.find_element_by_id(arg['userid'])
    pwdEle = d.find_element_by_id(arg['pwdid'])
    loginEle = d.find_element_by_class_name(arg['loginid'])
    return useEle, pwdEle, loginEle

# 填写表单数据函数
def sendVals(eletuple, arg):
    '''
    ele tuple
    account : uname, pwd
    '''
    listkey = ['uname', 'pwd']
    i = 0
    for key in listkey:
        print(type(eletuple))
        eletuple[i].send_keys('')
        eletuple[i].clear()
        time.sleep(1)
        eletuple[i].send_keys(arg[key])
        time.sleep(1)
        i+=1
        # if i==2:
        #     eletuple[2].click()

    eletuple[2].click()

# 错误检查函数
def checkResult(d, err_id, arg, log):
    result = False
    time.sleep(2)           #服务器是有响应的过程，不加休眠，就会提示报错（假如账号密码正确，也打印出err的日志）

    try:
        err = d.find_element_by_id(err_id)
        print("Account And Pwd Error!")
        # msg = 'uname=%s pwd=%s:error:%s\n'%(arg['uname'], arg['pwd'], err.text)   #打印TXT日志，则将这两句注释去掉
        # log.log_write(msg)
        log.log_write(arg['uname'], arg['pwd'], 'Error', err.text)

    except:
        print("Account And Pwd Right!")
        # msg = 'uname=%s pwd=%s:pass\n' % (arg['uname'], arg['pwd'])
        # log.log_write(msg)
        log.log_write(arg['uname'], arg['pwd'], 'Pass')
        result = True
    return result

# 注销登录函数
def logout(d, ele_dict):
    ele = d.find_element_by_class_name(ele_dict['usermenu'])
    ActionChains(d).move_to_element(ele).perform()
    d.find_element_by_link_text(ele_dict['logout']).click()

# 登录操作函数
def login_test(ele_dict, user_list):
    d = openBrower()
    log = Xlloginfo()
    log.log_init('sheet1', 'uname', 'pwd', 'result', 'msg')
    openUrl(d, ele_dict['url'])
    ele_tuple = findElement(d, ele_dict)
    for arg in user_list:
        sendVals(ele_tuple, arg)                #arg是user_list列表中的其中一个字典
        result = checkResult(d, ele_dict['err_id'], arg, log)
        if result:
            #logout注销
            logout(d, ele_dict)
            #login重新登陆
            ele_tuple = findElement(d, ele_dict)
    log.log_close()

if __name__ == '__main__':
    # 从json文件解析元素信息
    ele_dict = get_webinfo(r'F:\Python\autoTestFlame\ele_config\json_info.json')

    # 从excel读取用户信息
    xinfo = XlUserinfo(r'F:\Python\autoTestFlame\input_data\userinfo.xls')
    user_list = xinfo.get_sheetinfo_by_index(0)

    #file webinfo / userinfo    1.ele_dict = get_webinfo(path) 2.user_list = get_userinfo(path)
    login_test(ele_dict, user_list)

