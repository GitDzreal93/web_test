import os
import time

# 路径设置
# 项目路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
# Case 固化存放仓库：简称：TC：TestCase
TC_DIR = os.path.join(BASE_DIR, 'TestCase').replace("\\", "/")
# Case 工作仓库：简称：TCR：TestCaseRuntime
TCR_DIR = os.path.join(BASE_DIR, 'TestCaseRuntime').replace("\\", "/")
# 存放网页 对象-XPATH 映射文件的目录
ELE_DIR = os.path.join(BASE_DIR, 'EleMapping').replace("\\", "/")
# 存放测试数据的目录
DATA_DIR = os.path.join(BASE_DIR, 'DataConf').replace("\\", "/")
# 存放测试报告的目录
REPORT_DIR = os.path.join(BASE_DIR, 'Report').replace("\\", "/")

# chromedriver驱动
CHROMEDRIVER_PATH = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
# firefox驱动
GECKODRIVER_PATH = r'C:\Users\Dzreal_93\AppData\Local\Programs\Python\Python35\geckodriver.exe'

# 时间设置
NOW = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
DAY = time.strftime('%Y-%m-%d', time.localtime(time.time()))

# 操作者名单{名字：邮箱}，不在名单内的，不能操作本框架
OPERATOR = {
    'Dzreal': 'Dzreal_93@126.com'
}

# 测试完毕后是否清除case工作仓库（0 不清除；1 清除）
IS_CLEAN_TCR = 0
